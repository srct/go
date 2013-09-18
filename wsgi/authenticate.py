import ldap
import site

site.addsitedir('/srv/http/wsgi')
import library
import goconfig


def application(environ, start_response):
  
  # Set default "empty page" text.
  body = ["<p>Nothing here.</p>"]

  # If the page was requested via POST, that means the URL-input 
  # form was submitted. Scan over the input data, parse it, validate
  # it, and then finally connect to the DB and store it. Then output.
  if environ["REQUEST_METHOD"] == "POST":
    
    # Grab user data, cut off non-relevant fields.
    data = environ['wsgi.input']
    data = library.parse_post_data( data )
    fields = ['usr', 'pass']
    library.trim_noise( data, fields )
    
    # Determine the user credentials to authenticate.
    usr = data['usr']
    psw = data['pass']
    
    body = [usr]
    #body = [ data ]
    
    # Try to talk with the LDAP server.
    #ld = ldap.initialize( goconfig.ldap_domain )
    #ld.simple_bind_s()
    #ld.unbind_s()
  
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
