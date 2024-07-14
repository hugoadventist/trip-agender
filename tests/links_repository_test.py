from app.src.models.settings.db_connection_handler import db_connection_handler
import uuid
from app.src.models.repositories.links_repository import (
    LinksRepository,
)


db_connection_handler.connect()

trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())


def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_trips_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "https://airbnb.com",
        "title": "Hospedagem Gramado",
    }

    links_repository.registry_link(links_trips_infos)


def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links = links_repository.find_links_from_trip(trip_id)

    print(links)

    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
