from flask import Flask
from app.src.main.routes.trips_routes import trips_routes_bp

application = Flask(__name__)
application.register_blueprint(trips_routes_bp)
