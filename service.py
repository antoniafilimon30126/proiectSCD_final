from postAndComment import Post

class SocialMediaService:
    def __init__(self):
        self.posts = [
            Post(1, "Sample Post 1", "This is the content of post 1", "test1@example.com"),
            Post(2, "Sample Post 2", "This is the content of post 2", "test2@example.com")
        ]  # Listă de postări
        self.next_post_id = 3

    def get_posts_by_keyword(self, keyword):
        return [
            post.to_dict() for post in self.posts
            if keyword.lower() in post.title.lower() or keyword.lower() in post.content.lower()
        ]

    def approve_post(self, post_id):
        for post in self.posts:
            if post.id == post_id:
                post.approved = True
                return post.to_dict()
        return None

    def remove_post(self, post_id):
        for post in self.posts:
            if post.id == post_id:
                self.posts.remove(post)
                return True
        return False
