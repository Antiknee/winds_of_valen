from fastapi import FastAPI, HTTPException
import importlib

app = FastAPI()

@app.get("/api/run_function")
def run_function(name: str):
    """
    Dynamically load and execute any function inside winds_of_valen/functions or pipelines.
    Example:
      /api/run_function?name=resolve_chain
      /api/run_function?name=smelting_dataframe
    """

    # Try functions folder
    try:
        module = importlib.import_module(f"winds_of_valen.functions.{name}")
    except ModuleNotFoundError:
        # Try pipelines folder
        try:
            module = importlib.import_module(f"winds_of_valen.functions.pipelines.{name}")
        except ModuleNotFoundError:
            raise HTTPException(status_code=404, detail=f"Function '{name}' not found")

    # Find a callable with the same name as the module
    if hasattr(module, name):
        func = getattr(module, name)
    else:
        raise HTTPException(status_code=400, detail=f"Module '{name}' has no function '{name}'")

    # Execute the function
    try:
        result = func()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Convert result to JSON-friendly format
    if isinstance(result, (dict, list, str, int, float, bool)):
        return {"result": result}

    return {"result": str(result)}
