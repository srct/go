import random
import time
import math
import site
import MySQLdb
import Cookie
import cookielib
import hashlib
import ldap

site.addsitedir('/srv/http/go/wsgi')
import goconfig


# Extract the value of the cookie if one is set.
def get_cookie_value( environ ):
  cookie = Cookie.SimpleCookie()
  
  # if the environment contains a cookie, check it out
  if environ.has_key('HTTP_COOKIE'):
    # load the cookie we found
    cookie.load(environ['HTTP_COOKIE']);
    if cookie.has_key('user'):
      user_hash = cookie['user'].value
      return user_hash

  return None


# Determine if a user is appropriately validated through LDAP.
def user_logged_in( environ ):
  user_hash = get_cookie_value(environ)
  if( user_hash is not None ):
    # see if it's in the database
    mdb,cursor = connect_to_mysql()
    sql = """SELECT count(*) FROM `%s` WHERE `user_hash`=%s;"""
    cursor.execute( sql, (goconfig.sql_usr_table, user_hash) )
    ((num_rows,),) = cursor.fetchall()
    
    mdb.commit()
    mdb.close()
    
    return num_rows > 0
  
  return False


def get_username( environ ):
  user_hash = get_cookie_value( environ )
  username = None
  if( user_hash is not None ):
    mdb,cursor = connect_to_mysql()
    try:
      sql = """SELECT `user` FROM `%s` WHERE `user_hash`=%s;"""
      cursor.execute( sql, (goconfig.sql_usr_table, user_hash ) )
      ((username,),) = cursor.fetchall()
      mdb.commit()
    finally:
      mdb.close()
  return username


def user_approved( username ):
  mdb,cursor = connect_to_mysql()
  sql = """SELECT `approved` FROM `%s` WHERE `user`=%s;"""
  cursor.execute( sql, (goconfig.sql_registration_table, username) )
  ((approved,),) = cursor.fetchall()
  mdb.commit()
  mdb.close()
  if approved == 1:
    return True
  else:
    return False


# Determine if the user has posting permissions via the registration
# datbase.
def user_registered( username ):
  mdb,cursor = connect_to_mysql()
  sql = """SELECT count(*) FROM `%s` WHERE `user`=%s;"""
  cursor.execute( sql, (goconfig.sql_registration_table, username) )
  ((num_rows,),) = cursor.fetchall()
  
  mdb.commit()
  mdb.close()
  
  return num_rows > 0


# Register a user --- that is, enter them in the registered database with a 
# false (default=0) approval flag.
def register_user( user, name, desc ):
  mdb,cursor = connect_to_mysql()
  output = False
  try:
    sql = """INSERT INTO `%s`(`user`, `name`, `comment`) VALUES (%s, %s, %s)"""
    cursor.execute( sql, (goconfig.sql_registration_table, user, name, desc) )
    output = True
  except MySQLdb.IntegrityError:
    pass
  mdb.commit()
  mdb.close()
  return output


# Log in a user by placing a cookie on their machine and entering
# the related hash in a SQL database.
def generate_cookie( user ):
  # generate a random 32-character salt
  ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  chars=[]
  for i in range(32):
    chars.append( random.choice(ALPHABET) )
  salt = "".join(chars)
  
  # generate a randomized hash for this user
  hashed_value = hashlib.sha512( user + salt ).hexdigest()
  cookie = Cookie.SimpleCookie()
  cookie["user"] = hashed_value
  cookie["user"]["expires"] = ""
  cookie["user"]["path"] = "/"
  return cookie


# Generate an expired cookie in order to remove any preexisting cookie.
def eat_cookie():
  cookie = Cookie.SimpleCookie()
  cookie["user"] = "goodbye"
  cookie["user"]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"
  cookie["user"]["path"] = "/"
  return cookie


# Register the user in the table of active users.
def activate_user( hash_value, user ):
  mdb,cursor = connect_to_mysql()
  sql = """INSERT INTO `%s` (`user_hash`,`user`) VALUES (%s,%s);"""
  cursor.execute( sql, (goconfig.sql_usr_table, hash_value, user) )
  mdb.commit()
  mdb.close()


# Unregister the user in the table of active users.
def deactivate_user( hash_value ):
  mdb, cursor = connect_to_mysql()
  sql = """DELETE FROM `%s` WHERE `user_hash`=%s;"""
  cursor.execute( sql, (goconfig.sql_usr_table, hash_value) )
  mdb.commit()
  mdb.close()


