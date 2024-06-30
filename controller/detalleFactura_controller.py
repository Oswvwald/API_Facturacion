from fastapi.responses import JSONResponse
from model import detalleFactura_model

def getDetallesFactura():
    try:
        mensaje = detalleFactura_model.ObtenerDetallesFactura()
        return JSONResponse(status_code=200, content={"status": 200, "detallesFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def getDetalleFacturaById(detalle_id):
    try:
        mensaje = detalleFactura_model.ObtenerDetalleFacturaId(detalle_id)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def createDetalleFactura(detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total):
    try:
        mensaje = detalleFactura_model.CrearDetalleFactura(detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def updateDetalleFactura(detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total):
    try:
        mensaje = detalleFactura_model.ActualizarDetalleFactura(detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def deleteDetalleFactura(detalle_id):
    try:
        mensaje = detalleFactura_model.EliminarDetalleFactura(detalle_id)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})
