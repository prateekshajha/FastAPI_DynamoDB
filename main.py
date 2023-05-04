from fastapi import FastAPI,Path
app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}
