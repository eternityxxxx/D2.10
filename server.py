import os
import sentry_sdk
from bottle import route, run, HTTPResponse, HTTPError
from sentry_sdk.integrations.bottle import BottleIntegration


sentry_sdk.init(
    dsn="", # Укажите свои данные
    integrations=[BottleIntegration()]
)


@route("/")
def index():
    message = """
    <h1>Добро пожаловать на простейший веб-сервер!</h1>
    <p>Список поддерживаемых маршрутов:</p>
    <ul>
        <li>"/success" - вернет вам HTTP ответ со статусом 200 OK</li>
        <li>"/fail" - вызовет ошибку сервера и вернет HTTP ответ со статусом 500</li>
    </ul>
    """
    return message


@route("/success")
def success():
    message = "<p>Ok</p>"
    result = HTTPResponse(status=200, body=message)
    return result


@route("/fail")
def fail():
    raise RuntimeError
    message = "Something went wrong.."
    result = HTTPError(status=500, body=message)
    return result

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
    )
else:
    run(host="localhost", port=8080, debug=True)