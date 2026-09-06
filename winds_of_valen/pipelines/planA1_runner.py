"""
planA1_runner.py

Runs Option A1 end‑to‑end and produces df_planA1.
"""

import pandas as pd

from winds_of_valen.pipelines.smelting_dataframe import build_smelting_dataframe
from winds_of_valen.functions.leveling_plan_A1 import leveling_plan_A1
from winds_of_valen.functions.aggregate_plan_global import aggregate_plan_global


def planA1_runner(start_xp: int = 1, target_level: int = 60):
    """
    Run the full A1 leveling plan and return JSON‑serializable table data.

    Returns
    -------
    dict
        {
            "columns": [...],
            "rows": [...]
        }
    """

    # Build smelting dataframe
    df, df_smelting = build_smelting_dataframe()

    # Run A1 leveling plan
    planA1_raw = leveling_plan_A1(start_xp, target_level, df_smelting)
    planA1 = aggregate_plan_global(planA1_raw)

    # Convert to DataFrame
    df_planA1 = pd.DataFrame(planA1)

    # Convert DataFrame → JSON table
    return {
        "columns": list(df_planA1.columns),
        "rows": df_planA1.values.tolist()
    }
