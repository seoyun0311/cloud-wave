from flask import Blueprint, jsonify, request
from db_connection import get_db_connection
# from db_connection_secrest_manager import get_db_connection

update_destination_blueprint = Blueprint('update_destination', __name__)

@update_destination_blueprint.route('/attractions/<int:attraction_id>', methods=['PUT'])
def update_attraction(attraction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    update_data = request.get_json()
    name = update_data.get('name')
    location = update_data.get('location')
    average_rating = update_data.get('average_rating')
    photo_url = update_data.get('photo_url')
    attraction_id = update_data.get('attraction_id')

    # 데이터베이스 업데이트 쿼리
    cursor.execute("""UPDATE attractions 
                   SET name=%s, location=%s, average_rating=%s, photo_url=%s 
                   WHERE id=%s""", 
                   (name, location, average_rating, photo_url, attraction_id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'status': 'success'}), 200