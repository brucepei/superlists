from selenium import webdriver
import time
import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Alice heard that there is a cool web app used to to-do list
        #she go to the home page
        self.browser.get('http://127.0.0.1:8000')
        time.sleep(1)
        #she found the title contains 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        
        
        #she click the botton to add a to-do item
        
        #she click the finished button, and the app prompts her to add a new one
        
        #she add another item
        
        #she found a link which linked to to-do list
        
        #she click the list botton, and the app return the to-do items as a list

        self.fail("Test paused!")
        
if __name__ == '__main__':
    unittest.main()