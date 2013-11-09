import MySQLdb
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):

  # First things first - clear any old URL entries.
  library.remove_expired_urls()

  # Grab the requested short_url. Strip it of white space, and remove
  # the initial forward slash.
  request = environ["REQUEST_URI"]
  short_url = request.strip()[1:]
  
  # Find the target in the database if possible.
  target = library.get_redirect_target( short_url )

  if target is None:
    f = open(goconfig.doc_root + "/site_data/top.part", "r")
    top = f.read()
    f.close()
    f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
    bottom = f.read()
    f.close()

    response = []
    response.append( top )
    response.append( "<p>Nothing here.</p>" )
    response.append( bottom )

    response = ''.join( response )

    status = '200 OK'
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(response)))]
    start_response(status, response_headers)

    return [response]

  else:

    ## incorporate piwik python api thing HERE

    status = '303 See other'
    response_headers = [('Location', target)]
    start_response(status, response_headers)

    return ['Redirecting to url . . .']
