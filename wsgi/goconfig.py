##############################
# Site configuration variables
#
# These variables configure how the website is structured.
##############################

# doc_root: Describes where the website's root directory is.
doc_root = "/srv/http"



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
sql_db     = "srctgo"

# sql_table: The SQL table storing the URL listing.
sql_table  = "urls"

#ldap_domain: The location of the LDAP database to connect to.
ldap_domain = "ldap://ldap.gmu.edu"



##############################
# Behaviour configuration variables
#
# These variables define various system behaviors, such
# as global limits or values.
##############################

# min_url_len: This is the minimum required length of
#   a "short url" or url identifier.
min_url_len = 5

