import random
import math
import site


# Determine if a user is appropriately validated through LDAP.
def user_logged_in():
  return False


# Given a dictionary and a set of relevant entries, this procedure 
# removes all irrelevant entries, effectively trimming the noise level
def trim_noise( dictionary, relevant_keys ):
  marked_for_removal = []
  
  for key in dictionary:
    if key not in relevant_keys:
      marked_for_removal.append( key )
  for item in marked_for_removal:
    del dictionary[item]


# Parse post data submitted to this function. That is, split it up as a
# dictionary and return that readable dictionary.
def parse_post_data( post_data ):
  delimiter = "&"
  subdelimiter = "="
  
  # read stream to a list
  data = post_data.read()
  
  if len( data ) > 0:
    
    # create a dictionary as {field:val, field:val, ... }
    data = dict( item.split(subdelimiter) for item in data.split( delimiter ) )
    
    # return the dictionary of data
    return data
  
  # if there is no data, return an empty result
  return None


# Generate a random short url from a list of possible characters
# and the minimum allowed length.
def generate_short_url( long_url, min_len ):
  decimal = 10
  encoding = 62
  
  # determine the range of possible values (set by min_len)
  min_val = encoding ** (min_len - 1)
  max_val = (encoding ** min_len) - 1
  
  # generate the short url (some val between min and max)
  value = random.randint( min_val, max_val )
  
  # Encode the short url value in the most appropriate base.
  short = []
  
  # define the list of possible characters
  charlist = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
  
  while value > 0:
    short.append(charlist[ int(value % encoding) ])
    value = math.floor( value / encoding )
  
  return ''.join( short )


# This function should return true if the specified short_url
# already exists in the mySQL database. This prevents overlapping.
def short_url_exists( cursor, table, short_url ):
  output = cursor.execute( 
  """ SELECT * from """ + table +
  """ WHERE shorturl = %s """, (short_url))
  output = True if output > 0 else False
  return output


