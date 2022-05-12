from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
class LyftRequest(BaseModel):
    string_to_cut: str

'''
The application only needs to do the following:
Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
Return a JSON object with the key “return_string” and a string containing every third
letter from the original string
(e.g.) If you POST {'string_to_cut': 'iamyourlyftdriver'}, it will return: 
{'return_string': 'muydv'}.
'''

app = FastAPI()

templates = Jinja2Templates(directory='templates')

def everyThird(s: str):
    new = ''
    for i in range(2, len(s), 3):
        new += s[i]
    return new

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/test')
def test(req: LyftRequest):
    if len(req.string_to_cut) < 3:
        raise HTTPException(
            status_code = 400,
            detail = f'"{req.string_to_cut}" is not at least 3 characters'
        )
    return {'return_string': everyThird(req.string_to_cut)}
