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

  post = environ["REQUEST_METHOD"] == "POST"
  body = ["Nothing here."]

  if post:
    # Grab user data, cut off non-relevant fields.
    data = environ['wsgi.input']
    data = library.parse_post_data( data )
    
    user = data['user'].strip().replace('+',' ').lower()
    name = data['name'].strip().replace('+',' ')
    desc = data['desc'].strip().replace('+',' ')

    if len(user) > 0 and len(name) > 0 and len(desc) > 0:
      if library.register_user( user, name, desc ):
        body = ["<h3>~Sign-Up for Use~</h3>"]
        body.append("<p>Application success! Please wait for moderator ")
        body.append("approval before using this service.<br/><br/></p>")
      else:
        body = ["<h3>~Error~</h3>"]
        body.append("<p>That username is already registered!<br/><br/></p>")
    else:
      body = ["<h3>~Error~</h3>"]
      body.append("<p>Please complete all forms before submitting.<br/><br/></p>")
  else:
    body = ["""
      <h3>~Apply for Use~</h3>
      <form action="" method="post">

        <label for="user">username (NetID)</label>
        <br /><br />
        <input type="text" id="user" name="user" value="" />
        <br /><br />

        <label for="name">full name</label>
        <br /><br />
        <input type="text" id="name" name="name" value="" />
        <br /><br />

        <label for="desc">user description</label>
        <p>Provide a brief description of the user and why they require
        access to Go.</p>
        <textarea id="desc" name="desc"></textarea>

        <p>Submitting an application indicates acceptance of the
        <a href="http://srct.gmu.edu/usage-policy">SRCT Usage Policy</a>.</p>

        <input type="submit" name="submit" value="APPLY" />

        <br /><br />
      </form>
    """]

  body = ''.join( body )
  response = top_part + body + bottom_part

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
