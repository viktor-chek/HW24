from flask import Flask, request

from models import Request
from builder import response_builder

from typing import Any
from marshmallow import ValidationError


def create_app() -> Flask:
    application = Flask(__name__)
    return application


app = create_app()


@app.route('/perform_query', methods=["POST"])
def perform_query() -> list[str] | tuple[Any, int]:
    pop: Any = request.json
    try:
        params = Request().load(pop)
    except ValidationError as e:
        return e.messages, 400
    try:
        res = response_builder(
            path=params['filename'],
            cmd1=params['cmd1'],
            param1=params['value1'],
            cmd2=params['cmd2'],
            param2=params['value2']
        )
        return res, 200
    except FileNotFoundError:
        return f"Файл '{params['filename']}' не найден", 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=10000)
