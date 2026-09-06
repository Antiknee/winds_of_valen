from fastapi import FastAPI, HTTPException
import importlib
import io
import sys
import traceback
import pandas as pd

app = FastAPI()

def serialize(value):
    """
    Universal JSON-safe serializer for ANY Python return value.
    """

    # Pandas DataFrame → table format
    if isinstance(value, pd.DataFrame):
        return {
            "type": "dataframe",
            "columns": list(value.columns),
            "rows": value.values.tolist()
        }

    # Pandas Series → list
    if isinstance(value, pd.Series):
        return {
            "type": "series",
            "index": list(value.index),
            "values": value.values.tolist()
        }

    # defaultdict → dict
    if hasattr(value, "items") and not isinstance(value, dict):
        try:
            return {
                "type": "dict",
                "value": dict(value)
            }
        except Exception:
            pass

    # dict → dict
    if isinstance(value, dict):
        return {
            "type": "dict",
            "value": value
        }

    # list or tuple → list
    if isinstance(value, (list, tuple)):
        return {
            "type": "list",
            "value": list(value)
        }

    # primitive types
    if isinstance(value, (str, int, float, bool)) or value is None:
        return {
            "type": "primitive",
            "value": value
        }

    # fallback: string representation
    return {
        "type": "string",
        "value": str(value)
    }


@app.get("/api/run_function")
def run_function(name: str):
    """
    Dynamically load and execute ANY function inside winds_of_valen/functions or pipelines.
    Returns JSON-safe debug output.
    """

    debug = {
        "function": name,
        "stdout": "",
        "return": None,
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

        # Serialize return value
        debug["return"] = serialize(result)

        return debug

    except Exception as e:
        sys.stdout = real_stdout
        debug["stdout"] = buffer.getvalue()
        debug["error"] = str(e)
        debug["traceback"] = traceback.format_exc()
        return debug
