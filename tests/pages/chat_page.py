from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class ChatPage(Page):
    PATH = 'support'
    MESSAGE_INPUT = '//input[@class="message_input input"]'
    MESSAGE_TEXT = '//p[@class="messgae__text"]'
    SEND_BUT = '//button[@class="neon-button send_button"]'
    START_MESSAGE = __name__

    def wait_input_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MESSAGE_INPUT).is_displayed() and
                      d.find_element_by_xpath(self.SEND_BUT).is_displayed()
        )

    def wait_messages_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MESSAGE_TEXT).is_displayed()
        )

    def send_message(self, message):
        self.input_message(message)
        self.click_send()
        self.wait_message_sent()

    def send_start_message(self):
        self.send_message(self.START_MESSAGE)

    def wait_message_sent(self, ):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEND_BUT).get_attribute('disabled') is None
        )

    def message_number(self):
        return len(self.driver.find_elements_by_xpath(self.MESSAGE_TEXT))

    def click_send(self):
        self.driver.find_element_by_xpath(self.SEND_BUT).click()

    def input_message(self, message):
        self.driver.find_element_by_xpath(self.MESSAGE_INPUT).send_keys(message)

    @property
    def last_message(self):
        messages = self.driver.find_elements_by_xpath(self.MESSAGE_TEXT)
        return messages[-1].get_attribute('innerText')
