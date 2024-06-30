from fastapi import APIRouter, UploadFile, File, Form
from typing import Annotated
from pydantic import BaseModel

#model 
from controller import tipoPago_controller

#object body json
class tipoCliente(BaseModel):
    tipo: str
    descripcion: str

#variable de ruta
appTipoPago = APIRouter()

#rutas de appTipoPago
@appTipoPago.get("/tipoPago", tags=["TipoPago"])
def getTipoCliente():
    return tipoPago_controller.getTipoCliente()

@appTipoPago.get("/tipoPago/{id}", tags=["TipoPago"])
def getTipoClienteId(id: int):
    return tipoPago_controller.getTipoClienteId(id)

@appTipoPago.post("/tipoPago", tags=["TipoPago"])
def createTipoCliente(tipo: tipoCliente):
    return tipoPago_controller.createTipoCliente(tipo.tipo, tipo.descripcion)

@appTipoPago.put("/tipoPago/{tipo_code}", tags=["TipoPago"])
def updateTipoCliente(tipo_code: int, tipo: tipoCliente):
    return tipoPago_controller.updateTipoCliente(tipo_code, tipo.tipo, tipo.descripcion)

@appTipoPago.delete("/tipoPago/{tipo_code}", tags=["TipoPago"])
def deleteTipoCliente(tipo_code: int):
    return tipoPago_controller.deleteTipoCliente(tipo_code)