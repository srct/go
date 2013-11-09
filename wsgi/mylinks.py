import ldap
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):

  user_logged_in = library.user_logged_in( environ )
  top = library.get_top( user_logged_in )
  bottom = library.get_bottom( user_logged_in )

  body = "<p>Nothing here.</p>"

  response = top + body + bottom

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
