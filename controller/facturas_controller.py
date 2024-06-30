from fastapi.responses import JSONResponse
from model import facturas_model

def getFacturas():
    try:
        mensaje = facturas_model.ObtenerFacturas()
        return JSONResponse(status_code=200, content={"status": 200, "facturas": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def getFacturaById(factura_id):
    try:
        mensaje = facturas_model.ObtenerFacturaId(factura_id)
        return JSONResponse(status_code=200, content={"status": 200, "factura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def createFactura(factura_id, cedula_cliente, tipo_pago, fecha, total, iva):
    try:
        mensaje = facturas_model.CrearFactura(factura_id, cedula_cliente, tipo_pago, fecha, total, iva)
        return JSONResponse(status_code=200, content={"status": 200, "factura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def updateFactura(factura_id, cedula_cliente, tipo_pago, fecha, total, iva):
    try:
        mensaje = facturas_model.ActualizarFactura(factura_id, cedula_cliente, tipo_pago, fecha, total, iva)
        return JSONResponse(status_code=200, content={"status": 200, "factura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def deleteFactura(factura_id):
    try:
        mensaje = facturas_model.EliminarFactura(factura_id)
        return JSONResponse(status_code=200, content={"status": 200, "factura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})
