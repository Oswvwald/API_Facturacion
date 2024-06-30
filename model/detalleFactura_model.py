from config.pg_cnn import Facturacion_app
from decimal import Decimal

def decimal_to_float(value):
    if isinstance(value, Decimal):
        return float(value)
    return value

def convert_fields(record):
    for key in record:
        record[key] = decimal_to_float(record[key])
    return record

def ObtenerDetallesFactura():
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Detalle_Factura"
        cursor.execute(query)
        detalles_factura = cursor.fetchall()
        detalles_factura_dict = [dict(zip([column[0] for column in cursor.description], row)) for row in detalles_factura]
        detalles_factura_dict = [convert_fields(detalle) for detalle in detalles_factura_dict]
        Facturacion_app.commit()
        return detalles_factura_dict
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)

def ObtenerDetalleFacturaId(detalle_id):
    try:
        cursor = Facturacion_app.cursor()
        query = "SELECT * FROM Detalle_Factura WHERE detalle_id = %s"
        cursor.execute(query, (detalle_id,))
        detalle_factura = cursor.fetchone()
        Facturacion_app.commit()
        if detalle_factura:
            detalle_factura_dict = dict(zip([column[0] for column in cursor.description], detalle_factura))
            detalle_factura_dict = convert_fields(detalle_factura_dict)
            return detalle_factura_dict
        else:
            return None
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)

def CrearDetalleFactura(detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total):
    try:
        cursor = Facturacion_app.cursor()
        query = "INSERT INTO Detalle_Factura (detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
        cursor.execute(query, (detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total))
        row = cursor.fetchone()
        Facturacion_app.commit()
        if row:
            new_detalle_factura = dict(zip([column[0] for column in cursor.description], row))
            new_detalle_factura = convert_fields(new_detalle_factura)
            return new_detalle_factura
        else:
            return None
    except Exception as e:
        return str(e)

def ActualizarDetalleFactura(detalle_id, factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total):
    try:
        cursor = Facturacion_app.cursor()
        query = "UPDATE Detalle_Factura SET factura_id = %s, producto_id = %s, cantidad = %s, precio_unitario = %s, incluye_iva = %s, porcentaje_iva = %s, subtotal = %s, total = %s WHERE detalle_id = %s RETURNING *"
        cursor.execute(query, (factura_id, producto_id, cantidad, precio_unitario, incluye_iva, porcentaje_iva, subtotal, total, detalle_id))
        row = cursor.fetchone()
        Facturacion_app.commit()
        if row:
            updated_detalle_factura = dict(zip([column[0] for column in cursor.description], row))
            updated_detalle_factura = convert_fields(updated_detalle_factura)
            return updated_detalle_factura
        else:
            return None
    except Exception as e:
        return str(e)

def EliminarDetalleFactura(detalle_id):
    try:
        cursor = Facturacion_app.cursor()
        query = "DELETE FROM Detalle_Factura WHERE detalle_id = %s RETURNING *"
        cursor.execute(query, (detalle_id,))
        row = cursor.fetchone()
        Facturacion_app.commit()
        if row:
            deleted_detalle_factura = dict(zip([column[0] for column in cursor.description], row))
            deleted_detalle_factura = convert_fields(deleted_detalle_factura)
            return deleted_detalle_factura
        else:
            return None
    except Exception as e:
        cursor.execute("ROLLBACK")
        Facturacion_app.commit()
        return str(e)
