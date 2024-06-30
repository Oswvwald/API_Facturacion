from config.pg_cnn import Facturacion_app
from datetime import datetime

def ObtenerCliente():
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Clientes"
        cursor.execute(query)
        Clientes = cursor.fetchall()  # Obtener todos los clientes
        # Convertir los clientes a una lista de diccionarios
        Clientes_dict = [dict(zip([column[0] for column in cursor.description], row)) for row in Clientes]
        
        # Convertir los campos de fecha a cadenas
        for cliente in Clientes_dict:
            if 'fecha_nacimiento' in cliente:
                cliente['fecha_nacimiento'] = cliente['fecha_nacimiento'].strftime("%Y-%m-%d")
        
        Facturacion_app.commit()
        return Clientes_dict # Devolver los clientes como un JSON
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)

def ObtenerClienteId(id):
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Clientes WHERE cedula = %s"
        cursor.execute(query, (id,))
        Clientes = cursor.fetchall()  # Obtener todos los clientes
        Facturacion_app.commit()

        # Convertir los clientes a una lista de diccionarios
        Clientes_dict = [dict(zip([column[0] for column in cursor.description], row)) for row in Clientes]
        
        # Convertir los campos de fecha a cadenas
        for cliente in Clientes_dict:
            if 'fecha_nacimiento' in cliente:
                cliente['fecha_nacimiento'] = cliente['fecha_nacimiento'].strftime("%Y-%m-%d")
        
        Facturacion_app.commit()
        return Clientes_dict # Devolver los clientes como un JSON
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)
    
def CrearCliente(cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado):
    try:
        cursor = Facturacion_app.cursor()
        query = "INSERT INTO Clientes (cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
        cursor.execute(query, (cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado))
        row = cursor.fetchone()
        Facturacion_app.commit()

        if row is not None:
            new_cliente = { "cedula": row[0], "nombres": row[1], "apellidos": row[2], "fecha_nacimiento": row[3], "direccion": row[4], "telefono": row[5], "email": row[6], "tipo_cliente_id": row[7], "estado": row[8]}
            # Convertir el campo de fecha a cadena
            if 'fecha_nacimiento' in new_cliente:
                new_cliente['fecha_nacimiento'] = new_cliente['fecha_nacimiento'].strftime("%Y-%m-%d")
            return new_cliente
        else:
            return "No se pudo insertar el cliente"    
    except Exception as e:
        return str(e)

def ActualizarCliente(cedula, nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado):
    try:
        cursor = Facturacion_app.cursor()
        query = "UPDATE Clientes SET nombres = %s, apellidos = %s, fecha_nacimiento = %s, direccion = %s, telefono = %s, email = %s, tipo_cliente_id = %s, estado = %s WHERE cedula = %s RETURNING *"
        cursor.execute(query, (nombres, apellidos, fecha_nacimiento, direccion, telefono, email, tipo_cliente_id, estado, cedula))
        row = cursor.fetchone()
        Facturacion_app.commit()

        if row is not None:
            updated_cliente = { "cedula": row[0], "nombres": row[1], "apellidos": row[2], "fecha_nacimiento": row[3], "direccion": row[4], "telefono": row[5], "email": row[6], "tipo_cliente_id": row[7], "estado": row[8]}
            # Convertir el campo de fecha a cadena
            if 'fecha_nacimiento' in updated_cliente:
                updated_cliente['fecha_nacimiento'] = updated_cliente['fecha_nacimiento'].strftime("%Y-%m-%d")
            return updated_cliente
        else:
            return "No se pudo actualizar el cliente"    
    except Exception as e:
        return str(e)

def EliminarCliente(cedula):
    try:
        cursor = Facturacion_app.cursor()
        query = "DELETE FROM Clientes WHERE cedula = %s RETURNING *"
        cursor.execute(query, (cedula,))
        row = cursor.fetchone()
        Facturacion_app.commit()

        if row is not None:
            deleted_cliente = { "cedula": row[0], "nombres": row[1], "apellidos": row[2], "fecha_nacimiento": row[3], "direccion": row[4], "telefono": row[5], "email": row[6] }
            # Devolver el diccionario directamente
            if 'fecha_nacimiento' in deleted_cliente:
                deleted_cliente['fecha_nacimiento'] = deleted_cliente['fecha_nacimiento'].strftime("%Y-%m-%d")
            return deleted_cliente
        else:
            return "No se pudo eliminar el cliente"
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)
    
def to_dict(self):
    return {
        "cedula": self.cedula,
        "nombres": self.nombres,
        "apellidos": self.apellidos,
        "fecha_nacimiento": self.fecha_nacimiento.isoformat(),
        "direccion": self.direccion,
        "telefono": self.telefono,
        "email": self.email,
        "tipo_cliente_id": self.tipo_cliente_id,
        "estado": self.estado
    }