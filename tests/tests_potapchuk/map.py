import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.map_page import MapPage
from tests.pages.restaurant_page import RestaurantPage
from tests.tests_potapchuk.utils import authenticate, set_addr


class MapTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.LOGIN = os.environ.get('LOGIN')
        self.PASSWORD = os.environ.get('PASSWORD')
        authenticate(self)
        set_addr(self)

        self.map_page = MapPage(self.driver)
        self.map_page.open()
        self.map_page.wait_map_is_visible()

    def testMapRestaurantAvailable(self):
        self.map_page.click_on_restaurant_button()
        self.map_page.wait_restaurant_div_visible()
        # self.map_page.click_restaurant_button()

        restaurant_page = RestaurantPage(self.driver)
        restaurant_page.wait_until_we_are_on_rest_page()

    def tearDown(self):
        self.driver.quit()
