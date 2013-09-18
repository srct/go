import re
import urllib
import MySQLdb
import ldap
import site

site.addsitedir('/srv/http/wsgi')
import library
import goconfig


################ CONSTANT VALUES ####
# relevant input fields
fields = ["short-url", "long-url"]

url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
short_regex = re.compile(
        r'^[a-z0-9]+$', re.IGNORECASE)
#####################################

def application(environ, start_response):
  
  # Boolean flags which describe the validity of user input.
  INV_LU = False # invalid long url
  INV_SU = False # invalid short url
  SU_TS  = False # short url too short
  SU_EX  = False # short url already exists
  
  # Set default "empty page" text.
  body = ["<p>Nothing here.</p>"]

  # If the page was requested via POST, that means the URL-input 
  # form was submitted. Scan over the input data, parse it, validate
  # it, and then finally connect to the DB and store it. Then output.
  while environ["REQUEST_METHOD"] == "POST" and library.user_logged_in():
    
    # Grab user data, cut off non-relevant fields.
    data = environ['wsgi.input']
    data = library.parse_post_data( data )
    library.trim_noise( data, fields )
    
    # Store parsed user data in these handy variables.
    long_url = data["long-url"]
    short_url = data["short-url"]
    long_url = urllib.unquote( long_url )
    short_url = urllib.unquote( short_url )
    
    # Try to connect to the database and store this pairing
    # in the appropriate DB and Table.
    try:
      # Connect to and choose the database.
      mdb = MySQLdb.connect(
        goconfig.sql_domain,
        goconfig.sql_usr,
        goconfig.sql_pasw,
        goconfig.sql_db )
      cursor = mdb.cursor()
      
      # If we need to create the urls table, then construct it.
      cursor.execute("""CREATE TABLE IF NOT EXISTS %s(
      id INT NOT NULL AUTO_INCREMENT, 
      PRIMARY KEY(id), 
      longurl VARCHAR(100), 
      shorturl VARCHAR(100))""" % goconfig.sql_table)
      
      # If no custom short url identifier was entered, then 
      # generate a randomized value from the library.
      if len( short_url ) == 0:
        short_url = library.generate_short_url( long_url, goconfig.min_url_len )
        while library.short_url_exists( cursor, goconfig.sql_table, short_url ):
          short_url = library.generate_short_url( long_url, goconfig.min_url_len )
      
      
      # Check each possible error case and set flags accordingly.
      # 1) Check that long_url is a valid URL
      # 2) Check that short_url exceeds the minimum length
      # 3) Check that short_url only contains the appropriate characters
      # 4) Check that short_url doesn't already exist in the database
      if re.match(url_regex, long_url) == None:
        INV_LU = True       # long url validity
      if len( short_url ) < goconfig.min_url_len:
        SU_TS = True        # short url length
      if re.match(short_regex, short_url) == None:
        INV_SU = True       # short url validity
      if library.short_url_exists( cursor, goconfig.sql_table, short_url ):
        SU_EX = True        # short url uniqueness
      
      # Reset body of output to prepare for possible error/success msg.
      body = []
      
      # Depending on the values of error flags, display an appropriate
      # message to the user.
      if INV_LU:
        body.append("<p>You entered an invalid long url!</p>")
      if INV_SU:
        body.append("<p>The identifier can contain only letters and numbers.</p>")
      if SU_TS:
        body.append("<p>The identifier must be at least " + str(goconfig.min_url_len) + " characters.</p>")
      if SU_EX:
        body.append("<p>The identifier already exists in the database!</p>")
      
      # If none of the error flags have been thrown, then
      # append the success messages.
      # ie. Display the long and short URLs.
      if (not INV_LU) and (not INV_SU) and (not SU_TS) and (not SU_EX):
        body.append(
          '<p><em>Original URL:</em> <a href="%s">%s</a></p>' % 
          (long_url, long_url))
        body.append(
          '<p><em>Shortened URL:</em> <a href="/%s">%s</a></p>' % 
          (short_url, short_url))
      else:
        body.append(
          '<input type="submit" value="BACK" ' + 
          'onclick="history.back()" />')
        break;
      
      # If execution has proceeded this far, then all the error
      # flags must be down, and we are connected successfully to the
      # SQL database. If this is the case, then move on to 
      # insert the longurl-shorturl pairing in the database.
      cursor.execute( 
      """INSERT INTO """ + goconfig.sql_table + """ (id, longurl, shorturl) """ + 
      """VALUES (NULL, %s, %s)""", (long_url, short_url))
      
      # Commit changes and close connection.
      mdb.commit()
      mdb.close()
      
    except MySQLdb.OperationalError:
      body.append( "<p>Error in mySQL database.</p>" )
    finally:
      break
      
    break # failsafe in case we get to the end somehow!
  
  
  # Read and store in memory the header and footer sections 
  # of the page display.
  f = open(goconfig.doc_root + "/site_data/top.part", "r")
  top_part = f.read()
  f.close()
  
  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom_part = f.read()
  f.close()
  
  # Construct the HTML output using the wrapper and body data.
  body = ''.join( body )
  response = top_part + body + bottom_part
  
  # Do web-stuff
  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)
  
  return [response]
