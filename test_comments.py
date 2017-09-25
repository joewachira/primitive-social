import unittest

class TddInComments(unittest.TestCase):

    def setup(self):
        self.com = Comment()

    def test_comments_create_method_is_not_black(self):
        self.assertRaises(ValueError, self.com.create, '', '')

if __name__ =='__main__':
    unittest.main(test)        