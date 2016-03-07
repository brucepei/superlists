from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, item):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(item, [row.text for row in rows])
    
    def test_can_support_multiple_apps(self):
        #she go to the lists home page
        self.browser.get('http://127.0.0.1:8000')
        
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #she go to the study home page
        self.browser.get('http://127.0.0.1:8000/study')
        
        self.assertIn('Study Django', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Study Django', header_text)
        
        #she click the list botton, and the app return the to-do items as a list
        time.sleep(3)
        self.fail("Test paused!")
        
if __name__ == '__main__':
    unittest.main()