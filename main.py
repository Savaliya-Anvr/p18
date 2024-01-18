from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root(id:int):
    return {'data':f'{id} is your personal ID'}

if __name__ == '__main__':
    uvicorn.run(app)

