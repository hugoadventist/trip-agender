"""Module providing a server."""

from app.src.main.server.server import application
from app.src.models.settings.db_connection_handler import db_connection_handler

if __name__ == "__main__":
    db_connection_handler.connect()
    application.run(host="0.0.0.0", port=3000, debug=True)
