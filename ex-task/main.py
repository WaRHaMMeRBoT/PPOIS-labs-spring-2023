from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3
import text_recogniser

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    base = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("main.html", {"request": request, "base": base})


@app.get("/adding.html")
def root_add():
    return FileResponse("adding.html")


@app.get("/deleting.html")
def root_delete():
    return FileResponse("deleting.html")


@app.post("/add")
async def submit_add(request: Request):
    form_data = await request.form()
    user_name = form_data["Name"]
    user_email = form_data["Email"]
    user_number = form_data["PhoneNumber"]
    img = form_data["Image"]
    if len(img) > 0:
        text = text_recogniser.text_from_image(img)
        list = text.split()
        print(list)
        for element in list:
            if "@" in element:
                user_email = element
            if "+" in element:
                user_number = element
        if user_email != " ":
            if user_number != " ":
                user_name = " ".join(list[:2])
        print(user_name)
    if "" == user_name:
        if "" == user_email:
            if "" == user_number:
                return read_root(request)
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM users WHERE name = '{user_name}'")
    if cursor.fetchone() is None:
        cursor.execute(
            f"INSERT INTO users VALUES (?,?,?)", (user_name, user_email, user_number)
        )
        conn.commit()
    else:
        print("Already exists")
    base = cursor.fetchall()
    conn.close()
    templates.TemplateResponse("main.html", {"request": request, "base": base})
    return read_root(request)


@app.post("/delete")
async def submit_delete(request: Request):
    form_data = await request.form()
    user_name = form_data["Name"]
    user_email = form_data["Email"]
    user_number = form_data["PhoneNumber"]
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE name = '{user_name}'")
    cursor.execute(f"DELETE FROM users WHERE email = '{user_email}'")
    cursor.execute(f"DELETE FROM users WHERE phoneNumber = '{user_number}'")
    conn.commit()
    base = cursor.fetchall()
    conn.close()
    templates.TemplateResponse("main.html", {"request": request, "base": base})
    return read_root(request)


@app.post("/search")
async def submit_search(request: Request):
    form_data = await request.form()
    user_name = form_data["Name"]
    user_email = form_data["Email"]
    user_number = form_data["PhoneNumber"]
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users")
    base = cursor.fetchall()
    print(base)
    for value in base:
        if value[0] == user_name:
            base = []
            base.append(value)
            continue
        if value[2] == user_number:
            base = []
            base.append(value)
            continue
        if value[1] == user_email:
            base = []
            base.append(value)
            continue
    return templates.TemplateResponse("main.html", {"request": request, "base": base})