# Connect to a mySQL database and return a pointer to that database.
def connect_to_mysql():
  # Connect to and choose the database.
  mdb = MySQLdb.connect(
    goconfig.sql_domain,
    goconfig.sql_usr,
    goconfig.sql_pasw,
    goconfig.sql_db )
  cursor = mdb.cursor()
  
  # If we need to create the table, then construct it.
  # REGISTERED USER TABLE
  sql = """CREATE TABLE IF NOT EXISTS `'%s'`(
  user VARCHAR(50) CHARACTER SET 'utf8' NOT NULL,
  PRIMARY KEY(user),
  name VARCHAR(100) CHARACTER SET 'utf8' NOT NULL,
  comment VARCHAR(500) CHARACTER SET 'utf8' NOT NULL,
  approved INT(1) NOT NULL DEFAULT '0'
  )
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;""" % ( goconfig.sql_registration_table )
  cursor.execute( sql )
  
  # ACTIVE USER TABLE
  sql = """CREATE TABLE IF NOT EXISTS `'%s'`(
  id INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY(id),
  user_hash VARCHAR(500) CHARACTER SET 'utf8' NOT NULL,
  user VARCHAR(50) CHARACTER SET 'utf8' NOT NULL,
  CONSTRAINT `fk_active_user` FOREIGN KEY (`user`)
    REFERENCES `%s`.`'%s'`(`user`)
    ON DELETE CASCADE ON UPDATE CASCADE
  )
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;""" % (
    goconfig.sql_usr_table,
    goconfig.sql_db,
    goconfig.sql_registration_table
  )
  cursor.execute( sql )
  
  sql = """CREATE TABLE IF NOT EXISTS `'%s'`(
  id INT NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY(id),
  longurl VARCHAR(1000) CHARACTER SET 'utf8' NOT NULL,
  shorturl VARCHAR(100) CHARACTER SET 'utf8' NOT NULL,
  expiration INT(50) UNSIGNED NOT NULL,
  user VARCHAR(50) CHARACTER SET 'utf8' NOT NULL,
  clicks INT(10) UNSIGNED NOT NULL,
  CONSTRAINT `fk_url_user` FOREIGN KEY (`user`)
    REFERENCES `%s`.`'%s'`(`user`)
    ON DELETE CASCADE ON UPDATE CASCADE
  )
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;""" % ( 
    goconfig.sql_url_table,
    goconfig.sql_db,
    goconfig.sql_registration_table
  )
  cursor.execute( sql )
  
  return mdb, cursor


# Parse post data submitted to this function. That is, split it up as a
# dictionary and return that readable dictionary.
def parse_post_data( post_data ):
  delimiter = "&"
  subdelimiter = "="
  data = post_data.read()
  if len( data ) > 0:
    # create a dictionary as {field:val, field:val, ... }
    data = dict( item.split(subdelimiter) for item in data.split( delimiter ) )
    return data
  
  return None


# Generate a random short url from a list of possible characters
# and the minimum allowed length.
def generate_short_url( long_url ):
  decimal = 10
  encoding = 62
  
  # determine the range of possible values (set by goconfig.min_url_len)
  min_val = encoding ** (goconfig.min_url_len - 1)
  max_val = (encoding ** goconfig.min_url_len) - 1
  
  # generate the short url (some val between min and max)
  value = random.randint( min_val, max_val )
  
  # Encode the short url value in the most appropriate base.
  short = []
  
  # define the list of possible characters
  charlist = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
  
  while value > 0:
    short.append(charlist[ int(value % encoding) ])
    value = math.floor( value / encoding )
  
  return ''.join( short )


# This function should return true if the specified short_url
# already exists in the mySQL database. This prevents overlapping.
def short_url_exists( short_url ):
  mdb, cursor = connect_to_mysql()
  sql = """SELECT * FROM `%s` WHERE `shorturl` = %s;"""
  output = cursor.execute( sql, (goconfig.sql_url_table, short_url) )
  mdb.commit()
  mdb.close()
  return True if output > 0 else False


# Inserts a short-url, long-url pairing into the database.
def register_url( longurl, shorturl, expiration, environ ):
  username = get_username( environ )
  mdb, cursor = connect_to_mysql()
  sql = """INSERT INTO `%s`(`id`, `longurl`, `shorturl`, `expiration`, `user`, `clicks`)
  VALUES (NULL, %s, %s, %s, %s, '0')"""
  cursor.execute( sql, (goconfig.sql_url_table, longurl, shorturl, expiration, username) )
  mdb.commit()
  mdb.close()


