from flask import session, request, Blueprint, jsonify, Flask
import redis
from datetime import timedelta
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'cloudwave_test'

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)
app.config['REDIS'] = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    password='qwer1234',
    decode_responses=True)
server_session = Session(app)

@app.route('/session', methods = ['GET','POST'])
def login_session():
    if request.method == 'GET':
        username = session['username']
        gender = session['gender']
        age = session['age']
        return jsonify({'username':username,'gender':gender,'age':age})

    else:
        print(request)
        session['username'] = request.form.get('username')
        print(request.form.get('username'))
        session['gender'] = request.form.get('gender')
        print(request.form.get('gender'))
        session['age'] = request.form.get('age')
        print(request.form.get('age'))
        return jsonify({'upload':'success','username':session['username']})
    
if __name__ == '__main__':
    app.run(debug=True)