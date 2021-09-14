from datetime import date


class Post:
    def __init__(self, postID, title, subtitle, body, datePosted):
        self.id = postID
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.date = datePosted
        self.image = "assets/img/post-bg.jpg"