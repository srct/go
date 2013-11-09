import ldap
import site

site.addsitedir('/srv/http/go/wsgi')
import library
import goconfig

def application(environ, start_response):

  body = []

  signup_form = """
      <h3>~Sign Up for Use~</h3>
      <form action="/signup" method="post">

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
        <br /><br />

        <input type="submit" name="submit" value="APPLY" />

        <p>Submitting an application indicates acceptance of the
        <a href="http://srct.gmu.edu/usage-policy">SRCT Usage Policy</a>.</p>

      </form>
    """

  if not (environ["REQUEST_METHOD"] == "POST"):

    body = []
    body.append( signup_form )

  else:

    # Grab user data, cut off non-relevant fields.
    data = environ['wsgi.input']
    data = library.parse_post_data( data )
    
    user = data['user'].strip().replace('+',' ').lower()
    name = data['name'].strip().replace('+',' ')
    desc = data['desc'].strip().replace('+',' ')

    if len(user) > 0 and len(name) > 0 and len(desc) > 0:
      if library.register_user( user, name, desc ):
        body = []
        body.append("<h3>~Sign Up for Use~</h3>")
        body.append("<p>Application success! Please wait for moderator ")
        body.append("approval before using this service.<br/><br/></p>")
      else:
        body = []
        body.append("<h3>~Error~</h3>")
        body.append("<p>That username is already registered!<br/><br/></p>")
    else:
      body = []
      body.append("<h3>~Error~</h3>")
      body.append("<p>Please complete all forms before submitting.<br/><br/></p>")


  user_logged_in = library.user_logged_in( environ )
  top = library.get_top( user_logged_in )
  bottom = library.get_bottom( user_logged_in )

  body = ''.join( body )
  response = top + body + bottom

  status = '200 OK'
  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(len(response)))]
  start_response(status, response_headers)

  return [response]
