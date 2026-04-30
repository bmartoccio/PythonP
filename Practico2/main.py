from fastapi import FastAPI, Body, Path, Query

app = FastAPI()

app.title = "LIBRERIA"

app.version = "1.0"

libros = [
    {"id":1, "nombre":"Un cuento perfecto", "precio":30000, "activo":True},
    {"id":2, "nombre":"Donde todo brilla", "precio":25000, "activo":True},
    {"id":3, "nombre":"Romper el circulo", "precio":45000, "activo":True},
    {"id":4, "nombre":"El vizconde que me amo", "precio":50000, "activo":True},
    {"id":5, "nombre":"La amiga estupenda", "precio":35000, "activo":True},
    {"id":6, "nombre":"Donde habitan la sirenas", "precio":25000, "activo":True},
    {"id":7, "nombre":"Cuando no queden mas estrellas que contar", "precio":20000, "activo":True},
    {"id":8, "nombre":"Todas esas cosas que te dire mañana", "precio":25000, "activo":True},
    {"id":9, "nombre":"Quedara el amor", "precio":35000, "activo":True},
    {"id":10, "nombre":"Ugly Love", "precio":40000, "activo":True}
]

#MUESTRA TODO EL CONTENIDO DE LA LISTA
@app.get("/libros")
async def get_libros():
    return libros

#BUSCA POR ID
@app.get("/libros/{id}")
async def get_libros_id(id:int=Path(gt=0)):
    for libro in libros:
         if libro ["id"] == id:
            return libro
    return {"mensaje": "No se encontro libro"}

#BUSCA POR INICIAL
@app.get("/libros/buscar/inicial")
async def encontrar_por_inicial (letra: str = Query(min_length=1, max_length=1, description="Ingresa una letra")):
    libro_encontrado = []
    for libro in libros:
        if libro ["nombre"][0].lower() == letra.lower():
            libro_encontrado.append({"nombre":libro["nombre"],"precio": libro["precio"]})
    if libro_encontrado:
        return libro_encontrado
    else:
        return {"mensaje": f"No se encontraron resultados con la letra: {letra}"}


#AGREGA UN NUEVO LIBRO

@app.post("/libros")
async def publicar_libro(id:int = Body(gt=10), nombre:str = Body(min_length=3), precio: int = Body(gt=1000)):
    nuevo_libro = {
        "id" : id,
        "nombre" : nombre,
        "precio" : precio,
    }
    libros.append(nuevo_libro)
    return nuevo_libro


#EDITA UN LIBRO
@app.put("/libros/{id}")
async def editar_libro (id:int = Path(gt=0, description='Id del art para editar '), nombre: str = Body(min_length=3), precio: int = Body(ge = 1000, lt=9999999)):
    for libro in libros:
        if libro["id"] == id :
            libro["nombre"] = nombre
            libro["precio"] = precio
            return libro    
    return {"Not Found"}


#ELIMINAR UN LIBRO
@app.delete("/libros/{id}") 
async def borra_libro(id:int = Path(gt=0), logico:bool = Query (description="True si borrado logico")):
    for libro in libros:
        if libro["id"] == id:
            if logico:
                libro["activo"] = False
            else:    
                libros.remove(libro)
            return libros