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
    <form action="/login" method="post">
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

  if not (environ["REQUEST_METHOD"] == "POST"):

    body = []
    body.append( login_form )

  else:

    body = []

    # Grab user data, cut off non-relevant fields.
    data = environ['wsgi.input']
    data = library.parse_post_data( data )

    # Determine the user credentials to authenticate.
    usr = data['usr']
    psw = data['pass']

    success = library.ldap_authenticate( usr, psw )

    if( success ):
      # create a hashed cookie
      cookie = library.generate_cookie(usr)
      cookie_value = cookie["user"].OutputString()
      hash_value = cookie["user"].value

      if( library.user_registered( usr ) ):
        if( library.user_approved( usr ) ):
          # deactivate the user, in case they're already in
          ###library.deactivate_user( hash_value )
          # activate the hashed user with the SQL database
          library.activate_user( hash_value, usr )

          # push the cookie to the user and redirect
          status = '303 See Other'
          response_headers = [('Set-Cookie', cookie_value),
                              ('Location', '/'),
                              ('Content-type', 'text/plain')]
          start_response(status, response_headers)
          return [ str(cookie) ]

        else:
          body = [""]
          body.append("<p>Your account has been registered and is being processed.</p>")
          body.append("<p>You will be notified when you are granted access.</p>")

      else:
        body = [""]
        body.append("<p>You do not currently have permission to use this ")
        body.append("service. Please <a href=\"/signup\">apply</a> for access.</p>")
        body.append("<p>If you believe this message is in error, please contact ")
        body.append("a SRCT <a href=\"mailto:exec@srct.gmu.edu\">SysAdmin</a>.</p>")

    else:
      body = ["<p>Error: Invalid username or password.</p>"]


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
