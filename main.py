from fastapi import FastAPI

from uce.ai.openuce import Document, process_inference

import uvicorn

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hola, esta es una práctica de uso de los tokens OpenIA"}


@app.get("/Hola/{name}")
async def say_hello(name: str):
    return {"message": f"Hola {name}"}


@app.post("/inference", status_code=200)
def inference(doc: Document):
    explicacion = process_inference(doc.item)
    return {
        'Respuesta de la interación con el chat': explicacion[0],
        'Total de tokens consumidos: ': explicacion[1]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port = 1045)
