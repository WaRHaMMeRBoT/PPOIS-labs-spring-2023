from fastapi import FastAPI, Response, Query, Body, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from DataBase import *

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return FileResponse('public/index.html')


@app.get("/api/students")
def get_persons(db: Session = Depends(get_db)):
    return db.query(Person).all()


@app.get("/new-page")
def get_deleteByName(value: int):
    if value == 1:
        return FileResponse('public/deleteByName.html')
    elif value == 2:
        return FileResponse('public/deleteBySport.html')
    elif value == 3:
        return FileResponse('public/deleteByMoney.html')
    else:
        return JSONResponse(status_code=404, content={"message": "Значение не найдено"})


@app.delete("/api/students")
def delete_persons(data=Body(), db: Session = Depends(get_db)):
    if data["value"] == 1:
        found_values1 = db.query(Person).filter(Person.person_name == data["person_name"]).all()
        found_values2 = db.query(Person).filter(Person.date == data["date"]).all()
        found_values = found_values1 + found_values2
        if not found_values:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        for i in found_values:
            db.delete(i)
        db.commit()
        return found_values
    elif data["value"] == 2:
        found_values1 = db.query(Person).filter(Person.ill_hours == data["ill_hours"]).all()
        found_values2 = db.query(Person).filter(Person.other_reason == data["other_reason"]).all()
        found_values = found_values1 + found_values2
        if not found_values:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        for i in found_values:
            db.delete(i)
        db.commit()
        return found_values
    elif data["value"] == 3:
        found_values1 = db.query(Person).filter(
            data["no_reason"]["low"] < Person.no_reason, Person.no_reason < data["no_reason"]["high"]).all()
        found_values2 = db.query(Person).filter(
            data["all_hours"]["low"] < Person.all_hours, Person.all_hours < data["all_hours"]["high"]).all()
        found_values = found_values1 + found_values2
        if not found_values:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        for i in found_values:
            db.delete(i)
        db.commit()
        return found_values
    else:
        return JSONResponse(status_code=404, content={"message": "Значение не найдено"})


@app.post("/api/students")
def create_person(data=Body(), db: Session = Depends(get_db)):
    person = Person(person_name=data["person_name"], date=data["date"], ill_hours=data["ill_hours"],
                            other_reason=data["other_reason"], no_reason=data["no_reason"],
                            all_hours=int(int(data["no_reason"]) + int(data["other_reason"]) + int(data["ill_hours"])))
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@app.get("/deleteName")
async def delete(query1: str, query2: str, db: Session = Depends(get_db)):
    found_values1 = db.query(Person).filter(Person.person_name == query1).all()
    found_values2 = db.query(Person).filter(Person.date == query2).all()
    found_values = found_values1 + found_values2
    return {"query1": query1, "query2": query2, "found_values1": found_values}


@app.get("/deleteSport")
async def delete(query3: str, query4: str, db: Session = Depends(get_db)):
    found_values1 = db.query(Person).filter(Person.ill_hours == query3).all()
    found_values2 = db.query(Person).filter(Person.other_reason == query4).all()
    found_values = found_values1 + found_values2
    return {"query3": query3, "query4": query4, "found_values2": found_values}


@app.get("/deleteMoney")
async def delete(query5: int = 0, query6: int = 0, query7: int = 0, query8: int = 0, db: Session = Depends(get_db)):
    found_values1 = db.query(Person).filter(query6 < Person.no_reason, Person.no_reason < query5).all()
    found_values2 = db.query(Person).filter(query8 < Person.all_hours,  Person.all_hours < query7).all()
    found_values = found_values1 + found_values2
    return {"query5": query5, "query6": query6, "query7": query7, "query8": query8, "found_values3": found_values}
