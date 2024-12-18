# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import get_config


app = Flask(__name__)
app.config.from_object(get_config())
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
