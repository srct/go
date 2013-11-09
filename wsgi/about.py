import ldap
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):

  f = open(goconfig.doc_root + "/site_data/top.part", "r")
  top = f.read()
  f.close()

  f = open(goconfig.doc_root + "/site_data/about.part", "r")
  about = f.read()
  f.close()

  f = open(goconfig.doc_root + "/site_data/bottom.part", "r")
  bottom = f.read()
  f.close()

  response = top + about + bottom

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
