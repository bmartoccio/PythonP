from fastapi import FastAPI


app = FastAPI()

app.title = "Mi primera App"
app.summary = "Path Operations"
app.version = "1.0"

#Consultar informacion
@app.get("/")
async def saludo():
    return {"Hola": "Mundo"}

#Modificar
@app.put("/saludo/{nombre}")
async def despedir(nombre:str):
    return {"Hola": nombre}

#Crear
@app.post("/crear/{nombre}/{edad}")
async def post(nombre:str,edad:int):
    return{"Adios":nombre,
           "edad":edad}

#Eliminar
@app.delete("/elimina/{nombre}")
async def adios(nombre:str):
    return {"Chau":nombre}