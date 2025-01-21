import json
from flask import jsonify, Blueprint, current_app
from db_connection import get_db_connection
# from db_connection_secrest_manager import get_db_connection

get_destinations_redis_blueprint = Blueprint('get_destinations_redis', __name__)

@get_destinations_redis_blueprint.route('/attractions_redis', methods=['GET'])
def get_destinations():
    redis_client = current_app.config['REDIS']
    destinations = redis_client.get("table:attractions")

    if destinations is None:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM attractions;')
        destinations = cursor.fetchall()
        cursor.close()
        conn.close()

        destination_json = convert_to_json(destinations)

        redis_client.set("table:attractions", json.dumps(destination_json), ex=3600)
        
        return jsonify(destination_json)
    return destinations

def convert_to_json(destinations):
    destinations_list = []
    for dest in destinations:
        destinations_list.append({
            'id': dest[0], 
            'name': dest[1], 
            'location': dest[2], 
            'average_rating': str(dest[3]),
            'photo_url': dest[4]
        })
    return destinations_list