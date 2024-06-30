from fastapi import APIRouter, UploadFile, File, Form
from typing import Annotated
from pydantic import BaseModel
from datetime import date

#model 
from controller import clientes_controller

#objetos body json
class Cliente(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    direccion: str
    telefono: str
    email: str
    id_tipo_pago: int
    estado: bool

class Cliente2(BaseModel):
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    direccion: str
    telefono: str
    email: str
    id_tipo_pago: int
    estado: bool

#variable de ruta
appClientes = APIRouter()

#rutas para appClientes
@appClientes.get("/clientes", tags=["Clientes"])
def getClientes():
    return clientes_controller.getClientes()

@appClientes.get("/clientes/{cedula}", tags=["Clientes"])
def getClienteId(cedula: str):
    return clientes_controller.getClienteId(cedula)

@appClientes.post("/clientes", tags=["Clientes"])
def createCliente(cliente: Cliente):
    return clientes_controller.createCliente(cliente.cedula, cliente.nombres, cliente.apellidos, cliente.fecha_nacimiento, cliente.direccion, cliente.telefono, cliente.email, cliente.id_tipo_pago, cliente.estado)

@appClientes.put("/clientes/{cedula}", tags=["Clientes"])
def updateCliente(cedula: str, cliente: Cliente2):
    return clientes_controller.updateCliente(cedula, cliente.nombres, cliente.apellidos, cliente.fecha_nacimiento, cliente.direccion, cliente.telefono, cliente.email, cliente.id_tipo_pago, cliente.estado)

@appClientes.delete("/clientes/{cedula}", tags=["Clientes"])
def deleteCliente(cedula: str):
    return clientes_controller.deleteCliente(cedula)
