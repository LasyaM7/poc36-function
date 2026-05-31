import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}.")
    else:
        return func.HttpResponse("Function executed successfully")
