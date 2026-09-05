"""
levelpath_builder.py

Builds a detailed per‑step leveling path from the A1 leveling plan
and exports it to levelpath.csv.

Each row includes:
- item crafted
- levels gained
- cycles
- EXP gained
- time (seconds + formatted)
- full‑chain materials
- immediate recipe totals
"""

import pandas as pd

from winds_of_valen.pipelines.smelting_dataframe import build_smelting_dataframe
from winds_of_valen.functions.leveling_plan_A1 import leveling_plan_A1
from winds_of_valen.functions.immediate_recipe_totals import immediate_recipe_totals
from winds_of_valen.functions.format_hm import format_hm


def build_levelpath_csv(
    start_xp: int = 1,
    target_level: int = 60,
    output_path: str = "levelpath.csv"
):
    """
    Generate the full levelpath CSV for a leveling run.

    Parameters
    ----------
    start_xp : int
        Starting smithing XP.
    target_level : int
        Target smithing level.
    output_path : str
        CSV file path to write.
    """

    # Build smelting dataframe
    df, df_smelting = build_smelting_dataframe()

    # Run A1 leveling plan
    planA1_raw = leveling_plan_A1(start_xp, target_level, df_smelting)

    rows = []

    for step in planA1_raw:
        item = step["item"]
        cycles = step["cycles"]

        imm = immediate_recipe_totals(item, cycles)

        rows.append({
            "item": item,
            "from_level": step["from_level"],
            "to_level": step["to_level"],
            "total_cycles": cycles,
            "total_exp": step["exp_gained"],
            "total_time_seconds": step["time_seconds"],
            "materials": ", ".join(f"{k}: {v}" for k, v in step["materials"].items()),
            "immediate_recipe_totals": ", ".join(f"{k}: {v}" for k, v in imm.items()),
            "total_output": cycles,
            "time_hm": format_hm(step["time_seconds"]),
        })

    df_path = pd.DataFrame(rows)
    # df_path.to_csv(output_path, index=False)

    return df_path
