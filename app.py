from fastapi import FastAPI


app = FastAPI()

app.title = "MI PRIMERA APP"

app.summary = "Todavia no hace nada"

app.version = "2.5"

#PARAMETRO DE RUTA
#viene de la URL
@app.get("/saludo/{nombre}")
async def saludo_custom(nombre:str):
    return {"Hola": nombre}

#PARAMETROS QUERY
@app.get("/saludo")
async def saludo_query(nombre:str):
    return {"Hola": nombre}

@app.get("/")
async def saludo():
    return {"Hola": "Mundo"}


@app.put("/adios")
async def despedir():
    return {"Adios": "mundo"}

@app.post("/post")
async def post():
    return{"Adios":"mundo"}

@app.delete("/")
async def adios():
    return{"Chau":"mundo"}