# Removes any expired urls in the url table.
def remove_expired_urls():
  mdb, cursor = connect_to_mysql()
  today = int(time.time())
  sql = """DELETE FROM `%s` WHERE `expiration` > 0 AND `expiration` < %s;"""
  cursor.execute( sql, (goconfig.sql_url_table, today) )
  mdb.commit()
  mdb.close()

def get_redirect_target( short_url ):
  mdb,cursor = connect_to_mysql()
  sql = """SELECT * FROM `%s` WHERE `shorturl` = %s;"""
  output = cursor.execute( sql, (goconfig.sql_url_table, short_url) )

  selection = cursor.fetchall()
  target = None

  # If at least one row has been found, then grab its long_url.
  # If no rows are found, though, then don't do anything more!
  if len(selection) > 0:
    row = selection[0]  # we are only interested in the first result
    target = row[1]     # this is the index of the longurl field
    uid = row[0]        # this is the index of the ID field

    sql = """UPDATE `%s` SET `clicks`=`clicks`+1 WHERE `id`=%s;"""
    cursor.execute( sql, (goconfig.sql_url_table, uid) )

  # Close the connection to the mySQL database.
  mdb.commit()
  mdb.close()

  return target


def ldap_authenticate( usr, psw ):
  bind = 'uid='+usr+',ou=people,o=gmu.edu'

  if( len(usr) > 0 and len(psw) > 0):

    # Try to talk with the LDAP server.
    ldap.set_option(ldap.OPT_X_TLS, ldap.OPT_X_TLS_DEMAND)
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

    try:
      ld = ldap.initialize( goconfig.ldap_domain )
      result = ld.simple_bind_s( bind, psw )
      if result is not None:
        return True
    except ldap.INVALID_CREDENTIALS:
      pass
    except ldap.INAPPROPRIATE_AUTH:
      pass
    except ldap.NO_SUCH_OBJECT:
      pass

  return False


def get_top( logged_in=False ):
  f = open(goconfig.doc_root + "/site_data/top.part", "r")
  top = f.read()
  f.close()

  myaccount = """| [ <a href="/account">My Account</a> ]"""
  if logged_in:
    top = top.replace( "%{myaccount}%", myaccount )
  else:
    top = top.replace( "%{myaccount}%", "" )

  mylinks = """| [ <a href="/mylinks">My Links</a> ]"""
  if logged_in:
    top = top.replace( "%{mylinks}%", mylinks )
  else:
    top = top.replace( "%{mylinks}%", "" )

  return top


def get_bottom( logged_in=False ):
  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom = f.read()
  f.close()

  logout = """<a href="/logout">Log Out</a>"""
  if logged_in:
    bottom = bottom.replace( "%{logout}%", logout )
  else:
    bottom = bottom.replace( "%{logout}%", "" )

  return bottom


def get_links( username ):
  mdb,cursor = connect_to_mysql()
  sql = """SELECT * FROM `%s` WHERE `user`=%s;"""
  cursor.execute( sql, (goconfig.sql_url_table, username) )
  result = cursor.fetchall()
  mdb.commit()
  mdb.close()
  return result

def piwik_track( environ ):
  from piwikapi.tracking import PiwikTracker
  from piwikapi.tests.request import FakeRequest

  headers = {
    'HTTP_USER_AGENT': environ['HTTP_USER_AGENT'],
    'REMOTE_ADDR': environ['REMOTE_ADDR'],
    'HTTP_REFERER': environ['HTTP_REFERER'],
    'HTTP_ACCEPT_LANGUAGE': environ['HTTP_ACCEPT_LANGUAGE'],
    'SERVER_NAME': environ['SERVER_NAME'],
    'PATH_INFO': environ['PATH_INFO'],
    'QUERY_STRING': environ['QUERY_STRING'],
    'HTTPS': False,
  }

  request = FakeRequest(headers)
  piwiktracker = PiwikTracker(goconfig.piwik_site_id, request)
  piwiktracker.set_api_url(goconfig.piwik_tracking_api_url)

  piwiktracker.set_ip(headers['REMOTE_ADDR'])
  #piwiktracker.set_token_auth(PIWIK_TOKEN_AUTH)

  # submit tracking entry
  piwiktracker.do_track_page_view('My Page Title')
