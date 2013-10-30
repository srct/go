import ldap
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):

  # Construct the default body, along with its header/footer wrapper.
  body = []
  f = open(goconfig.doc_root + "/site_data/top.part", "r")
  top_part = f.read()
  f.close()
  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom_part = f.read()
  f.close()

  apply_form = """
    <form action="" method="post">
      <p>This form allows you to apply for registered access to the George
      Mason Student-Run Computing and Technology's Go URL shortening
      service. Access to this computing resource is governed by the <a
      href="http://srct.gmu.edu/usage-policy">SRCT Usage Policy</a>.
      Submitting an application indicates implicit acceptance of these
      terms. Misuse of this service will be handled strictly.</p>
      <br />
      <label for="usr">username</label>
      <br /><br />
      <input type="text" id="usr" name="usr" value="" />
      <br /><br />
      <label for="pass">password</label>
      <br /><br />
      <input type="password" id="pass" name="pass" value="" />
      <br /><br />
      <input type="submit" name="submit" value="LOGIN" />
      <br /><br />
    </form>
  """
  body.append( apply_form )

  body = ''.join( body )
  response = top_part + body + bottom_part

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
