from flask import Blueprint, request, make_response, current_app
from . import db, helper
import jwt
from datetime import datetime, timedelta


bp = Blueprint('product', __name__, url_prefix='/product')


# @bp.route('upload', methods=['POST'])
# def upload_product():	
# 	if request.content_type != 'application/json':
# 		return make_response({'status': 0, 'message': 'Bad Request'}, 401)

# 	token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
# 	if not token or token['typ'] != 'admin':
# 		return make_response({'status': 0, 'message': 'Please login first!'}, 401)

# 	# form_data = request.get_json()
# 	# if helper.product_exists(sno=form_data['']):
# 	# 	return make_response({'status': 0, 'message': 'The product exists!'}, 409)

# 	query = '''INSERT INTO product (id , name, category,price, quantity description) VALUES (, '{}', '{}', '{}', '{}',"{}")'''.format(form_data[''], form_data['name'], form_data['category'], form_data['description'])

# 	conn = db.get_db()
# 	cur = conn.cursor()
# 	result = cur.execute(query)
# 	conn.commit()

# 	if result < 1:
# 		return make_response({'status': 0, 'message': "Server Error. Couldn't save product"}, 500)
	
# 	return make_response({'status': 1, 'message': 'product Registered'}, 200)		


@bp.route('all', methods=['GET'])
def get_products():
    conn = db.get_db()
    cur = conn.cursor()
    query = '''SELECT id, name, category, price, quantity, description FROM product ORDER BY id DESC'''
    cur.execute(query)
    conn.commit()
    result = cur.fetchall()
    if not result:
        return make_response({'status': 0, 'message': 'No products found'}, 404)
    return make_response({'status': 1, 'message': 'Request successful', 'data': result}, 200)


@bp.route('view/<id>', methods=['GET'])
def view_product(id):
    token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
    if token:
        conn = db.get_db()
        cur = conn.cursor()
        query = '''SELECT  id,  name, category, description, uploaded_at FROM product WHERE id = ('{}')'''.format(id)
        cur.execute(query)
        conn.commit()
        result = cur.fetchone()
        if not result:
            return make_response({'status': 0, 'message': 'Product not found'}, 404)
        return make_response({'status': 1, 'message': 'Request successful', 'data': result}, 200)
    else:
        return make_response({'status': 0, 'message': 'Must be logged in to complete this request'}, 401)


# # @bp.route('update/<id>', methods=['PATCH'])
# # def edit_product(id):
# #     token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
# #     if not token or token['typ'] != 'admin':
# #         return make_response({'status': 0, 'message': 'Please login first!'}, 401)

# #     form_data = request.get_json()

# #     edit_query = '''UPDATE product SET  = '{}', name = '{}', category = '{}', description = '{}' WHERE id=UUID_TO_BIN('{}') LIMIT 1'''.format(form_data[""], form_data["name"], form_data["category"], form_data["description"], id)
# #     conn = db.get_db()
# #     cur = conn.cursor()
# #     result = cur.execute(edit_query)
# #     conn.commit()

# #     if result < 1:
# #         return make_response({'status': 1, 'message': 'Server Error. Could not update product!'}, 500)

# #     return make_response({'status': 1, 'message': 'Request Successful'}, 200)


# @bp.route('delete/<id>', methods=['DELETE'])
# def delete_product(id):
#     if request.content_type != 'application/json':
#         return make_response({'status':0, 'message': 'Invalid content type'}, 400)

#     token = helper.is_logged_in(request.headers['Authorization'].split(' ')[-1], current_app.config['SCRT'])
#     request_data = request.get_json()

#     if token and token['typ'] == 'admin':
#         conn = db.get_db()
#         cur = conn.cursor()
#         del_query = "DELETE FROM product WHERE id = ('{}')".format(id)
#         result = cur.execute(del_query)
#         conn.commit()

#         if result > 0:
#             return make_response({'status': 1, 'message': 'Request successful'}, 200)

#         return make_response({'status': 1, 'message': 'Product not found'}, 200)

#     else:
#         return make_response({'status': 0, 'message': 'Must be logged in to complete this request'}, 401)
