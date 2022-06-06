from flask import Flask
import models
from routes import user_blueprint
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Wkpbn45t7Q-oaLlhskZrCg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
models.init_app(app)
app.register_blueprint(user_blueprint)
migrate = Migrate(app, models.db)


if __name__ == "__main__":
    app.run(debug=True)
