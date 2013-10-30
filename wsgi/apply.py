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

  if environ["REQUEST_METHOD"] == "POST":
    
    # Grab user data, cut off non-relevant fields.
    data = environ['wsgi.input']
    data = library.parse_post_data( data )
    
    user = data['user']
    name = data['name']
    desc = data['desc']


  apply_form = """
    <form action="" method="post">
      <br />
      <label for="user">username (NetID)</label>
      <br /><br />
      <input type="text" id="user" name="user" value="" />
      <br /><br />
      <label for="name">full name</label>
      <br /><br />
      <input type="text" id="name" name="name" value="" />
      <br /><br />
      <label for="desc">user description</label>
      <br /><br />
      <textarea id="desc" name="desc"></textarea>
      <p>Submitting an application indicates implicit acceptance of the
      <a href="http://srct.gmu.edu/usage-policy">SRCT Usage Policy</a>.</p>
      <input type="submit" name="submit" value="APPLY" />
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
