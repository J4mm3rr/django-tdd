from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith hears about new fancy to-do list app and heads to the website
		self.browser.get('http://localhost:8000')

		# She sees the title and notices it mentions To-Do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do item straight away
		inputbox =self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a to-do item')

		# She types "Buy Peacock feathers" into the textbox
		inputbox.send_keys('Buy peacock feathers')

		# When she hits enter the page updates, and now the page lists:
		# "1. Buy Peacock feathers" as an item in to-do list.
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table =  self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peackock feathers' for row in rows)
		)

		# There is still a button to add more To-Do's so she enters:
		# "Use peacock feathers to make a fly".
		self.fail('Finish Test!')

		# Page updates again and lists her new item.

		# Edith wonders if site will save her list over sessions
		# she see's text explaining this on page.

		# She revisits url, her list is restored.

		# Happy, she closes the site and goes back to her life.
if __name__ == '__main__':
	unittest.main(warnings='ignore')
	