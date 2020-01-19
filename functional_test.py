from selenium import webdriver
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
		self.fail('Finish The Test!')

		# She is invited to enter a to-do item straight away

		# She types "Buy Peacock feathers" into the textbox

		# When she hits enter the page updates, and now the page lists:
		# "1. Buy Peacock feathers" as an item in to-do list.

		# There is still a button to add more To-Do's so she enters:
		# "Use peacock feathers to make a fly".

		# Page updates again and lists her new item.

		# Edith wonders if site will save her list over sessions
		# she see's text explaining this on page.

		# She revisits url, her list is restored.

		# Happy, she closes the site and goes back to her life.
if __name__ == '__main__':
	unittest.main(warnings='ignore')
	