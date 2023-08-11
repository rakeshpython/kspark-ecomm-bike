from fastapi import FastAPI
from bike import Bike

app = FastAPI()
Bike_list = []


@app.get("/")
def bike_shop():
    print(f"inside Bike_shop")
    return {"message": "Welcome to the Bike Shop"}


@app.post("/new-bike")
def add_new_bike(Bike: Bike):
    Bike_list.append(Bike.dict())
    return Bike_list


@app.get("/bikes")
def get_all_bikes():
    return Bike_list


@app.delete("/bikes/{id}")
def remove_bikes_by_id(id: int):
    print(f"remove_desktop_by_id|id{id}")
    return Bike_list

# if __name__ == '__main__':
#    print(f"startup |")
