from sqlite3 import Connection
from typing import Dict, List, Tuple


class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participants(self, participants_info: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                       INSERT INTO participants 
                            (id, id_trip, emails_to_invite_id, name)
                       VALUES 
                            (?, ?, ?, ?, ?)
                       """,
            (
                participants_info["id"],
                participants_info["id_trip"],
                participants_info["emails_to_invite_id"],
                participants_info["name"],
            ),
        )
        self.__conn.commit()

    def find_participants_from_trips(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT p.id, p.name, p.is_confirmed, e.email
            FROM participants AS p
            JOIN emails_to_invite AS e ON e.id = p.emails_to_invite_id
            WHERE p. trip_id = ?
            """,
            (trip_id,),
        )
        participants = cursor.fetchall()
        return participants

    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            UPDATE participants
            SET is_confirmed = 1
            WHERE id = ?
        """,
            (participant_id,),
        )
        self.__conn.commit()
