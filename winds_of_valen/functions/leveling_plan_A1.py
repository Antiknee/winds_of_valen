"""
leveling_plan_A1.py

Generate a full leveling plan from current XP → target level.
"""

import numpy as np

from winds_of_valen.global_dicts.exp_table import exp_table
from winds_of_valen.global_dicts.level_req import level_req

from winds_of_valen.functions.resolve_chain import resolve_chain
from winds_of_valen.functions.smelting_item_flags import is_smelting_item
from winds_of_valen.functions.LevelWhenXP import LevelWhenXP


def leveling_plan_A1(current_xp: int, target_level: int, df_smelting):
    plan = []
    current_level = LevelWhenXP(current_xp)

    while current_level < target_level:
        next_level = current_level + 1
        xp_needed = exp_table[next_level] - current_xp

        best = df_smelting.loc[df_smelting["chain_efficiency"].idxmax()]
        item_name = best["item"]

        chain_info = resolve_chain(item_name, qty=1)
        exp_per_item = chain_info["total_smithing_exp"]
        time_per_item = chain_info["total_time"]

        cycles = int(np.ceil(xp_needed / exp_per_item))
        exp_gained = cycles * exp_per_item
        total_time = cycles * time_per_item

        total_materials = {
            mat: qty * cycles for mat, qty in chain_info["materials"].items()
        }

        # intermediate smelting steps
        for mat, qty in chain_info["materials"].items():
            if is_smelting_item(mat):
                plan.append({
                    "from_level": current_level,
                    "to_level": next_level,
                    "item": mat,
                    "cycles": qty * cycles,
                    "exp_gained": exp_table.get(mat, 0) * qty * cycles,
                    "materials": resolve_chain(mat, qty * cycles)["materials"],
                    "time_seconds": resolve_chain(mat, qty * cycles)["total_time"],
                })

        # final craft step
        plan.append({
            "from_level": current_level,
            "to_level": next_level,
            "item": item_name,
            "cycles": cycles,
            "exp_gained": exp_gained,
            "materials": total_materials,
            "time_seconds": total_time,
        })

        current_xp += exp_gained
        current_level = next_level

    return plan
