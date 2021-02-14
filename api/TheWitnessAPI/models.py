from main import db
from utils import get_formatted_time


# Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}


# NewsLikes model
class NewsLikes(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('profile.id'))
    is_liked = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {'id': self.id, 'news_id': self.news_id, 'user_id': self.user_id, 'is_liked': self.is_liked}


# ReplyLikes model
class ReplyLikes(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    reply_id = db.Column(db.Integer, db.ForeignKey('reply.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('profile.id'))
    is_liked = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {'id': self.id, 'reply_id': self.reply_id, 'user_id': self.user_id, 'is_liked': self.is_liked}


# CommentLikes model
class CommentLikes(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('profile.id'))
    is_liked = db.Column(db.Boolean, nullable=False, default=False)


# News model
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    region = db.Column(db.String(100))
    image_url = db.Column(db.String(200))
    video_url = db.Column(db.String(200))
    flag_url = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.String(30), default=get_formatted_time())
    comments_count = db.Column(db.Integer, default=0)
    likes_count = db.Column(db.Integer, default=0)
    tags = db.Column(db.Text, nullable=False)
    article_link = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='news')
    is_liked = db.relationship('NewsLikes', backref='news')

    def to_dict(self, user_id=None):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'region': self.region,
                'image_url': self.image_url,
                'video_url': self.video_url, 'flag_url': self.flag_url,
                'timestamp': self.timestamp, 'comments_count': self.comments_count,
                'likes_count': self.likes_count, 'tags': self.tags.split(','),
                'comments': self.list_of_dict(self.comments, user_id=user_id),
                'is_liked': self.get_is_liked(is_liked=self.is_liked, user_id=user_id, news_id=self.id),
                'article_link': self.article_link}

    @staticmethod
    def list_of_dict(news):
        return [current_news.to_dict() for current_news in news]

    def list_of_dict(self, comments, user_id):
        return [comment.to_dict(user_id=user_id) for comment in comments]

    def get_is_liked(self, is_liked, user_id, news_id):
        if user_id == None:
            return False
        for liked in is_liked:
            if liked.user_id == int(user_id) and liked.news_id == news_id:
                return liked.is_liked
        return False


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    name = db.Column(db.String(75))
    message = db.Column(db.Text)
    timestamp = db.Column(db.String(30), default=get_formatted_time())
    likes = db.Column(db.Integer, default=0)
    is_liked = db.relationship('ReplyLikes', backref='reply')

    def to_dict(self, user_id):
        return {'id': self.id, 'news_id': self.news_id, 'user_id': self.user_id, 'comment_id': self.comment_id,
                'name': self.name,
                'message': self.message, 'timestamp': self.timestamp,
                'likes': self.likes,
                'is_liked': self.get_is_liked(is_liked=self.is_liked, reply_id=self.id, user_id=user_id)}

    def get_is_liked(self, is_liked, reply_id, user_id):
        for liked in is_liked:
            if liked.user_id == int(user_id) and liked.reply_id == reply_id:
                return liked.is_liked
        return False


# Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    reply_id = db.Column(db.Integer, db.ForeignKey('reply.id'))
    name = db.Column(db.String(75))
    message = db.Column(db.Text)
    timestamp = db.Column(db.String(30), default=get_formatted_time())
    likes = db.Column(db.Integer, default=0)
    replies = db.relationship('Reply', backref=db.backref('comment'), primaryjoin="Comment.id==Reply.comment_id")
    is_liked = db.relationship('CommentLikes', backref='comment')

    def to_dict(self, user_id):
        return {'id': self.id, 'news_id': self.news_id, 'user_id': self.user_id, 'name': self.name,
                'message': self.message, 'timestamp': self.timestamp,
                'likes': self.likes, 'replies': self.list_of_dict(self.replies, user_id=user_id),
                'is_liked': self.get_is_liked(is_liked=self.is_liked, user_id=user_id, comment_id=self.id)}

    def get_is_liked(self, is_liked, user_id, comment_id):
        for liked in is_liked:
            if liked.user_id == int(user_id) and liked.comment_id == comment_id:
                return liked.is_liked
        return False

    def list_of_dict(self, comments):
        return [comment.to_dict() for comment in comments]

    def list_of_dict(self, replies, user_id):
        return [reply.to_dict(user_id=user_id) for reply in replies]
