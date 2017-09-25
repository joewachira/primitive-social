import sys
import unittest
from primefeed_post import PrimeFeedPost


class TestPost(unittest.TestCase):
    """
    Perform unit testing for the User class
    """
def setUp(self):
    """"""
    self.newPost = PrimeFeedPost()


def test_empty_post(self):
    """defining method to test for creating an empty post"""
    output=self.newPost.add_post_feed('' ,'')
    self.assertRaises(ValueError, output, "cant create empty post")    
     
def test_post_null_title(self):
    """defining method to test for creating post with an empty name title"""
    output=self.newPost.add_post_feed('' ,'This is the body')
    self.assertRaises(ValueError, output, "Please provide the post title")

def test_post_null_body(self):
    """defining method to test for creating post with an empty name title"""
    output=self.newPost.add_post_feed('title' ,'')
    self.assertRaises(ValueError, output, "Please provide the post content")

if __name__ =='main':
    unittest.main()