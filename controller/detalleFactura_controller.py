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

def createDetalleFactura(factura_id, producto_id, nombre_producto, descripcion_producto, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total):
    try:
        mensaje = detalleFactura_model.CrearDetalleFactura(factura_id, producto_id, nombre_producto, descripcion_producto, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def getDetalleFacturaByFacturaId(factura_id):
    try:
        detalles = detalleFactura_model.ObtenerDetallesPorFactura(factura_id)
        if detalles:
            return JSONResponse(status_code=200, content={"status": 200, "detallesFactura": detalles})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron detalles para la factura especificada"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def updateDetalleFactura(detalle_id, factura_id, producto_id, nombre_producto, descripcion_producto, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total):
    try:
        mensaje = detalleFactura_model.ActualizarDetalleFactura(detalle_id, factura_id, producto_id, nombre_producto, descripcion_producto, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def deleteDetalleFactura(detalle_id):
    try:
        mensaje = detalleFactura_model.EliminarDetalleFactura(detalle_id)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def deleteDetalleFacturaByFacturaId(factura_id):
    try:
        mensaje = detalleFactura_model.eliminarDetallesPorFacturaId(factura_id)
        return JSONResponse(status_code=200, content={"status": 200, "detalleFactura": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})

def getNombresProductosByFacturaId(factura_id):
    try:
        nombres_productos = detalleFactura_model.ObtenerNombresProductosPorFactura(factura_id)
        return JSONResponse(status_code=200, content={"status": 200, "nombresProductos": nombres_productos})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": str(e)})
