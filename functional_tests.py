import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_that_can_start_a_todo_list(self):
        # Dave has heard about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # He notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)

        # He is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        # He types "Buy peakcock feathers" into a text box
        # (Dave's hobby is tying fly-fishing lures)

        # When he hits enter, thepage updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # He enters "Use peacock feathers to make a fly" (Dave is very methodical)

        # The page updates again, and now shows both items on his list

        # Satisfied, he goes back to sleep

if __name__ == "__main__":
    unittest.main()