from typing import Any
from marshmallow import ValidationError
from flask import Flask, request, Response
from models import Request
from builder import response_builder


def create_app() -> Flask:
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/perform_query', methods=["POST"])
def perform_query() -> Response | Any:
    pop: Any = request.json
    try:
        params = Request().load(pop)
    except ValidationError as e:
        return e.messages, 400
    res = response_builder(
        path=params['filename'],
        cmd1=params['cmd1'],
        param1=params['value1'],
        cmd2=params['cmd2'],
        param2=params['value2']
    )
    return res, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=10000)
