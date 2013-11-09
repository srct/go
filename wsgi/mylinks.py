from datetime import datetime
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

  body = []

  user = library.get_username( environ )
  links = library.get_links( user )

  if len(links) == 0:
    body.append("<p>None found.</p>")

  else:
    body.append('<div id="mylinks">')

    for entry in links:
      (link_id, long_url, short_url, expiration, user, clicks) = entry

      link_text = '<a href="%s">%s</a>'
      short_url_link = link_text % (short_url, short_url)
      long_url_link = link_text % (long_url, long_url)
      delete_link = link_text % ("#", "<strong>Delete</strong>")

      if expiration <= 0:
        expiration = "never"
      else:
        expiration = datetime.fromtimestamp( int(expiration) )
        expiration = expiration.strftime('%m/%d/%Y')

      body.append("<p><strong>Long</strong>: ")
      body.append(long_url_link)
      body.append("<br /><strong>Short</strong>: ")
      body.append(short_url_link)
      body.append("<br /><strong>Clicks</strong>: ")
      body.append(str(clicks))
      body.append("<br /><strong>Expires</strong>: ")
      body.append(str(expiration))
      body.append("<br />")
      body.append(delete_link)
      body.append("</p>")

    body.append('</div>')

  user_logged_in = library.user_logged_in( environ )
  top = library.get_top( user_logged_in )
  bottom = library.get_bottom( user_logged_in )

  body = ''.join( body )
  response = top + body + bottom

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
