from fastapi import FastAPI
from winds_of_valen.app import df_smelting, df_planA1

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "smelting_rows": len(df_smelting),
        "plan_rows": len(df_planA1)
    }
