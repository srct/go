import ldap
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):

  if( library.user_logged_in( environ ) ):
    status = '303 See other'
    response_headers = [('Location', '/')]
    start_response(status, response_headers)
    return ['Redirecting to index . . .']

  body = []

  login_form = """
    <h3>~Login~</h3>
    <form action="/authenticate" method="post">
      <label for="usr">username</label>
      <br /><br />
      <input type="text" id="usr" name="usr" value="" />
      <br /><br />
      <label for="pass">password</label>
      <br /><br />
      <input type="password" id="pass" name="pass" value="" />
      <br /><br />
      <input type="submit" name="submit" value="LOGIN" />
      <p>
        <br />
        You must be <a href="/signup">registered</a> in
        order to use this service.
        <br /><br />
      </p>
    </form>
  """

  body.append( login_form )

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
