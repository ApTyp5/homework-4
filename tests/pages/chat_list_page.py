from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class ChatListPage(Page):
    PATH = 'support/chats'
    CHAT_ITEM = 'div[class^="chat-item"]'
    CHAT_LIST = 'div.chat-list'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CHAT_ITEM).is_displayed()
        )

    def click_first_chat_card(self):
        items = self.driver.find_elements_by_css_selector(self.CHAT_ITEM)
        items[-1].click()
