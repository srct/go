"""
go/test_models.py
"""

# Django Imports
from django.contrib.auth.models import User
from django.db.utils import DataError, IntegrityError
from django.test import TestCase
from django.utils import timezone

# App Imports
from .models import URL, RegisteredUser

class RegisteredUserTest(TestCase):
    """
    Test cases for the RegisteredUser Model
    """

    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """

        User.objects.create(username='dhaynes', password='password')

    # user ---------------------------------------------------------------------

    def test_registereduser_creation(self):
        """
        check if RegisteredUsers are actually made
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        self.assertTrue(get_registered_user)

    # full_name ----------------------------------------------------------------

    def test_full_name(self):
        """
        check if full_name char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.full_name = "David Haynes"
        get_registered_user.save()

        self.assertEqual(get_registered_user.full_name, "David Haynes")

    def test_full_name_length(self):
        """
        check if full_name char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.full_name = """
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        """
        try:
            get_registered_user.save()
        except DataError as ex:
            self.assertTrue(ex)

    # blank=False is purely form validation related

    # organization -------------------------------------------------------------

    def test_organization(self):
        """
        check if organization char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.organization = "SRCT"
        get_registered_user.save()

        self.assertEqual(get_registered_user.organization, "SRCT")

    def test_organization_length(self):
        """
        check if organization char field functions as intentioned
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.organization = """
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        """

        try:
            get_registered_user.save()
        except DataError as ex:
            self.assertTrue(ex)


    # blank=False is purely form validation related

    # description --------------------------------------------------------------

    def test_description_blank(self):
        """
        - add in description (blank)
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        self.assertEqual(get_registered_user.description, "")

    def test_description_text(self):
        """
        - add in description (text)
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.description = "We're going to build a big beautiful testcase"
        get_registered_user.save()

        self.assertEqual(
            get_registered_user.description,
            "We're going to build a big beautiful testcase"
        )


    # registered ---------------------------------------------------------------

    def test_registered(self):
        """
        test the registered bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.registered = True
        get_registered_user.save()

        self.assertTrue(get_registered_user.registered)

    def test_registered_default(self):
        """
        test the registered bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)

        self.assertTrue(get_registered_user.registered)

    # approved -----------------------------------------------------------------

    def test_approved(self):
        """
        test the approved bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.approved = True
        get_registered_user.save()

        self.assertTrue(get_registered_user.approved)

    def test_approved_default(self):
        """
        test the approved bool default
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)

        self.assertFalse(get_registered_user.approved)

    # blocked ------------------------------------------------------------------

    def test_blocked(self):
        """
        test the blocked bool
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        get_registered_user.blocked = True
        get_registered_user.save()

        self.assertTrue(get_registered_user.blocked)

    def test_approved_default(self):
        """
        test the blocked bool default
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)

        self.assertFalse(get_registered_user.blocked)


    # __str__ ------------------------------------------------------------------

    def test_check_str(self):
        """
        check printing
        """

        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        expected = '<Registered User: dhaynes - Approval Status: True>'
        actual = str(get_registered_user)
        self.assertEqual(expected, actual)


