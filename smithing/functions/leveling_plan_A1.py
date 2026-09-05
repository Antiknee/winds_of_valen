import numpy as np

from smithing.dictionaries.exp_table import xp_table
from smithing.dictionaries.level_req import level_req
from smithing.functions.resolve_chain import resolve_chain
from smithing.functions.is_smelting_item import is_smelting_item
from smithing.functions.immediate_recipe_totals import immediate_recipe_totals
from smithing.functions.best_item_for_level_chain import best_item_for_level_chain
from smithing.functions.format_hm import format_hm
from smithing.functions.resolve_time import resolve_time
from smithing.functions.resolve import resolve
from smithing.functions.is_stackable import is_stackable
from smithing.functions.tier_efficiency import tier_efficiency
from smithing.functions.classify import classify
from smithing.functions.resolve_time import resolve_time
from smithing.functions.resolve_chain import resolve_chain
from smithing.functions.format_hm import format_hm
from smithing.functions.LevelWhenXP import LevelWhenXP


def leveling_plan_A1(current_xp, target_level, df_smelting):
    plan = []
    current_level = LevelWhenXP(current_xp)

    while current_level < target_level:
        next_level = current_level + 1
        xp_needed = xp_table[next_level] - current_xp

        best = best_item_for_level_chain(current_level, df_smelting)
        if best is None:
            break

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

        for mat, qty in chain_info["materials"].items():
            if is_smelting_item(mat):
                plan.append({
                    "from_level": current_level,
                    "to_level": next_level,
                    "item": mat,
                    "cycles": qty * cycles,
                    "exp_gained": xp_table.get(mat, 0) * qty * cycles,
                    "materials": resolve_chain(mat, qty * cycles)["materials"],
                    "time_seconds": resolve_chain(mat, qty * cycles)["total_time"],
                })

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
