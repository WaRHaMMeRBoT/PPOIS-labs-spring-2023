from fastapi import FastAPI, Response, Query, Body, Depends, Request
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from DataBase import *

Base.metadata.create_all(bind=engine)

app = FastAPI()
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


@app.get("/api/tournaments")
def get_tournaments(db: Session = Depends(get_db)):
    return db.query(Tournament).all()


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


@app.delete("/api/tournaments")
def delete_tournaments(data=Body(), db: Session = Depends(get_db)):
    if data["value"] == 1:
        found_values1 = db.query(Tournament).filter(Tournament.tournament_name == data["tournament_name"]).all()
        found_values2 = db.query(Tournament).filter(Tournament.date == data["date"]).all()
        found_values = found_values1 + found_values2
        if not found_values:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        for i in found_values:
            db.delete(i)
        db.commit()
        return found_values
    elif data["value"] == 2:
        found_values1 = db.query(Tournament).filter(Tournament.sport_name == data["sport_name"]).all()
        found_values2 = db.query(Tournament).filter(Tournament.winner_name == data["winner_name"]).all()
        found_values = found_values1 + found_values2
        if not found_values:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        for i in found_values:
            db.delete(i)
        db.commit()
        return found_values
    elif data["value"] == 3:
        found_values1 = db.query(Tournament).filter(
            data["prize_money"]["low"] < Tournament.prize_money, Tournament.prize_money < data["prize_money"]["high"]).all()
        found_values2 = db.query(Tournament).filter(
            data["winner_money"]["low"] < Tournament.winner_money, Tournament.winner_money < data["winner_money"]["high"]).all()
        found_values = found_values1 + found_values2
        if not found_values:
            return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
        for i in found_values:
            db.delete(i)
        db.commit()
        return found_values
    else:
        return JSONResponse(status_code=404, content={"message": "Значение не найдено"})


@app.post("/api/tournaments")
def create_tournament(data=Body(), db: Session = Depends(get_db)):
    tournament = Tournament(tournament_name=data["tournament_name"], date=data["date"], sport_name=data["sport_name"],
                            winner_name=data["winner_name"], prize_money=data["prize_money"],
                            winner_money=int(data["prize_money"] * 0.6))
    db.add(tournament)
    db.commit()
    db.refresh(tournament)
    return tournament


@app.get("/deleteName")
async def delete(query1: str, query2: str, db: Session = Depends(get_db)):
    found_values1 = db.query(Tournament).filter(Tournament.tournament_name == query1).all()
    found_values2 = db.query(Tournament).filter(Tournament.date == query2).all()
    found_values = found_values1 + found_values2
    return {"query1": query1, "query2": query2, "found_values1": found_values}


@app.get("/deleteSport")
async def delete(query3: str, query4: str, db: Session = Depends(get_db)):
    found_values1 = db.query(Tournament).filter(Tournament.sport_name == query3).all()
    found_values2 = db.query(Tournament).filter(Tournament.winner_name == query4).all()
    found_values = found_values1 + found_values2
    return {"query3": query3, "query4": query4, "found_values2": found_values}


@app.get("/deleteMoney")
async def delete(query5: int = 0, query6: int = 0, query7: int = 0, query8: int = 0, db: Session = Depends(get_db)):
    found_values1 = db.query(Tournament).filter(query6 < Tournament.prize_money, Tournament.prize_money < query5).all()
    found_values2 = db.query(Tournament).filter(query8 < Tournament.winner_money,  Tournament.winner_money < query7).all()
    found_values = found_values1 + found_values2
    return {"query5": query5, "query6": query6, "query7": query7, "query8": query8, "found_values3": found_values}
