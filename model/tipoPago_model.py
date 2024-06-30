from config.pg_cnn import Facturacion_app

def ObtenerTipoCliente():
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Tipo_Pago"
        cursor.execute(query)
        TipoCliente = cursor.fetchall()  # Obtener todos los tipos clientes
        # Convertir los tipos clientes a una lista de diccionarios
        TipoCliente_dict = [dict(zip([column[0] for column in cursor.description], row)) for row in TipoCliente]
        Facturacion_app.commit()
        return TipoCliente_dict # Devolver los tipos clientes como un JSON
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e) 
    
def ObtenerTipoClienteId(id):
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Tipo_Pago WHERE tipo_code = %s"
        cursor.execute(query, (id,))
        TipoCliente = cursor.fetchall()  # Obtener todos los tipos clientes
        Facturacion_app.commit()
        # Convertir los tipos clientes a una lista de diccionarios
        TipoCliente_dict = [dict(zip([column[0] for column in cursor.description], row)) for row in TipoCliente]
        Facturacion_app.commit()
        return TipoCliente_dict # Devolver los tipos clientes como un JSON
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)
    
def CrearTipoCliente(tipo, descripcion):
    try:
        cursor = Facturacion_app.cursor()
        query = "INSERT INTO Tipo_Pago (tipo, descripcion) VALUES (%s, %s) RETURNING *"
        cursor.execute(query, (tipo, descripcion))
        row = cursor.fetchone()
        Facturacion_app.commit()

        if row is not None:
            new_tipo_cliente = { "tipo_code": row[0], "tipo": row[1], "descripcion": row[2] }
            # Devolver el diccionario directamente
            return new_tipo_cliente
        else:
            return "No se pudo insertar el tipo de cliente"
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)
    

def ActualizarTipoCliente(tipo_code, tipo, descripcion):
    try:
        cursor = Facturacion_app.cursor()
        query = "UPDATE Tipo_Pago SET tipo = %s, descripcion = %s WHERE tipo_code = %s RETURNING *"
        cursor.execute(query, (tipo, descripcion, tipo_code))
        row = cursor.fetchone()
        Facturacion_app.commit()

        if row is not None:
            updated_tipo_cliente = { "tipo_code": row[0], "tipo": row[1], "descripcion": row[2] }
            # Devolver el diccionario directamente
            return updated_tipo_cliente
        else:
            return "No se pudo actualizar el tipo de cliente"
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)
    
def EliminarTipoCliente(tipo_code):
    try:
        cursor = Facturacion_app.cursor()
        query = "DELETE FROM Tipo_Pago WHERE tipo_code = %s"
        cursor.execute(query, (tipo_code,))
        Facturacion_app.commit()
        Facturacion_app.commit()

        if cursor.rowcount > 0:
            return "Tipo de cliente eliminado"
        else:
            return "No se encontró el tipo de cliente con el id proporcionado"
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)