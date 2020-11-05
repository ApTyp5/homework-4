import os
import unittest

from tests.helpers.database import DatabaseFiller
from tests.pages.chat_list_page import ChatListPage
from tests.pages.chat_page import ChatPage
from selenium.webdriver import DesiredCapabilities, Remote
from tests.tests_potapchuk.utils import authenticate, re_authenticate


class ChatListTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.user_id, self.sent_message = self.createChatWithUserMessage()

        self.LOGIN = os.environ.get('SUP_LOGIN')
        self.PASSWORD = os.environ.get('SUP_PASSWORD')
        re_authenticate(self)

        self.chat_list_page = ChatListPage(self.driver)
        self.chat_list_page.open()
        self.chat_list_page.wait_visible()

    def tearDown(self):
        self.driver.quit()

    def testRecvUserMessage(self):
        self.chat_list_page.click_user_chat_card(self.user_id)
        chat_page = ChatPage(self.driver)
        chat_page.wait_messages_visible()
        self.assertEqual(chat_page.last_message, self.sent_message)

    def createChatWithUserMessage(self):
        self.LOGIN = os.environ.get('LOGIN')
        self.PASSWORD = os.environ.get('PASSWORD')
        authenticate(self)
        chat = ChatPage(self.driver)
        chat.open()
        chat.wait_input_visible()
        chat.send_start_message()
        self.sent_message = chat.START_MESSAGE

        filler = DatabaseFiller()
        filler.user_auth()
        user_id = filler.get_profile_id()
        return user_id, chat.START_MESSAGE
