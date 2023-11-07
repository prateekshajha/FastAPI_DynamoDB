from fastapi import FastAPI
app=FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test/")
async def test(image_id,job_id=123,job_name='xyz'):
    result={"job_id":job_id,"job_name":job_name,"image_id":image_id}
    print(result)
    return result