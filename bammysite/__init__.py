from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# session key
app.secret_key = os.urandom(24)

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bammy.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# import blueprint
#from bammysite.site.views import sitemod

# register blueprint
#app.register_blueprint(site.views.sitemod)