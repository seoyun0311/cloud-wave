from flask import jsonify, Blueprint, request
from db_connection import get_db_connection
# from db_connection_secrest_manager import get_db_connection

add_destination_blueprint = Blueprint('add_destination', __name__)

@add_destination_blueprint.route('/attractions', methods=['POST'])
def add_destination():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    average_rating = data.get('average_rating')
    photo_url = data.get('photo_url')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO attractions (name, location, average_rating, photo_url) VALUES (%s, %s, %s, %s)',
                   (name, location, average_rating, photo_url))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Travel attraction added successfully'}), 201