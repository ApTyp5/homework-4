from tests.pages.auth_page import AuthPage
from tests.pages.profile_page import ProfilePage


def authenticate(test_suite):
    auth_page = AuthPage(test_suite.driver)
    auth_page.open()
    auth_page.wait_open()
    auth_page.auth(test_suite.LOGIN, test_suite.PASSWORD)


def re_authenticate(test_suite):
    prof_page = ProfilePage(test_suite.driver)
    prof_page.open()
    prof_page.wait_open()
    prof_page.profile_form.logout()
    authenticate(test_suite)
