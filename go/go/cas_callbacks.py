"""
go/cas_callbacks.py
"""

# Future Imports
from __future__ import unicode_literals, absolute_import, print_function, division

# Django Imports
from django.contrib.auth.models import User
from django.conf import settings

# Other Imports
import requests

def pfparse(pf_name_result):
    """
    Parse what peoplefinder sends back to us and make a list out of it
    """

    # name comes in format of Anderson, Nicholas J
    name_list = pf_name_result.split(',')
    # there's random whitespace with the first name
    first_name_section = name_list[1].strip()
    # check if there's a middle initial
    mi_q = first_name_section.split(' ')
    # make sure that the additional elements aren't multiple names
    if len(mi_q[-1]) == 1:
        first_name = ' '.join(mi_q[:-1])
    else:
        first_name = first_name_section
    # our list containing the name of the person in a usable list
    new_name_list = [first_name, name_list[0]]
    return new_name_list

def pfinfo(uname):
    """
    Get information from peoplefinder
    """

    base_url = settings.PF_URL
    url = base_url + "basic/all/" + str(uname)
    try:
        metadata = requests.get(url, timeout=5)
        print("Retrieving information from the peoplefinder api.")
        metadata.raise_for_status()
    except requests.exceptions.RequestException as ex:
        print("Cannot resolve to peoplefinder api:", ex)
        print("Returning empty user info tuple.")
        return ['', '']
    else:
        pfjson = metadata.json()
        try:
            if len(pfjson['results']) == 1:
                if pfjson['method'] == 'peoplefinder':
                    name_str = pfjson['results'][0]['name']
                    name = pfparse(name_str)
                elif pfjson['method'] == 'ldap':
                    name = [pfjson['results'][0]['givenname'], pfjson['results'][0]['surname']]
                else:
                    name = pfjson['results'][0]['name']
                return name
            else:
                if pfjson['method'] == 'peoplefinder':
                    name_str = pfjson['results'][1]['name']
                    name = pfparse(name_str)
                elif pfjson['method'] == 'ldap':
                    name = [pfjson['results'][1]['givenname'], pfjson['results'][1]['surname']]
                else:
                    name = pfjson['results'][0]['name']
                return name
        # if the name is not in peoplefinder, return empty first and last name
        except IndexError as ex:
            print("Name not found in peoplefinder.")
            return ['', '']
        except Exception as ex:
            print("Unknown peoplefinder error:", ex)
            print("Returning empty user info tuple.")
            return ['', '']

def create_user(tree):
    """
    Create a django user based off of the peoplefinder info we parsed earlier
    """

    print("Parsing CAS information.")
    try:
        username = tree[0][0].text
        user, user_created = User.objects.get_or_create(username=username)
    except Exception as ex:
        print("CAS callback unsuccessful:", ex)

    # error handling in pfinfo function
    info_name = pfinfo(username)

    try:
        if user_created:
            print("Created user object %s." % username)

            # set and save the user's email
            email_str = "%s%s" % (username, settings.EMAIL_DOMAIN)
            user.email = email_str
            # Password is a required User object field, though doesn't matter for our
            # purposes because all user auth is handled through CAS, not Django's login.
            user.set_password('cas_used_instead')
            user.save()
            print("Added user's email, %s." % email_str)

            user.first_name = info_name[0]
            user.last_name = info_name[1]
            user.save()
            print("Added user's name, %s %s." % (info_name[0], info_name[1]))

            print("User object creation process completed.")

        else:
            print("User object already exists.")

        print("CAS callback successful.")
    except Exception as ex:
        print("Unhandled user creation error:", ex)
