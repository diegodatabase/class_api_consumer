import requests

from .models import People

class APIConsumer:

    base_url = 'https://swapi.dev/api'

    @classmethod
    def get_people(cls, people_id: int) -> People:
        response = requests.get(f'{cls.base_url}/people/{people_id}')

        response.raise_for_status()

        data = response.json()

        return People(name=data['name'], height=data['height'])