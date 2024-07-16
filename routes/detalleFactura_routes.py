from fastapi import APIRouter
from typing import Annotated
from pydantic import BaseModel

# Importar el controlador
from controller import detalleFactura_controller

# Definir los objetos body JSON
class DetalleFactura(BaseModel):
    factura_id: str
    producto_id: int
    nombre_producto: str
    descripcion_producto: str
    cantidad: int
    precio_unitario: float
    incluye_iva: bool
    porcentaje_iva: float
    subtotal: float
    total: float

class DetalleFacturaUpdate(BaseModel):
    factura_id: str
    producto_id: int
    nombre_producto: str
    descripcion_producto: str
    cantidad: int
    precio_unitario: float
    incluye_iva: bool
    porcentaje_iva: float
    subtotal: float
    total: float

# Variable de ruta
appDetalleFactura = APIRouter()

# Rutas para appDetalleFactura
@appDetalleFactura.get("/detalle_factura", tags=["Detalle Factura"])
def getDetallesFactura():
    return detalleFactura_controller.getDetallesFactura()

@appDetalleFactura.get("/detalle_factura/{detalle_id}", tags=["Detalle Factura"])
def getDetalleFacturaById(detalle_id: int):
    return detalleFactura_controller.getDetalleFacturaById(detalle_id)

@appDetalleFactura.post("/detalle_factura", tags=["Detalle Factura"])
def createDetalleFactura(detalle_factura: DetalleFactura):
    return detalleFactura_controller.createDetalleFactura(
        detalle_factura.factura_id, 
        detalle_factura.producto_id, 
        detalle_factura.nombre_producto,
        detalle_factura.descripcion_producto,
        detalle_factura.cantidad, 
        detalle_factura.precio_unitario, 
        detalle_factura.incluye_iva, 
        detalle_factura.porcentaje_iva, 
        detalle_factura.subtotal, 
        detalle_factura.total
    )

@appDetalleFactura.get("/detalle_factura/factura/{factura_id}", tags=["Detalle Factura"])
def getDetalleFacturaByFacturaId(factura_id: str):
    return detalleFactura_controller.getDetalleFacturaByFacturaId(factura_id)

@appDetalleFactura.put("/detalle_factura/{detalle_id}", tags=["Detalle Factura"])
def updateDetalleFactura(detalle_id: int, detalle_factura: DetalleFacturaUpdate):
    return detalleFactura_controller.updateDetalleFactura(
        detalle_id, 
        detalle_factura.factura_id, 
        detalle_factura.producto_id, 
        detalle_factura.nombre_producto,
        detalle_factura.descripcion_producto,
        detalle_factura.cantidad, 
        detalle_factura.precio_unitario, 
        detalle_factura.incluye_iva, 
        detalle_factura.porcentaje_iva, 
        detalle_factura.subtotal, 
        detalle_factura.total
    )

@appDetalleFactura.delete("/detalle_factura/{detalle_id}", tags=["Detalle Factura"])
def deleteDetalleFactura(detalle_id: int):
    return detalleFactura_controller.deleteDetalleFactura(detalle_id)

@appDetalleFactura.delete("/detalle_factura/factura/{factura_id}", tags=["Detalle Factura"])
def deleteDetalleFacturaByFacturaId(factura_id: str):
    return detalleFactura_controller.deleteDetalleFacturaByFacturaId(factura_id)

@appDetalleFactura.get("/detalle_factura/factura/{factura_id}/nombres_productos", tags=["Detalle Factura"])
def getNombresProductosByFacturaId(factura_id: str):
    return detalleFactura_controller.getNombresProductosByFacturaId(factura_id)
