import web

render = web.template.render("views", base="master")

class TargetaUno:
    def GET(self):
        try:
            return render.targetauno()
        except Exception as error:
            message = {
                "Error": str(error)
            }
            print(f"ERROR: {message}")  
            return message


