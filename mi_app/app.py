import web
from controllers.index import Index as Index
from controllers.opciones import Opciones as Opciones
from controllers.targeta_Uno import TargetaUno as TargetaUno

urls = (
    "/", "Index",
    "/Opciones", "Opciones", 
    "/targetaUno", "TargetaUno", 
    "/targetasDos", "targetasDos"
)

app = web.application(urls, globals()) 


def error_handler():
    return web.internalerror("Ocurrió un error en el servidor. Intenta nuevamente.")

if __name__ == "__main__":
    app.run()
