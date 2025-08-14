from fastapi import FastAPI,HTTPException
from services.data_loader import Dal

app = FastAPI()
dal = Dal()
dal.connect()


@app.get("/")
def home():
    return {"message": "hello"}

@app.get("get_people")
def get_people():
    try:
        sql_string = "SELECT * FROM Studens"
        return dal.execute_query(sql_string)
    except Exception as e :
        print(f"erorr {e}  ")



