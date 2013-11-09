import re
import urllib
import time
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
short_regex = re.compile(
        r'^[a-z0-9]+$', re.IGNORECASE)

def application(environ, start_response):

  if( not library.user_logged_in( environ ) ):
    status = '303 See other'
    response_headers = [('Location', '/login')]
    start_response(status, response_headers)
    return ['Redirecting to login . . .']

  body = []

  url_form = """
    <h3>~Shorten URL~</h3>
    <form action="/" method="post" target="_self">
      <label for="long-url">Long URL</label>
      <br /><br />
      <input type="text" id="long-url" name="long-url" value="http://" />
      <br /><br />
      <label for="short-url">Short URL (Optional)</label>
      <br /><br />
      <input type="text" id="short-url" name="short-url" value="" />
      <br /><br />
      <label>Expiration (Optional)</label>
      <br /><br />
      <input type="radio" name="expiration" value="day" id="day" />
      <label for="day" class="sublabel">1 Day</label>
      <input type="radio" name="expiration" value="week" id="week" />
      <label for="week" class="sublabel">1 Week</label>
      <input type="radio" name="expiration" value="month" id="month" />
      <label for="month" class="sublabel">1 Month</label>
      <input type="radio" name="expiration" value="never" id="never"
        checked="checked" />
      <label for="never" class="sublabel">Never</label>
      <br /><br />
      <input type="submit" name="submit" value="SHORTEN" />
      <br /><br />
    </form>
  """

  if not (environ["REQUEST_METHOD"] == "POST"):

    body = []
    body.append( url_form )

  else:

    body = []
    error = []

    # Grab user data, cut off non-relevant fields.
    data = environ['wsgi.input']
    data = library.parse_post_data( data )

    # Store parsed user data in these handy variables.
    long_url = data["long-url"]
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
