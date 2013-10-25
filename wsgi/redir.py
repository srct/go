import MySQLdb
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):
  # First things first - clear any old URL entries.
  library.remove_expired_urls()
  
  # Construct the default body, along with its header/footer wrapper.
  body = ["<p>Nothing here.</p>"]
  f = open(goconfig.doc_root + "/site_data/top.part", "r")
  top_part = f.read()
  f.close()
  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom_part = f.read()
  f.close()
  
  # Set up an empty URL in case we can't find one in the database.
  url = None
  
  # Grab the requested short_url. Strip it of white space, and remove
  # the initial forward slash.
  request = environ["REQUEST_URI"]
  target = request.strip()[1:]
  
  try:
    # Connect to and choose the database.
    mdb,cursor = library.connect_to_mysql()
    
    # Query the database for the short_url value.
    sql = """SELECT * FROM `%s` WHERE `shorturl` = %s;"""
    query = cursor.execute( sql, (goconfig.sql_url_table, target) )
    
    # If at least one row has been found, then grab its short_url.
    # If no rows are found, though, then don't do anything more!
    if query > 0:
      # Grab the data from the database.
      selection = cursor.fetchall()
      row = selection[0]  # we are only interested in the first result
      url = row[1]        # this is the index of the longurl field
      uid = row[0]        # this is the index of the ID field
      
      sql = """UPDATE `%s` SET `clicks`=`clicks`+1 WHERE `id`=%s;"""
      query = cursor.execute( sql, (goconfig.sql_url_table, uid) )
    
    # Close the connection to the mySQL database.
    mdb.commit()
    mdb.close()
    
  except MySQLdb.OperationalError:
    body.append( "<p>Error in mySQL database.</p>" )
  
  body = ''.join( body )
  
  if url == None:
    response = top_part + body + bottom_part
    
    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(response)))]
    start_response(status, response_headers)
    
    return [response]
    
  else:
    status = '303 See other'
    response_headers = [('Location', url)]
    start_response(status, response_headers)
    
    return ['Redirecting to url . . .']
    
