import azure.functions as func

app = func.FunctionApp()

@app.route(route="HttpTrigger1", auth_level=func.AuthLevel.ANONYMOUS)
def HttpTrigger1(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string for a personalized response."
        )
