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

  url_form = """
    <h3>~Shorten URL~</h3>
    <form action="/register-url" method="post" target="_self">
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

  body.append( url_form )

  f = open(goconfig.doc_root + "/site_data/top.part", "r")
  top = f.read()
  f.close()
  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom = f.read()
  f.close()

  body = ''.join( body )
  response = top + body + bottom

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
