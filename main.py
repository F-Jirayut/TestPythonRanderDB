import psycopg2
from fastapi import FastAPI

app = FastAPI()
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