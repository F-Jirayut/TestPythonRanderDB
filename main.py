import psycopg2
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
app = FastAPI()
test = 1

@app.get("/")
def read_root():
    try:
        con = psycopg2.connect(
            host = "dpg-ceqr3barrk0bsuje62q0-a" ,
            database = "test_python" ,
            user = "test_python_user" ,
            password = "4GEyvFJ9Djhluh0P9yH0UuZ7Qs1XDw1l",
            port = "5432"
        )
        return {"msg" : "ได้แล้วโว้ยยย"}
    except Exception as error:
        print ("Oops! An exception has occured:", error)
        print ("Exception TYPE:", type(error))
        return error

@app.on_event("startup")
@repeat_every(seconds=5)
def remove_expired_tokens_task() -> None:
    global test
    test = test + 1
    print(test)

@app.get("/count")
def get_count():
    return {"count" : test}