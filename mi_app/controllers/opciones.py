import web

render = web.template.render("views", base="master")

class Opciones:
    def GET(self):
        try:
            return render.opciones()
        except Exception as error:
            message = {
                "Error": str(error)
            }
            print(f"ERROR: {message}")  
            return message

