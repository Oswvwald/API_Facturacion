from fastapi.responses import JSONResponse
from model import clientes_model

def getClientes():
    try:
        mensaje = clientes_model.ObtenerCliente()
        return JSONResponse(status_code=200, content={"status":200, "clientes": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})

def getClienteId(cedula):
    try:
        mensaje = clientes_model.ObtenerClienteId(cedula)
        return JSONResponse(status_code=200, content={"status":200, "cliente": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})
    
def createCliente(cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado):
    try:
        mensaje = clientes_model.CrearCliente(cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado)
        return JSONResponse(status_code=200, content={"status":200, "cliente": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})

def updateCliente(cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado):
    try:
        mensaje = clientes_model.ActualizarCliente(cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado)
        return JSONResponse(status_code=200, content={"status":200, "cliente": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})

def deleteCliente(cedula):
    try:
        mensaje = clientes_model.EliminarCliente(cedula)
        return JSONResponse(status_code=200, content={"status":200, "cliente": mensaje})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status":500, "message": str(e)})
