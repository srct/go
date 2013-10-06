##############################
# Site configuration variables
#
# These variables configure how the website is structured.
##############################

# doc_root: Describes where the website's root directory is.
doc_root = "/srv/http"

# domain: This is the domain the website is being hosted at.
domain = "go.gmu.edu"



##############################
# Database connection variables
#
# These variables configure how the website connects
# to the required database.
##############################

# sql_domain: The location of the SQL database to connect to.
sql_domain = "localhost"

# sql_usr: The username to use with this SQL database.
sql_usr    = "go-user"

# sql_pasw: The plaintext password used to connec to the SQL database.
sql_pasw   = "georgemasonsrct"

# sql_db: The SQL database or schema name to which to connect.
sql_db     = "go"

# sql_url_table: The SQL table storing the URL listing.
sql_url_table  = "urls"

# sql_usr_table: The SQL table storing the active users.
sql_usr_table = "usrs"

#ldap_domain: The location of the LDAP database to connect to.
ldap_domain = "ldaps://directory.gmu.edu:636"



##############################
# Behaviour configuration variables
#
# These variables define various system behaviors, such
# as global limits or values.
##############################

# min_url_len: This is the minimum required length of
#   a "short url" or url identifier.
min_url_len = 5

# hash_salt: This is the private salt used to salt cookie hashing.
hash_salt = "salty"
