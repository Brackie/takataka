from flask import Blueprint, request, make_response, current_app
from . import db, helper
import jwt
from datetime import datetime, timedelta


bp = Blueprint('orders', __name__, url_prefix='/orders')


@bp.route('upload', methods=['POST'])
def upload_order():	
    token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
    if not token:
        return make_response({'status': 0, 'message': 'Please login first!'}, 401)

    if request.content_type != 'application/json':
        return make_response({'status': 0, 'message': 'Bad Request'}, 400)

    form_data = request.get_json()

    query = '''INSERT INTO `orders` (user_id, number, description, credit, debit, balance) 
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')'''.format(token['sub'], form_data['number'], 
        form_data['description'], form_data['credit'], form_data['debit'], form_data['balance'])

    conn = db.get_db()
    cur = conn.cursor()
    result = cur.execute(query)
    conn.commit()

    if result < 1:
        return make_response({'status': 0, 'message': "Server Error. Couldn't save order"}, 500)

    return make_response({'status': 1, 'message': 'Order Registered'}, 200)		


@bp.route('all', methods=['GET'])
def get_orders():
    token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
    if not token:
        return make_response({'status': 0, 'message': 'Must be logged in to complete this request'}, 401)

    conn = db.get_db()
    cur = conn.cursor()
    query = '''SELECT id, number, description, credit, debit, balance FROM `orders` ORDER BY id DESC'''
    cur.execute(query)
    conn.commit()
    result = cur.fetchall()

    if not result:
        return make_response({'status': 0, 'message': 'No orders found'}, 404)

    return make_response({'status': 1, 'message': 'Request successful', 'data': result}, 200)


@bp.route('view/<id>', methods=['GET'])
def view_order(id):
    token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
    if not token:
        return make_response({'status': 0, 'message': 'Must be logged in to complete this request'}, 401)

    conn = db.get_db()
    cur = conn.cursor()
    query = '''SELECT  id,number, description, credit, debit ordered_at FROM `orders` WHERE id = '{}' ORDER BY ordered_at DESC LIMIT 1'''.format(id)
    cur.execute(query)
    conn.commit()
    result = cur.fetchone()
    if not result:
        return make_response({'status': 0, 'message': 'Order not found'}, 404)
    return make_response({'status': 1, 'message': 'Request successful', 'data': result}, 200)


# @bp.route('update/<id>', methods=['PATCH'])
# def edit_order(order_id):
#     token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
#     if not token or token['typ'] != 'admin':
#         return make_response({'status': 0, 'message': 'Please login first!'}, 401)

#     form_data = request.get_json()

#     edit_query = '''UPDATE `order` SET description = '{}', order_location = '{}' WHERE order_id = UUID_TO_BIN('{}') LIMIT 1'''.format(form_data["description"], form_data["order_location"], order_id)
#     conn = db.get_db()
#     cur = conn.cursor()
#     result = cur.execute(edit_query)
#     conn.commit()

#     if result < 1:
#         return make_response({'status': 1, 'message': 'Server Error. Could not update order!'}, 500)

#     return make_response({'status': 1, 'message': 'Request Successful'}, 200)


# @bp.route('delete/<id>', methods=['DELETE'])
# def delete_order(id):
#     if request.content_type != 'application/json':
#         return make_response({'status':0, 'message': 'Invalid content type'}, 400)

#     token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
#     request_data = request.get_json()

#     if token and token['typ'] == 'admin':
#         conn = db.get_db()
#         cur = conn.cursor()
#         del_query = "DELETE FROM `order` WHERE id = '{}'".format(order_id)
#         result = cur.execute(del_query)
#         conn.commit()

#         if result > 0:
#             return make_response({'status': 1, 'message': 'Request successful'}, 200)

#         return make_response({'status': 1, 'message': 'Order not found'}, 200)

#     else:
#         return make_response({'status': 0, 'message': 'Must be logged in to complete this request'}, 401)
