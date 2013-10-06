import ldap
import site
import Cookie

site.addsitedir('/srv/http/wsgi')
import library
import goconfig

def application(environ, start_response):
  
  # Grab the current user hash value cookie if there is one, and then
  # deactivate that hash value from the SQL database.
  current_cookie = Cookie.SimpleCookie()
  try:
    current_cookie.load( environ['HTTP_COOKIE'] )
    user_hash = current_cookie['user'].value
    library.deactivate_user( user_hash )
  except KeyError:
    pass
  
  # Generate an expired cookie to overwrite any existing cookie.
  expired_cookie = library.eat_cookie()
  expired_cookie_value = expired_cookie['user'].OutputString()
  
  # Push push push.
  status = '303 See Other'
  response_headers = [('Set-Cookie', expired_cookie_value),
                      ('Location', '/'),
                      ('Content-type', 'text/plain')]
  start_response(status, response_headers)
  
  return [ str(expired_cookie) ]
