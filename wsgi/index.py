import ldap
import site

site.addsitedir('/srv/http/go/wsgi')
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
      <br />
      You must be pre-approved by a SRCT <a
      href="mailto:exec@srct.gmu.edu">SysAdmin</a> to use this service.
      <br /><br />
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
  #body.append( login_form )
  
  url_form = """
    <form action="/exec/rg" method="post" target="_self">
      <br />
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
