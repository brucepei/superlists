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
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Alice heard that there is a cool web app used to to-do list
        #she go to the home page
        self.browser.get('http://127.0.0.1:8000')
        
        #she found the title contains 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #she found the inputbox which require her to input a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #she input a to-do item
        inputbox.send_keys('Buy peacock feathers')
        #she input Enter, then the app prompts her to add a new one
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(3)
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        

        inputbox = self.browser.find_element_by_id('id_new_item')
        #she add another item
        inputbox.send_keys('Buy another peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(3)
        #she found the 2 items are in the to-do list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Buy another peacock feathers')
    
        
        #she click the list botton, and the app return the to-do items as a list
        time.sleep(3)
        self.fail("Test paused!")
        
if __name__ == '__main__':
    unittest.main()