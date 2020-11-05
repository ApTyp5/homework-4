import re

from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class RestaurantPage(Page):
    BASE_PATH = 'restaurants'

    def wait_until_we_are_on_rest_page(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: re.search(r'%s%s*' % (self.BASE_URL, self.BASE_PATH), d.current_url) is not None
        )