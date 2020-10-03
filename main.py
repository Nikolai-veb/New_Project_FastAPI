from fastapi import FastAPI


app = FastAPI()

@app:get('/')
def home():
    return {'key': "Hellow World"}




#if __namme__ == '__main__':
   # main()
