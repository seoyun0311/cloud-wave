# import redis
from flask import *

from login_connection import login_blueprint
from get_destination import get_destinations_blueprint
# from get_destination_redis import get_destinations_redis_blueprint
from add_destination import add_destination_blueprint
from delete_destination import delete_destination_blueprint
from update_destination import update_destination_blueprint


app = Flask(__name__)
# app.secret_key = 'cloudwave'

# app.config['REDIS'] = redis.StrictRedis(
#     host='localhost',
#     port=6379,
#     db=0,
#     password='qwer1234',
#     decode_responses=True)

app.register_blueprint(login_blueprint)
app.register_blueprint(get_destinations_blueprint)
# app.register_blueprint(get_destinations_redis_blueprint)
app.register_blueprint(add_destination_blueprint)
app.register_blueprint(delete_destination_blueprint)
app.register_blueprint(update_destination_blueprint)

if __name__ == '__main__':
    app.run(debug=True)