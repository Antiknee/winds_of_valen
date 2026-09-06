from fastapi import FastAPI, HTTPException
import importlib
import io
import sys
import traceback
import json

app = FastAPI()

@app.get("/api/run_function")
def run_function(name: str):
    """
    Dynamically load and execute any function inside winds_of_valen/functions or pipelines.
    Returns full debug info so the frontend can display errors and raw output.
    """

    debug = {
        "function": name,
        "stdout": "",
        "return_type": "",
        "return_value": "",
        "error": "",
        "traceback": ""
    }

    # Capture stdout
    buffer = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = buffer

    try:
        # Try functions folder
        try:
            module = importlib.import_module(f"winds_of_valen.functions.{name}")
        except ModuleNotFoundError:
            # Try pipelines folder
            module = importlib.import_module(f"winds_of_valen.functions.pipelines.{name}")

        if not hasattr(module, name):
            raise AttributeError(f"Module '{name}' has no function '{name}'")

        func = getattr(module, name)

        # Execute function
        result = func()

        # Restore stdout
        sys.stdout = real_stdout
        debug["stdout"] = buffer.getvalue()

        # Return type
        debug["return_type"] = str(type(result))

        # Try JSON serialization
        try:
            json.dumps(result)
            debug["return_value"] = result
        except Exception:
            debug["return_value"] = str(result)

        return debug

    except Exception as e:
        sys.stdout = real_stdout
        debug["stdout"] = buffer.getvalue()
        debug["error"] = str(e)
        debug["traceback"] = traceback.format_exc()
        return debug
