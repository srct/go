from cgi import parse_qs, escape
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):

  if( not library.user_logged_in( environ ) ):
    status = '303 See other'
    response_headers = [('Location', '/login')]
    start_response(status, response_headers)
    return ['Redirecting to login . . .']

  if not (environ["REQUEST_METHOD"] == "GET"):
    status = '303 See other'
    response_headers = [('Location', '/')]
    start_response(status, response_headers)
    return ['Redirecting to index . . .']

  body = []

  # Grab user data.
  data = parse_qs(environ['QUERY_STRING'])
  short_url = data.get("u", [''])[0]
  short_url = escape(short_url)

  username = library.get_username( environ )
  links = library.get_links( username )

  if links is not None:
    for link in links:
      (link_id, _, link_short_url, _, _, _) = link
      if short_url == link_short_url:
        library.delete_url( link_id )

  status = '303 See other'
  response_headers = [('Location', '/mylinks')]
  start_response(status, response_headers)
  return ['Redirecting to mylinks . . .']
