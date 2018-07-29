"""
go/cas_callbacks.py

Parse the CAS/PF responses and create users in the database.
"""
# Other Imports
import requests
# Django Imports
from django.conf import settings
from django.contrib.auth.models import User


def pfparse(pf_name_result: str) -> list:
    """
    Parse what peoplefinder sends back to us and make a list out of it.
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

def pfinfo(uname: str) -> list:
    """
    Get information from peoplefinder.
    """
    url = f"{settings.PF_URL}basic/all/{uname}"
    try:
        metadata = requests.get(url, timeout=30)
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

def create_user(tree: list):
    """
    Create a django user based off of the peoplefinder info we parsed earlier.
    """
    print("Parsing CAS information.")

    try:
        username = tree[0][0].text
        # error handling in pfinfo function
        info_name = pfinfo(username)
        # set and save the user's email
        email_str = "%s%s" % (username, settings.EMAIL_DOMAIN)

        user, user_created = User.objects.get_or_create(
            username=username,
            email=email_str,
            first_name=info_name[0],
            last_name=info_name[1]
        )
        # Password is a required User object field, though doesn't matter for our
        # purposes because all user auth is handled through CAS, not Django's login.
        user.set_password('cas_used_instead')
        user.save()

        if user_created:
            print("Created user object %s." % username)
        else:
            print("User object already exists.")

    except Exception as ex:
        print("CAS callback unsuccessful:", ex)
