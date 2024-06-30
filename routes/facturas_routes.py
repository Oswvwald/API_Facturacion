from fastapi import APIRouter
from typing import Annotated
from pydantic import BaseModel
from datetime import datetime

# Importar el controlador
from controller import facturas_controller

# Definir los objetos body JSON
class Factura(BaseModel):
    factura_id: str
    cedula_cliente: str
    tipo_pago: int
    fecha: datetime
    total: float
    iva: float

class FacturaUpdate(BaseModel):
    cedula_cliente: str
    tipo_pago: int
    fecha: datetime
    total: float
    iva: float

# Variable de ruta
appFacturas = APIRouter()

# Rutas para appFacturas
@appFacturas.get("/facturas", tags=["Facturas"])
def getFacturas():
    return facturas_controller.getFacturas()

@appFacturas.get("/facturas/{factura_id}", tags=["Facturas"])
def getFacturaById(factura_id: str):
    return facturas_controller.getFacturaById(factura_id)

@appFacturas.post("/facturas", tags=["Facturas"])
def createFactura(factura: Factura):
    return facturas_controller.createFactura(factura.factura_id, factura.cedula_cliente, factura.tipo_pago, factura.fecha, factura.total, factura.iva)

@appFacturas.put("/facturas/{factura_id}", tags=["Facturas"])
def updateFactura(factura_id: str, factura: FacturaUpdate):
    return facturas_controller.updateFactura(factura_id, factura.cedula_cliente, factura.tipo_pago, factura.fecha, factura.total, factura.iva)

@appFacturas.delete("/facturas/{factura_id}", tags=["Facturas"])
def deleteFactura(factura_id: str):
    return facturas_controller.deleteFactura(factura_id)
