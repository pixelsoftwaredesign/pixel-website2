from pymongo import MongoClient
from django.conf import settings

_client = None
_db = None


def get_mongo_client():
    global _client
    if _client is None:
        _client = MongoClient(settings.MONGODB_URI)
    return _client


def get_mongo_db():
    global _db
    if _db is None:
        _db = get_mongo_client()[settings.MONGODB_DB]
    return _db


def get_collection(name):
    return get_mongo_db()[name]


def store_social_post(post_data):
    col = get_collection('posts')
    result = col.insert_one(post_data)
    return str(result.inserted_id)


def get_social_posts(limit=50, skip=0):
    col = get_collection('posts')
    return list(col.find().sort('created_at', -1).skip(skip).limit(limit))


def store_chat_message(message_data):
    col = get_collection('messages')
    result = col.insert_one(message_data)
    return str(result.inserted_id)


def get_chat_messages(conv_id, limit=50):
    col = get_collection('messages')
    return list(col.find({'conversation_id': conv_id}).sort('created_at', -1).limit(limit))


def store_user_session(session_data):
    col = get_collection('user_sessions')
    col.update_one(
        {'user_id': session_data['user_id']},
        {'$set': session_data},
        upsert=True,
    )


def get_user_sessions(user_id):
    col = get_collection('user_sessions')
    return list(col.find({'user_id': user_id}))


def store_notification(notification_data):
    col = get_collection('notifications')
    result = col.insert_one(notification_data)
    return str(result.inserted_id)


def get_notifications(user_id, limit=20):
    col = get_collection('notifications')
    return list(col.find({'user_id': user_id}).sort('created_at', -1).limit(limit))


def store_media_file(media_data):
    col = get_collection('media')
    result = col.insert_one(media_data)
    return str(result.inserted_id)


def get_media_files(user_id=None, limit=50):
    col = get_collection('media')
    query = {'user_id': user_id} if user_id else {}
    return list(col.find(query).sort('created_at', -1).limit(limit))


def health_check():
    try:
        get_mongo_client().admin.command('ping')
        return True
    except Exception:
        return False
