"""
raw_material_summary.py

Generate a summary of total raw materials required for a full
leveling plan (e.g., Option A1).

This module extracts ONLY raw materials from each step's
full recursive material list.
"""

import pandas as pd

from winds_of_valen.pipelines.smelting_dataframe import build_smelting_dataframe
from winds_of_valen.functions.leveling_plan_A1 import leveling_plan_A1
from winds_of_valen.global_dicts.raw_items import raw_items


def build_raw_material_summary(
    start_xp: int = 1,
    target_level: int = 60
):
    """
    Build a DataFrame summarizing total raw materials required
    for the full leveling plan.

    Parameters
    ----------
    start_xp : int
        Starting smithing XP.
    target_level : int
        Target smithing level.

    Returns
    -------
    pandas.DataFrame
        Columns:
            raw_material
            total_required
    """

    # Build smelting dataframe
    df, df_smelting = build_smelting_dataframe()

    # Run leveling plan
    planA1_raw = leveling_plan_A1(start_xp, target_level, df_smelting)

    raw_totals = {}

    # Accumulate raw materials only
    for step in planA1_raw:
        for mat, qty in step["materials"].items():
            if mat in raw_items:
                raw_totals[mat] = raw_totals.get(mat, 0) + qty

    summary_rows = [
        {"raw_material": mat, "total_required": qty}
        for mat, qty in raw_totals.items()
    ]

    df_raw_summary = pd.DataFrame(summary_rows)
    return df_raw_summary
