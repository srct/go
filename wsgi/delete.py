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

  # Grab user data, cut off non-relevant fields.
  data = environ['wsgi.input']
  data = library.parse_data( data )

  # Store parsed user data in these handy variables.
  short_url = data["short_url"]
  expiration = data["expiration"]
  try:
    short_url = data["short-url"]
  except KeyError:
    pass

  if len(short_url) == 0:
    short_url = library.generate_short_url( long_url )
    while library.short_url_exists( short_url ):
      short_url = library.generate_short_url( long_url )

  # Prepend the long_url with a protocol if it doesn't have one.
  if not (long_url.startswith("http") or long_url.startswith("ftp")):
    long_url = "http://" + long_url

  # Un-quote the url for storage, if it's quoted.
  long_url = urllib.unquote( long_url )
  short_url = urllib.unquote( short_url )

  # Parse the expiration date.
  today = int(time.time())
  if expiration is None:
    end_stamp = today
  elif expiration == "never":
    end_stamp = 0
  elif expiration == "month":
    end_stamp = today + 2629740
  elif expiration == "week":
    end_stamp = today + 604800
  elif expiration == "day":
    end_stamp = today + 86400
  else:
    end_stamp = today

  # Add error messages if any are found.
  if re.match(url_regex, long_url) is None:
    error.append("<p>You entered an invalid long url!</p>")
  if len( short_url ) < goconfig.min_url_len:
    error.append("<p>The identifier must be at least ")
    error.append(str(goconfig.min_url_len) + " characters.</p>")
  if re.match(short_regex, short_url) == None:
    error.append("<p>The identifier can contain only letters and numbers.</p>")
  if library.short_url_exists( short_url ):
    error.append("<p>The identifier already exists in the database!</p>")

  if len(error) > 0: # at least one error found

    body = ["<h3>~Error~</h3>"]
    body.extend( error )
    body.append('<input type="submit" value="BACK" ')
    body.append('onclick="history.back()" /><br /><br />')

  else: # no error found

    # insert the longurl-shorturl pairing in the database.
    library.register_url( long_url, short_url, end_stamp, environ )
    display_short = goconfig.domain + "/" + short_url

    body = ["<h3>~Success~</h3>"]
    body.append(
      '<p><em>Original URL:</em> <a href="%s">%s</a></p>' % 
      (long_url, long_url))
    body.append(
      '<p><em>Shortened URL:</em> <a href="/%s">%s</a></p>' % 
      (short_url, display_short))


  status = '303 See other'
  response_headers = [('Location', '/mylinks')]
  start_response(status, response_headers)
  return ['Redirecting to index . . .']
