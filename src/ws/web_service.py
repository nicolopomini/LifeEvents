from __future__ import absolute_import
from __future__ import annotations

from flask import Flask, request
from flask_restful import Api, Resource

from logic.manager import Manager
from tapoi.api.common import TapoiNotFoundApiException


class LifeEventDiscovery(Resource):
    def post(self):
        posted_data = request.get_json()
        try:
            instance = posted_data['instance']
            asset = posted_data['asset']
            year = posted_data['year']
            life_event = posted_data['lifeEvent']
            detections = Manager.compute_week_profiling(instance, asset, year, life_event)
            return {
                "detections": [d.to_repr() for d in detections],
                "instance": instance,
                "asset": asset,
                "year": year,
                "lifeEvent": life_event
            }, 200
        except KeyError:
            return {"message": "Error, some keys are missing"}, 400
        except TapoiNotFoundApiException:
            return {"message": "The requested instance or asset don't exist"}, 404
        except ValueError:
            return {"message": "The requested life event is not supported"}, 422


class ResourceBuilder:

    @staticmethod
    def routes():
        return [
            (LifeEventDiscovery, "/le")
        ]


class WebService:

    def __init__(self, host: str = "0.0.0.0", port: int = 8000, prefix: str="") -> None:
        self._host = host
        self._port = port
        self._prefix = prefix

        self._app = Flask("engine-ws")
        self._api = Api(app=self._app)
        for (resource, path) in ResourceBuilder.routes():
            self._api.add_resource(resource, self._prefix + path)

    def run(self):
        self._app.run(host=self._host, port=self._port)
