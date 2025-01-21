from flask import jsonify, Blueprint, request
from db_connection import get_db_connection
# from db_connection_secrest_manager import get_db_connection

login_blueprint = Blueprint('login_destinations', __name__)
    
@login_blueprint.route('/login', methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username,password)

    # 데이터베이스 연결
    conn = get_db_connection()
    cursor = conn.cursor()

    # 안전한 사용자 인증 쿼리
    cursor.execute('SELECT * FROM users WHERE username = %s;', (username,))
    # 취약한 사용자 인증 쿼리
    # query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    # cursor.execute(query)
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    # 안전한 사용자 검증 처리
    if user and user[3] == password: 
        return jsonify(success=True)
    # 취약한 사용자 검증 처리
    # if user:
        # return jsonify(user=user, success=True)
    else:
        return jsonify(success=False), 401