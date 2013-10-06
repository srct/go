import random
import time
import math
import site
import MySQLdb
import Cookie
import cookielib
import hashlib

site.addsitedir('/srv/http/wsgi')
import goconfig


# Determine if a user is appropriately validated through LDAP.
def user_logged_in( environ ):
  cookie = Cookie.SimpleCookie()
  
  # if the environment contains a cookie, check it out
  if environ.has_key('HTTP_COOKIE'):
    # load the cookie we found
    cookie.load(environ['HTTP_COOKIE']);
    if cookie.has_key('user'):
      user_hash = cookie['user'].value
      
      # see if it's in the database
      mdb,cursor = connect_to_mysql()
      sql = """SELECT count(*) FROM `%s` WHERE `user_hash`=%s;"""
      cursor.execute( sql, (goconfig.sql_usr_table, user_hash) )
      ((num_rows,),) = cursor.fetchall()
      
      mdb.commit()
      mdb.close()
      
      return num_rows > 0
  
  return False


# Log in a user by placing a cookie on their machine and entering
# the related hash in a SQL database.
def generate_cookie( user ):
  hashed_value = hashlib.sha512( user + goconfig.hash_salt ).hexdigest()
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
def activate_user( hash_value ):
  mdb,cursor = connect_to_mysql()
  sql = """INSERT INTO `%s` (`user_hash`) VALUES (%s);"""
  cursor.execute( sql, (goconfig.sql_usr_table, hash_value) )
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
  
  # If we need to create the urls table, then construct it.
  sql = """CREATE TABLE IF NOT EXISTS `%s`(
  id INT NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY(id), 
  longurl VARCHAR(100), 
  shorturl VARCHAR(100),
  expiration INT(50),
  clicks INT(10));"""
  cursor.execute( sql, (goconfig.sql_url_table) )
  
  sql = """CREATE TABLE IF NOT EXISTS `%s`(
  id INT NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY(id), 
  user_hash VARCHAR(500));"""
  cursor.execute( sql, (goconfig.sql_usr_table) )
  
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
def register_url( longurl, shorturl, expiration ):
  mdb, cursor = connect_to_mysql()
  sql = """INSERT INTO `%s`(`id`, `longurl`, `shorturl`, `expiration`, `clicks`)
  VALUES (NULL, %s, %s, %s, '0')"""
  cursor.execute( sql, (goconfig.sql_url_table, longurl, shorturl, expiration) )
  mdb.commit()
  mdb.close()


# Removes any expired urls in the url table.
def remove_expired_urls():
  mdb, cursor = connect_to_mysql()
  today = int(time.time())
  sql = """DELETE FROM `%s` WHERE `expiration` > 0 AND `expiration` < %d;"""
  cursor.execute( sql, (goconfig.sql_url_table, today) )
  mdb.commit()
  mdb.close()
