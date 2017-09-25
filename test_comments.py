import unittest
from comments import Comment

class Test_Comment(unittest.TestCase):

    def setUp(self):
        self.com = Comment()
        

    def test_comments_create_method_commentid_is_not_integer(self):
        self.assertRaises(ValueError, self.com.create, 'one', '1', 'one', 'two')
    
    def test_comments_create_method_commentid_is_blank(self):
        self.assertRaises(ValueError, self.com.create, '', '1', 'one', 'two')

    def test_comments_create_method_user_is_blank(self):
        self.assertRaises(ValueError, self.com.create, 'one', '1', '', 'two')  
    
    def test_comments_create_method_body_is_blank(self):
        self.assertRaises(ValueError, self.com.create, 'one', '1', 'one', '')

    def test_comments_create_method_user_and_body_is_blank(self):
        self.assertRaises(ValueError, self.com.create, 'one', '1', '', '')      


if __name__ =='__main__':
    unittest.main()        