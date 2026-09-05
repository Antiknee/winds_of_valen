from winds_of_valen.app import df_smelting, df_planA1

def handler(request):
    return {
        "status": "ok",
        "smelting_rows": len(df_smelting),
        "plan_rows": len(df_planA1)
    }
