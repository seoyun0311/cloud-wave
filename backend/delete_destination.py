from flask import jsonify, Blueprint
from db_connection import get_db_connection
# from db_connection_secrest_manager import get_db_connection

delete_destination_blueprint = Blueprint('delete_destination', __name__)

@delete_destination_blueprint.route('/attractions/<int:attraction_id>', methods=['DELETE'])
def delete_attraction(attraction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM attractions WHERE id = %s', (attraction_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Travel attraction deleted successfully'}), 200