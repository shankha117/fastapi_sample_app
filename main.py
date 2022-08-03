from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'shankha'}}


@app.get('/about')
def index():
    return {'data': {'about': 'shankha_shankha'}}


