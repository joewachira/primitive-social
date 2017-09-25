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
        if not isinstance(commentId, int):  # check if commentId is an integer
            raise ValueError("Expected value of %(xtype)s" % dict(xtype=type(int)))

        if not isinstance(postId, int):  # check if postId is an integer
            raise ValueError("Expected value of %(xtype)s" % dict(xtype=type(int)))

        if not isinstance(user, str):  # check if user is str
            raise ValueError("Expected argument of %(xtype)s" % dict(xtype=type(str)))

        if not isinstance(body, str):  # check if body is str
            raise ValueError("Expected argument of %(xtype)s" % dict(xtype=type(str)))

        self.commentId = commentId
        self.postId = postId
        self.user = user
        self.body = body
        return True
