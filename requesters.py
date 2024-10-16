import exceptions
import requests
import models


class MatchRequester:
    """Requester class to the `bn-hiring-challenge` domain"""
    
    path: str
    model_class: models.Model

    def to_models(self) -> list[models.Model]:
        try:
            return [self.model_class(**obj) for obj in self.make_request()]
        except TypeError as e:
            raise exceptions.MatchException from e

    def make_request(self) -> list[dict]:
        return self.make_get_request(self.path)

    def make_get_request(self, path: str) -> list[dict]:
        """For a given request path, return the JSON body"""

        url = f"https://bn-hiring-challenge.fly.dev/{path}.json"

        response = requests.get(url)

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise exceptions.MatchException from e

        body = response.json()

        return body


class MembersRequester(MatchRequester):
    path = "members"
    model_class = models.Member


class JobsRequester(MatchRequester):
    path = "jobs"
    model_class = models.Job
