from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

import config
from routes.movie_routes import movies
from routes.login_routes import login

app = Flask(__name__)

brypt = Bcrypt(app)
jwt = JWTManager(app)

app.config.from_object(config.DevelopmentConfig)

app.register_blueprint(movies)
app.register_blueprint(login)

if __name__ == '__main__':
    debug = True

if debug:
    app.run(host='0.0.0.0', debug=True)
else:
    app.run(host='0.0.0.0')