import ldap
import site

site.addsitedir('/srv/http/wsgi')
import library
import goconfig

def application(environ, start_response):
  
  ## This application should display two the user one of two
  ##  screens, depending on the situation. 
  ## 
  ## Given an unverified user, display the login screen. 
  ##  On login, authenticate the user's credentials. If the credentials
  ##  are good, then consider the user logged in.
  ##
  ## Given a logged in user, display the URL register screen. On
  ##  submission, transfer control to the url-register script and 
  ##  allow it to verify submission content. If the url-register script
  ##  sends the user back here, the user should remain logged in and 
  ##  have no issues travelling back and forth.
  
  # Construct the default body, along with its header/footer wrapper.
  body = []
  f = open(goconfig.doc_root + "/site_data/top.part", "r")
  top_part = f.read()
  f.close()
  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom_part = f.read()
  f.close()
  
  login_form = """
    <form action="/exec/lg" method="post">
      <label for="usr">username</label>
      <p>Your administrator username (MasonID).</p>
      <input type="text" id="usr" name="usr" value="" />
      <br /><br />
      <label for="pass">password</label>
      <p>Your administrator password.</p>
      <input type="password" id="pass" name="pass" value="" />
      <br /><br />
      <input type="submit" name="submit" value="LOGIN" />
      <br />
    </form>
  """
  #body.append( login_form )
  
  url_form = """
    <form action="/exec/rg" method="post" target="_self">
      <label for="long-url">long URL</label>
      <p>Make sure to include http:// in front.</p>
      <input type="text" id="long-url" name="long-url" value="http://" />
      <br /><br />
      <label for="short-url">identifier</label>
      <p>What your want your URL to look like. This is optional.</p>
      <p>Identifier must be at least 5 characters, and only 
      contain letters and numbers.</p>
      <input type="text" id="short-url" name="short-url" value="" />
      <br /><br />
      <input type="submit" name="submit" value="SHORTEN" />
      <br />
    </form>
  """
  #body.append( url_form )
  
  if( library.user_logged_in( environ ) ):
    body.append( url_form )
  else:
    body.append( login_form )

  body = ''.join( body )
  response = top_part + body + bottom_part
  
  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)
  
  return [response]
