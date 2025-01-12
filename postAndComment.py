class Post:
    def __init__(self, post_id, title, content, email):
        """
        Initialize a new post.

        :param post_id: Unique identifier for the post.
        :param title: Title of the post.
        :param content: Content of the post.
        :param email: Author's email address.
        """
        self.id = post_id
        self.title = title
        self.content = content
        self.email = email
        self.approved = False  # Statusul de aprobare al postării
        self.comments = []  # Listă de comentarii asociate cu postarea

    def to_dict(self):
        """
        Convert the Post instance to a dictionary.

        :return: Dictionary representation of the post.
        """
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "email": self.email,
            "approved": self.approved,
            "comments": [comment.to_dict() for comment in self.comments],
        }
