from flask import jsonify, Blueprint
from db_connection import get_db_connection
# from db_connection_secrest_manager import get_db_connection

get_destinations_blueprint = Blueprint('get_destinations', __name__)

@get_destinations_blueprint.route('/attractions', methods=['GET'])
def get_destinations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM attractions;')
    destinations = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # JSON 형태로 변환
    destinations_list = []
    for dest in destinations:
        destinations_list.append({
            'id': dest[0], 
            'name': dest[1], 
            'location': dest[2], 
            'average_rating': str(dest[3]),
            'photo_url': dest[4]
        })
    return jsonify(destinations_list)