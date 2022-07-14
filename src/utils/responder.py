import json

from flask import Response


class Responder:
    @staticmethod
    def send(data, status_code: int):
        if data is None:
            data = {}

        return Response(
            json.dumps(data, default=str),
            mimetype="application/json",
            status=status_code,
        )
