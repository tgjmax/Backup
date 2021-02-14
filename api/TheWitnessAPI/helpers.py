"""
Helpers class for handling database operations.
"""
from flask import request

from main import db
from models import News, Comment, Profile, NewsLikes, CommentLikes, Reply, ReplyLikes

"""
Get profile based on email. If profile does not exist, create one and then return.
"""


def get_profile(email, name):
    db.create_all()
    profile = Profile.query.filter_by(email=email).first()
    if profile is not None:
        return profile
    else:
        return create_profile(email=email, name=name)


"""
Create a new profile for given email and name. Return the profile object.
"""


def create_profile(email, name):
    db.create_all()
    profile = Profile(name=name, email=email)
    try:
        db.session.add(profile)
        db.session.commit()
        return profile
    except:
        db.session.rollback()


"""
Get news for given id. Returns all news if no id is specified.
"""


def get_news(user_id, news_id=None):
    db.create_all()
    if news_id is None:
        return News.query.all()
    else:
        return News.query.get(news_id)


def update_likes_in_news(news_id, user_id, is_liked):
    news_likes = NewsLikes.query.filter_by(news_id=news_id, user_id=user_id).first()
    if news_likes is None:
        try:
            news_likes = NewsLikes(news_id=news_id, user_id=user_id, is_liked=bool(is_liked))
            db.session.add(news_likes)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    else:
        news_likes.is_liked = bool(is_liked)
        try:
            db.session.commit()
        except:
            db.session.rollback()


def append_is_liked_to_news(news, user_id):
    db.create_all()
    if isinstance(news, News):
        if news is not None:
            news_likes = NewsLikes.query.filter_by(news_id=news.id, user_id=user_id).first()
            if news_likes is not None:
                news.is_liked = news_likes.is_liked
            else:
                news.is_liked = False
        return news
    else:  # list of news
        if len(news) > 0:
            for current_news in news:
                news_likes = NewsLikes.query.filter_by(news_id=current_news.id, user_id=user_id).first()
                if news_likes is not None:
                    current_news.is_liked = news_likes.is_liked
            return news


"""
Get comments for given news_id, comment_id. Returns comments based on parameters availability.
"""


def get_comments(news_id=None, id=None):
    db.create_all()
    if id is None and news_id is None:
        return None
    elif news_id is not None:
        return Comment.query.filter_by(news_id=news_id).all()
    elif id is not None:
        return Comment.query.get(id)
    else:
        return Comment.query.filter_by(id=id, news_id=news_id).all()


"""
Get comments for specific user id.
"""


def get_comments_for_user(user_id):
    db.create_all()
    return Comment.query.filter_by(user_id=user_id)


"""
Get replies for given reply_id, comment_id. Returns replies based on parameters availability.
"""


def get_replies(comment_id=None, reply_id=None):
    db.create_all()
    if reply_id is None and comment_id is None:
        return None
    elif comment_id is not None:
        return Reply.query.filter_by(comment_id=comment_id).all()
    elif reply_id is not None:
        return Reply.query.get(reply_id)
    else:
        return Reply.query.filter_by(id=reply_id, comment_id=comment_id).all()


"""
Post news.
"""


def post_news(title, tags, description, flag_url, region, image, video, article_link):
    db.create_all()
    news = News(title=title, tags=tags, flag_url=flag_url, description=description, region=region,
                article_link=article_link)
    try:
        db.session.add(news)
        db.session.commit()

        from utils import upload_file
        if image is not None and image.filename != '':
            news.image_url = upload_file(news=news, file=image, upload_type='images')
        if video is not None and video.filename != '':
            news.video_url = upload_file(news=news, file=video, upload_type='videos')

        db.session.add(news)
        db.session.commit()
        return news
    except Exception as e:
        print(e)
        db.session.rollback()


"""
Post a new comment.
"""


def post_comment(news_id, user_id, name, message):
    db.create_all()
    comment = Comment(news_id=news_id, user_id=user_id, name=name, message=message)
    try:
        db.session.add(comment)
        db.session.commit()
        return comment
    except Exception as e:
        db.session.rollback()


"""
Post a new reply.
"""


def post_reply(news_id, comment_id, user_id, name, message):
    db.create_all()
    reply = Reply(news_id=news_id, comment_id=comment_id, user_id=user_id, name=name, message=message)
    try:
        db.session.add(reply)
        db.session.commit()
        return reply
    except Exception as e:
        db.session.rollback()


"""
Update likes of a specific comment.
"""


def update_comment_likes(comment_id, user_id, is_liked):
    db.create_all()
    comment_likes = CommentLikes.query.filter_by(comment_id=comment_id, user_id=user_id).first()
    try:
        if comment_likes is None:
            comment_likes = CommentLikes(comment_id=comment_id, user_id=user_id, is_liked=is_liked)
            db.session.add(comment_likes)
            db.session.commit()
        else:
            comment_likes.is_liked = bool(is_liked)
        comment = get_comments(id=comment_id)
        if int(is_liked) == 1:
            comment.likes = comment.likes + 1
        else:
            comment.likes = comment.likes - 1
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        db.session.rollback()
    return False


def update_reply_likes(reply_id, user_id, is_liked):
    db.create_all()
    reply_likes = ReplyLikes.query.filter_by(reply_id=reply_id, user_id=user_id).first()
    try:
        if reply_likes is None:
            reply_likes = ReplyLikes(reply_id=reply_id, user_id=user_id, is_liked=is_liked)
            db.session.add(reply_likes)
            db.session.commit()
        else:
            reply_likes.is_liked = bool(is_liked)
        reply = get_replies(reply_id=reply_id)
        if is_liked == 1:
            reply.likes = reply.likes + 1
        else:
            reply.likes = reply.likes - 1
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
    return False


"""
Update likes of a specific news.
"""


def update_news_likes(news_id, is_liked, user_id):
    db.create_all()
    news = get_news(news_id=news_id, user_id=user_id)
    update_likes_in_news(news_id=news_id, user_id=user_id, is_liked=is_liked)
    try:
        if is_liked == 1:
            news.likes_count = news.likes_count + 1
        else:
            news.likes_count = news.likes_count - 1
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
    return False


"""
Given a key, return the form data.
"""


def retrieve_post_param_value(key):
    return request.form.get(key)


"""
Given a key, return the query param value.
"""


def retrieve_get_param_value(key):
    return request.args.get(key)


"""
Given a key, return file uploaded.
"""


def retrieve_file_content(key):
    try:
        return request.files[key]
    except Exception as e:
        print(e)
