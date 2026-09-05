"""
global_material_totals.py

Compute total usage of ALL materials (raw + intermediates + final items)
across a full leveling plan.

This includes:
- cycles of each crafted item
- all recursive materials used in each step
"""

import pandas as pd
from collections import defaultdict

from winds_of_valen.pipelines.smelting_dataframe import build_smelting_dataframe
from winds_of_valen.functions.leveling_plan_A1 import leveling_plan_A1


def build_global_material_totals(
    start_xp: int = 1,
    target_level: int = 60
):
    """
    Compute global material usage across the full leveling plan.

    Parameters
    ----------
    start_xp : int
        Starting smithing XP.
    target_level : int
        Target smithing level.

    Returns
    -------
    dict
        Mapping material → total quantity used.
    pandas.DataFrame
        Tabular representation of the totals.
    """

    # Build smelting dataframe
    df, df_smelting = build_smelting_dataframe()

    # Run leveling plan
    planA1_raw = leveling_plan_A1(start_xp, target_level, df_smelting)

    global_totals = defaultdict(int)

    for step in planA1_raw:
        # count the crafted item itself
        global_totals[step["item"]] += step["cycles"]

        # count all materials used in its full chain
        for mat, qty in step["materials"].items():
            global_totals[mat] += qty

    # Convert to DataFrame
    rows = [
        {"material": mat, "total_required": qty}
        for mat, qty in global_totals.items()
    ]

    df_global = pd.DataFrame(rows)

    return global_totals, df_global