class URLTest(TestCase):
    """
    Test cases for the URL Model
    """

    def setUp(self):
        """
        Set up any variables such as dummy objects that will be utilised in
        testing methods
        """

        # Setup a blank URL object with an owner
        User.objects.create(username='dhaynes', password='password')
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        URL.objects.create(owner=get_registered_user)

        # Create a dummy User object
        User.objects.create(username='evildhaynes', password='password')

    # owner --------------------------------------------------------------------

    def test_change_owner(self):
        """
        Test the ability to change the owner of a URL
        """

        # Original owner
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # New Owner
        get_user = User.objects.get(username='evildhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)

        # Change original owner to new owner 
        current_url.owner = get_registered_user
        current_url.save()

        self.assertEqual(current_url.owner, get_registered_user)

    # date_created -------------------------------------------------------------

    def test_date_created(self):
        """
        Test that the timedate is set properly on URL creation
        """

        # Get a date
        now = timezone.now()

        # Get the URL to apply it to
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Apply the date
        current_url.date_created = now
        current_url.save()

        self.assertEqual(current_url.date_created, now)


    # target -------------------------------------------------------------------

    def test_target(self):
        """
        Test that the target field properly accepts a URL
        """

        # Get a URL
        test_url = "https://dhaynes.xyz"

        # Get the URL to apply it to
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Apply the URL
        current_url.target = test_url
        current_url.save()

        self.assertEqual(current_url.target, test_url)

    def test_target_length(self):
        """
        Test that we can't input a URL longer than 1000 chars
        """

        # Get a URL
        test_url = "https://ymzvakaamyamelmshikymeodyqogjbmrxfgjsjowjjluzbhmgaahkoflhftnicprokfsmkwzoczfowboagwvarbtozszvumruvjlnmxcyhzltgijfatiacihrnbennvvuiwpjpredeyrqdqvkhyjixohrhpyrhrzaptzfeacvkopzkvxcxapknoelcfapjiwlvwnhulmsadiuzhvjevywwvkjordyhyrqntfueycgasyantpcnartxappzmmhbhtyplatqylunvdfkpcrvjjuvpnprxrgcxzbatfcvipvhetoiuknlnwscrgtwruatjazkrmsbyvrkxjiggejxormncbrxwajhhmuvsmzaclaehievayhtjbublhrljdfrudxcmnmokmlpdvhbgkicbfezdjyxhhspdnnufevvcncdbqkmqbubvrtaeiniowpjuqyuvxpjqfuejubjbphempwgvhlrvmtjuqafsopppjqujpinphyslfyyoiysoozblpjtigjaaqiwwoggjspbotzgwzzjvhgeztcnkzwjeejjzrjrhiqvjurrncoluwmcxmfmhngaqovpxocishflcfklyoowqlgnjsmagadlpgaphptpeoojqkyhsfcyhoxjnfwczhnunyhvlnzcdauydaipefedqalakkfexbkddcyjxofxgvrhriryrjzrnvoudkvuehbrhfwudgsrxktflglkqdqptxeadlhpvgwobwrbyrynbljuzjrogjgpkgfkhaawcykwzpqeahkigkmldxkrzavoqhivlebfhkmwvxgfgveaqdkgxtaixzdlhbdgcygeuwqfquqaojutlrybdrlfvxitectjyfdjtsinsuahnxsfovecymnuswkrcptpkgjreccmhznbxngzhzarmaxenhkfncmmzqyqpiccugfnxdiyifzyjawykpgheayboekztyitvajbwgrnmhrpprmuteofemxtcfqcekwbkqgggggggggggggggg.xyz"

        # Get the URL to apply it to
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Apply the URL
        current_url.target = test_url

        try:
            current_url.save()
        except DataError as ex:
            self.assertTrue(ex)


    # short --------------------------------------------------------------------

    def test_short(self):
        """
        Test that the short field functions as intended
        """

        # Get a short 
        test_short = "dhaynes"

        # Get the URL to apply it to
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Apply the short
        current_url.short = test_short
        current_url.save()

        self.assertEqual(current_url.short, test_short)

    def test_short_dupe(self):
        """
        Test that the short field primary key functions as intended
        """

        # Get a short 
        test_short = "dhaynes"

        # Get the URL to apply it to
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Apply the short
        current_url.short = test_short
        current_url.save()

        try:
            new_url = URL.objects.create(owner=get_registered_user, short="dhaynes")
            new_url.save()
        except IntegrityError as ex:
            self.assertTrue(ex)

    def test_short_length(self):
        """
        Test that a short field can be no longer than 20 characters
        """

        # Get a invalid short
        test_short = "ggggggggggggggggggggg"

        # Get the URL to apply it to
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Apply the URL
        current_url.short = test_short

        try:
            current_url.save()
        except DataError as ex:
            self.assertTrue(ex)

    # clicks -------------------------------------------------------------------

    def test_clicks(self):
        """
        Test that clicks incremention works
        """

        # Get the URL to test
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Increment
        current_url.clicks += 1
        current_url.save()

        self.assertEqual(current_url.clicks, 1)

    # qrclicks -----------------------------------------------------------------

    def test_qrclicks(self):
        """
        Test that cliqrclickscks incremention works
        """

        # Get the URL to test
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Increment
        current_url.qrclicks += 1
        current_url.save()

        self.assertEqual(current_url.qrclicks, 1)

    # socialclicks -------------------------------------------------------------

    def test_socialclicks(self):
        """
        Test that socialclicks incremention works
        """

        # Get the URL to test
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Increment
        current_url.socialclicks += 1
        current_url.save()

        self.assertEqual(current_url.socialclicks, 1)

    # expires ------------------------------------------------------------------

    def test_expires(self):
        """
        Test that the expires field functions as intended
        """
        
        tomorrow = timezone.now() + timezone.timedelta(days=1)

        # Get the URL to apply it to
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        # Apply the date
        current_url.date_created = tomorrow
        current_url.save()

        self.assertEqual(current_url.date_created, tomorrow)


    # __str__ ------------------------------------------------------------------

    def test_check_str(self):
        """
        check printing
        """

        # Get the URL to test
        get_user = User.objects.get(username='dhaynes')
        get_registered_user = RegisteredUser.objects.get(user=get_user)
        current_url = URL.objects.get(owner=get_registered_user)

        current_url.target = "https://dhaynes.xyz"
        current_url.save()

        expected = '<Owner: dhaynes - Target URL: https://dhaynes.xyz>'
        actual = str(current_url)
        self.assertEqual(expected, actual)

    # generate_valid_short -----------------------------------------------------

    # def test_generate_valid_short(self):
    #     """
    #     Test that we can generate a short url at will
    #     """

    #     # Get the URL to test
    #     get_user = User.objects.get(username='dhaynes')
    #     get_registered_user = RegisteredUser.objects.get(user=get_user)
    #     current_url = URL.objects.get(owner=get_registered_user)

    #     self.assertTrue(current_url.generate_valid_short())
