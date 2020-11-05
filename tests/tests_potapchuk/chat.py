import os
import unittest
from tests.pages.chat_page import ChatPage
from selenium.webdriver import DesiredCapabilities, Remote
from tests.tests_potapchuk.utils import authenticate


class ChatTest(unittest.TestCase):
    def setUp(self):
        self.LOGIN = os.environ.get('LOGIN')
        self.PASSWORD = os.environ.get('PASSWORD')

        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        authenticate(self)

        self.page = ChatPage(self.driver)
        self.page.open()
        self.page.wait_input_visible()
        # guarantee the positive number of messages
        self.page.send_start_message()

    def test_send_message(self):
        message = self.test_send_message.__name__
        self.page.send_message(message)
        self.assertEqual(self.page.last_message, message)

    def test_send_empty_message(self):
        self.page.send_message('')
        self.assertEqual(self.page.last_message, self.page.START_MESSAGE)

    def test_long_message(self):
        message = self.test_long_message.__name__
        long_message = 10 * message

        self.page.send_message(long_message)
        self.assertEqual(self.page.last_message, long_message)

    def tearDown(self):
        self.driver.quit()