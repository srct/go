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

  f = open(goconfig.doc_root + "/site_data/about.part", "r")
  about_part = f.read()
  f.close()

  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom_part = f.read()
  f.close()

  response = top_part + about_part + bottom_part

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
