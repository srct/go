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
      <br />
      <label for="usr">username</label>
      <br />
      <input type="text" id="usr" name="usr" value="" />
      <br /><br />
      <label for="pass">password</label>
      <br />
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
      <label for="long-url">long URL</label>
      <br />
      <input type="text" id="long-url" name="long-url" value="http://" />
      <br /><br />
      <label for="short-url" onClick="expand('identifier-div');">
        identifier (optional)
      </label>
      <br />
      <div style="display:none;" id="identifier-div" class="expands">
        <input type="text" id="short-url" name="short-url" value="" />
      </div>
      <br />
      <label onClick="expand('expiration-div');">expiration (optional)</label>
      <br />
      <div style="display:none;" id="expiration-div">
        <input type="radio" name="expiration" value="day" id="day"> 1
        Day</input>
        <input type="radio" name="expiration" value="week" /> 1 Week
        <input type="radio" name="expiration" value="month" /> 1 Month
        <input type="radio" name="expiration" value="never"
          checked="checked" /> Never
      </div>
      <br />
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
