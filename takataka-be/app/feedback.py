from flask import Blueprint, request, make_response, current_app
from . import db, helper
import jwt
from datetime import datetime, timedelta


bp = Blueprint('announcements', __name__, url_prefix='/announcements')
<<<<<<< Updated upstream

=======
 
>>>>>>> Stashed changes

@bp.route('upload', methods=['POST'])
def upload_announcements():	
    if request.content_type != 'application/json':
        return make_response({'status': 0, 'time': 'Bad Request'}, 401)

    token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
    if not token or token['typ'] != 'client':
        return make_response({'status': 0, 'time': 'Please login first!'}, 401)

    form_data = request.get_json()

    conn = db.get_db()
    cur = conn.cursor()

    query = '''INSERT INTO `announcements` (id, content, time) VALUES ( '{}', '{}','{}')'''.format(token['sub'], form_data['content'], form_data['time'])
    result = cur.execute(query)
    conn.commit()

    if result < 1:
        return make_response({'status': 0, 'time': "Server Error. Couldn't save time"}, 500)

    return make_response({'status': 1, 'time': 'time Received :)'}, 200)


# @bp.route('all', methods=['GET'])
# def get_announcementss():
#     token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
#     if token:
#         conn = db.get_db()
#         cur = conn.cursor()
#         query = '''SELECT id, content, time, sent_at FROM `announcements` ORDER BY sent_at DESC'''
#         cur.execute(query)
#         conn.commit()
#         result = cur.fetchall()
#         if not result:
#             return make_response({'status': 0, 'time': 'No times found'}, 404)
#         return make_response({'status': 1, 'time': 'Request successful', 'data': result}, 200)
#     else:
#         return make_response({'status': 0, 'time': 'Must be logged in to complete this request'}, 401)


# @bp.route('view/<id>', methods=['GET'])
# def view_announcements(id):
#     token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
#     if token:
#         conn = db.get_db()
#         cur = conn.cursor()
#         query = '''SELECT id, content, time, sent_at FROM `announcements` WHERE id = '{}' ORDER BY sent_at DESC LIMIT 1'''.format(id)
#         cur.execute(query)
#         conn.commit()
#         result = cur.fetchone()
#         if not result:
#             return make_response({'status': 0, 'time': 'time not found'}, 404)
#         return make_response({'status': 1, 'time': 'Request successful', 'data': result}, 200)
#     else:
#         return make_response({'status': 0, 'time': 'Must be logged in to complete this request'}, 401)


# @bp.route('delete/<id>', methods=['DELETE'])
# def delete_announcements(id):
#     if request.content_type != 'application/json':
#         return make_response({'status':0, 'time': 'Invalid content type'}, 400)

#     token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
#     request_data = request.get_json()

#     if token and token['typ'] == 'admin':
#         conn = db.get_db()
#         cur = conn.cursor()
#         del_query = "DELETE FROM `announcements` WHERE id = ('{}')".format(id)
#         result = cur.execute(del_query)
#         conn.commit()

#         if result > 0:
#             return make_response({'status': 1, 'time': 'Request successful'}, 200)

#         return make_response({'status': 1, 'time': 'time not found'}, 200)

#     else:
#         return make_response({'status': 0, 'time': 'Must be logged in to complete this request'}, 401)
