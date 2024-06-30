from fastapi.responses import JSONResponse
from model import tipoPago_model

def getTipoCliente():
    try:
        mensaje = tipoPago_model.ObtenerTipoCliente()
        return JSONResponse(status_code=200, content={"status":200, "tipoPago": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})
    
def getTipoClienteId(id):
    try:
        mensaje = tipoPago_model.ObtenerTipoClienteId(id)
        return JSONResponse(status_code=200, content={"status":200, "tipoPago": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})

def createTipoCliente(tipo, descripcion):
    try:
        mensaje = tipoPago_model.CrearTipoCliente(tipo, descripcion)
        return JSONResponse(status_code=200, content={"status":200, "tipoPago": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})

def updateTipoCliente(tipo_code, tipo, description):
    try:
        mensaje = tipoPago_model.ActualizarTipoCliente(tipo_code, tipo, description)
        return JSONResponse(status_code=200, content={"status":200, "tipoPago": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})

def deleteTipoCliente(tipo_code):
    try:
        mensaje = tipoPago_model.EliminarTipoCliente(tipo_code)
        return JSONResponse(status_code=200, content={"status":200, "tipoPago": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})