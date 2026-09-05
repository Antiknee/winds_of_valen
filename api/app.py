from fastapi import FastAPI
from winds_of_valen.app import build_smelting_df, build_plan_df

app = FastAPI()

@app.get("/")
def root():
    df_smelting = build_smelting_df()
    df_planA1 = build_plan_df()

    return {
        "status": "ok",
        "smelting_rows": len(df_smelting),
        "plan_rows": len(df_planA1)
    }
