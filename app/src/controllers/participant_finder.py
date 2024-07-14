class ParticipantFinder:
    def __init__(self, participant_repository) -> None:
        self.__participants_repository = participant_repository

    def find_participants_from_trip(self, trip_id: str):
        try:
            participants = self.__participants_repository.find_participants_from_trips(
                trip_id
            )

            formatted_participants_infos = []
            for participant in participants:
                formatted_participants_infos.append(
                    {
                        "id": participant[0],
                        "name": participant[1],
                        "is_confirmed": participant[2],
                        "email": participant[3],
                    }
                )

            return {
                "body": {"participants": formatted_participants_infos},
                "status_code": 200,
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
