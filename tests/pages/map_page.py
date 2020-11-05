import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class MapPage(Page):
    PATH = 'map'
    REST_MARK = 'main div ymaps ymaps ymaps[class="ymaps-2-1-77-events-pane ymaps-2-1-77-user-selection-none"]'
    POINTER_REST_MARK = 'ymaps[class="ymaps-2-1-77-events-pane ymaps-2-1-77-user-selection-none", style*="cursor: ' \
                        'pointer"] '
    BODY = 'body'
    MAP_VIEW = 'ymaps[class="ymaps-2-1-77-map"]'
    REST_BUT = 'button[class^="neon-button"]'
    BUT_CONTAINER = 'ymaps[class="ymaps-2-1-77-balloon-content__footer"]'

    def wait_map_is_visible(self):
        return WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.REST_MARK).is_displayed()
        )

    def click_on_restaurant_button(self):
        map_view = self.driver.find_element_by_css_selector(self.MAP_VIEW)
        act = ActionChains(self.driver)
        act.move_to_element(self.driver.find_element_by_css_selector(self.BODY)).move_by_offset(
            map_view.size['width']/2,
            map_view.size['height']/2,
        ).click().perform()

    def wait_restaurant_div_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BUT_CONTAINER).is_displayed()
        )

    def click_restaurant_button(self):
        self.driver.find_element_by_css_selector(self.REST_MARK).click()
