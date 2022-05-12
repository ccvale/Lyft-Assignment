from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

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

'''
Deadline: May 13 8PM
https://boards.greenhouse.io/lyft/jobs/6063505002?gh_jid=6063505002#app
'''

app = FastAPI()

templates = Jinja2Templates(directory='templates')

# s = 'iamyourlyftdriver'

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
        return {'return_string': 'Error - string should be at least 3 characters!'}
    return {'return_string': everyThird(req.string_to_cut)}


if __name__ == '__main__':
    uvicorn.run('lyft:app', host='localhost', port=8000, reload=True)
