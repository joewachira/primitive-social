class Comment(object):
    """ comment class to store comments """
    def __init__(self):
        # make all attributes to None because create method will handle validation
        self.commentId = None
        self.postId = None
        self.user = None
        self.body = None

    def create(self, commentId, postId, user, body):

        """
        A function to create comment, returns True if successful
        """
        if not isinstance((commentId, postId), int):
            raise ValueError("Expected value of %(xtype)s" % dict(xtype=type(int)))

        if not isinstance((user, body), str):
            raise ValueError("Expected argument of %(xtype)s" % dict(xtype=type(str)))

        self.commentId = commentId
        self.postId = postId
        self.user = user
        self.body = body
        return True







