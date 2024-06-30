from config.pg_cnn import Facturacion_app
from datetime import datetime
from decimal import Decimal

def decimal_to_float(value):
    if isinstance(value, Decimal):
        return float(value)
    return value

def date_to_str(value):
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value

def convert_fields(record):
    for key in record:
        record[key] = decimal_to_float(record[key])
        record[key] = date_to_str(record[key])
    return record

def ObtenerFacturas():
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Facturas"
        cursor.execute(query)
        facturas = cursor.fetchall()
        # Convertir las facturas a una lista de diccionarios
        facturas_dict = [dict(zip([column[0] for column in cursor.description], row)) for row in facturas]
        
        # Convertir campos Decimal y fecha
        facturas_dict = [convert_fields(factura) for factura in facturas_dict]
        
        Facturacion_app.commit()
        return facturas_dict
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)

def ObtenerFacturaId(factura_id):
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Facturas WHERE factura_id = %s"
        cursor.execute(query, (factura_id,))
        factura = cursor.fetchone()
        Facturacion_app.commit()
        if factura:
            factura_dict = dict(zip([column[0] for column in cursor.description], factura))
            # Convertir campos Decimal y fecha
            factura_dict = convert_fields(factura_dict)
            return factura_dict
        else:
            return None
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)

def CrearFactura(factura_id, cedula_cliente, tipo_pago, fecha, total, iva):
    try:
        cursor = Facturacion_app.cursor()
        query = "INSERT INTO Facturas (factura_id, cedula_cliente, tipo_pago, fecha, total, iva) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
        cursor.execute(query, (factura_id, cedula_cliente, tipo_pago, fecha, total, iva))
        row = cursor.fetchone()
        Facturacion_app.commit()
        if row:
            new_factura = dict(zip([column[0] for column in cursor.description], row))
            # Convertir campos Decimal y fecha
            new_factura = convert_fields(new_factura)
            return new_factura
        else:
            return None
    except Exception as e:
        return str(e)

def ActualizarFactura(factura_id, cedula_cliente, tipo_pago, fecha, total, iva):
    try:
        cursor = Facturacion_app.cursor()
        query = "UPDATE Facturas SET cedula_cliente = %s, tipo_pago = %s, fecha = %s, total = %s, iva = %s WHERE factura_id = %s RETURNING *"
        cursor.execute(query, (cedula_cliente, tipo_pago, fecha, total, iva, factura_id))
        row = cursor.fetchone()
        Facturacion_app.commit()
        if row:
            updated_factura = dict(zip([column[0] for column in cursor.description], row))
            # Convertir campos Decimal y fecha
            updated_factura = convert_fields(updated_factura)
            return updated_factura
        else:
            return None
    except Exception as e:
        return str(e)

def EliminarFactura(factura_id):
    try:
        cursor = Facturacion_app.cursor()
        query = "DELETE FROM Facturas WHERE factura_id = %s RETURNING *"
        cursor.execute(query, (factura_id,))
        row = cursor.fetchone()
        Facturacion_app.commit()
        if row:
            deleted_factura = dict(zip([column[0] for column in cursor.description], row))
            # Convertir campos Decimal y fecha
            deleted_factura = convert_fields(deleted_factura)
            return deleted_factura
        else:
            return None
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)
