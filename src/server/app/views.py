from app import app_


@app_.errorhandler(404)
def page_not_found(e):
    return "404 page not found."


@app_.route('/')
def index():
    return 'Hello World!'

