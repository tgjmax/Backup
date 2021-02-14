from flask import Blueprint, jsonify

news_bp = Blueprint('news_bp', __name__)

"""
Route to GET profile
"""


@news_bp.route('/profile')
def get_profile():
    from helpers import get_profile, retrieve_get_param_value
    email = retrieve_get_param_value('email')
    name = retrieve_get_param_value('name')
    profile = get_profile(email=email, name=name)
    if profile is None:
        return '', 500
    else:
        return jsonify(profile.to_dict())


@news_bp.route('/news/')
def get_news():
    from helpers import get_news, retrieve_get_param_value
    user_id = retrieve_get_param_value('user_id')
    news = get_news(user_id=user_id)
    if news is None:
        return '', 404
    else:
        return jsonify([current_news.to_dict(user_id=user_id) for current_news in news])


""" 
Route to GET/POST news.
"""


@news_bp.route('/news/<int:news_id>')
def news(news_id):
    from helpers import get_news, retrieve_get_param_value
    user_id = retrieve_get_param_value('user_id')
    news = get_news(news_id=news_id, user_id=user_id)
    if news is None:
        return '', 404
    else:
        return jsonify(news.to_dict(user_id=user_id))


@news_bp.route('/publish/news', methods=['POST'])
def post_news():
    from helpers import post_news
    from helpers import retrieve_post_param_value, retrieve_file_content
    from utils import get_flag_url

    title = retrieve_post_param_value('title')
    description = retrieve_post_param_value('description')
    region = retrieve_post_param_value('region')
    flag_url = get_flag_url(region=region)
    image = retrieve_file_content('image')
    video = retrieve_file_content('video')
    tags = retrieve_post_param_value('tags')
    article_link = retrieve_post_param_value('article_link')
    news = post_news(title=title, tags=tags, flag_url=flag_url, description=description, region=region, image=image,
                     video=video, article_link=article_link)
    if news is not None:
        return jsonify(news.to_dict()), 201
    else:
        return '', 403


"""
Route to update likes for given news id.
"""


@news_bp.route('/news/update/likes', methods=['PUT'])
def update_likes_of_news():
    from helpers import retrieve_post_param_value
    news_id = retrieve_post_param_value('news_id')
    user_id = retrieve_post_param_value('user_id')
    is_liked = int(retrieve_post_param_value('is_liked'))
    from helpers import update_news_likes
    is_updated = update_news_likes(news_id=news_id, user_id=user_id, is_liked=is_liked)
    if is_updated:
        return '', 204
    else:
        return '', 403


"""
Route to get all comments irrespective of news.
Will be nuked if not necessary.
"""


@news_bp.route('/comments')
def comment():
    from helpers import get_comments
    comments = get_comments()
    if comments is None:
        return '', 404
    else:
        return jsonify([comment.to_dict() for comment in comments])


"""
Route to create/reply a comment. It's a new comment if parent_id is None, Reply otherwise.
"""


@news_bp.route('/comment/new', methods=['POST'])
def new_comment():
    from helpers import retrieve_post_param_value
    news_id = retrieve_post_param_value('news_id')
    user_id = retrieve_post_param_value('user_id')
    name = retrieve_post_param_value('name')
    message = retrieve_post_param_value('message')

    from helpers import post_comment
    comment = post_comment(news_id=news_id, user_id=user_id, name=name, message=message)
    if comment is not None:
        return jsonify(comment.to_dict(user_id=user_id)), 201
    else:
        return '', 403


"""
Route to update likes of a specific comment/reply.
"""


@news_bp.route('/comment/update/likes', methods=['PUT'])
def update_comment():
    from helpers import retrieve_post_param_value, update_comment_likes
    comment_id = retrieve_post_param_value('comment_id')
    user_id = retrieve_post_param_value('user_id')
    is_liked = int(retrieve_post_param_value('is_liked'))
    is_updated = update_comment_likes(comment_id=comment_id, is_liked=is_liked, user_id=user_id)
    if is_updated:
        return '', 204
    else:
        return '', 403


@news_bp.route('/reply/new', methods=['POST'])
def new_reply():
    from helpers import retrieve_post_param_value
    news_id = retrieve_post_param_value('news_id')
    comment_id = retrieve_post_param_value('comment_id')
    user_id = retrieve_post_param_value('user_id')
    name = retrieve_post_param_value('name')
    message = retrieve_post_param_value('message')

    from helpers import post_reply
    comment = post_reply(news_id=news_id, comment_id=comment_id, user_id=user_id, name=name, message=message)
    if comment is not None:
        return jsonify(comment.to_dict(user_id=user_id)), 201
    else:
        return '', 403


"""
Route to update likes of a specific comment/reply.
"""


@news_bp.route('/reply/update/likes', methods=['PUT'])
def update_reply():
    from helpers import retrieve_post_param_value
    reply_id = retrieve_post_param_value('reply_id')
    user_id = retrieve_post_param_value('user_id')
    is_liked = int(retrieve_post_param_value('is_liked'))
    from helpers import update_reply_likes
    is_updated = update_reply_likes(reply_id=reply_id, is_liked=is_liked, user_id=user_id)
    if is_updated:
        return '', 204
    else:
        return '', 403


"""
Route to get comments for a specific news.
"""


@news_bp.route('/comments/<int:news_id>')
def comment_by_news_id(news_id):
    from helpers import get_comments, retrieve_get_param_value
    user_id = retrieve_get_param_value('user_id')
    comments = get_comments(news_id=news_id)
    if comments is None or len(comments) == 0:
        return '', 404
    else:
        return jsonify([comment.to_dict(user_id=user_id) for comment in comments])


"""
Route to get a specific comment given it's id.
"""


@news_bp.route('/comment/<int:id>')
def comment_by_id(id):
    from helpers import get_comments
    comment = get_comments(id=id)
    if comment is None:
        return '', 404
    else:
        return jsonify(comment.to_dict())


@news_bp.route('/comments/')
def comments_for_user():
    from helpers import retrieve_get_param_value, get_comments_for_user
    user_id = retrieve_get_param_value('user_id')
    comments = get_comments_for_user(user_id=user_id)
    if comments is None or len(comments) < 1:
        return '', 404
    else:
        return jsonify([comment.to_dict() for comment in comments])
