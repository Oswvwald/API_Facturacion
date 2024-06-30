from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

#importe de rutas
from routes.tipoPago_routes import appTipoPago
from routes.clientes_routes import appClientes
from routes.facturas_routes import appFacturas
from routes.detalleFactura_routes import appDetalleFactura

app = FastAPI()

#configuracion de cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#rutas
app.include_router(appTipoPago)
app.include_router(appClientes)
app.include_router(appFacturas)
app.include_router(appDetalleFactura)

#levantar servidor 
if __name__ == "__main__":
    uvicorn.run( 'app:app', host='0.0.0.0', port=3000, reload=True)