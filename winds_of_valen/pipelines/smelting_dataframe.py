"""
smelting_dataframe.py

Generates a full smelting efficiency table for all craftable items.
Returns JSON‑serializable dicts instead of pandas DataFrames.
"""

from winds_of_valen.global_dicts.global_data import global_data
item_recipes = global_data["item_recipes"]
from winds_of_valen.global_dicts.global_data import global_data
material_breakdown_recipes = global_data["material_breakdown_recipes"]
from winds_of_valen.global_dicts.global_data import global_data
craft_time = global_data["craft_time"]

from winds_of_valen.functions.resolve import resolve
from winds_of_valen.functions.resolve_time import resolve_time
from winds_of_valen.functions.stackable import is_stackable
from winds_of_valen.functions.format_hm import format_hm
from winds_of_valen.functions.tier_efficiency import tier_efficiency


def build_smelting_dataframe():
    """
    Returns
    -------
    dict
        {
            "sorted": {
                "columns": [...],
                "rows": [...]
            },
            "unsorted": {
                "columns": [...],
                "rows": [...]
            }
        }
    """

    records = []

    df_items = list(item_recipes.keys()) + list(material_breakdown_recipes.keys())

    for item in df_items:
        r = resolve(item)

        # compute slot cost
        slot_cost = 0
        for ing in r["recipe"]:
            slot_cost += 1 if is_stackable(ing["name"]) else ing["count"]

        per_run = 28 // slot_cost if slot_cost > 0 else 0

        # focused run recipe
        focused_run_recipe = [
            {"name": ing["name"], "count": ing["count"] * per_run}
            for ing in r["recipe"]
        ]

        # focused EXP
        focused_run_exp = per_run * r["recipe_exp"]

        # focused time (immediate recipe only)
        focused_time_per_item = craft_time.get(item, 0)
        smelt_cycle_duration = focused_time_per_item * per_run

        # focused efficiency
        efficiency_focused_time = (
            focused_run_exp / smelt_cycle_duration
            if smelt_cycle_duration > 0 else 0
        )

        # full-chain time
        total_time_per_recipe = resolve_time(item)
        full_chain_time_per_run = total_time_per_recipe * per_run

        # full-chain EXP
        full_chain_exp_per_run = per_run * r["total_smithing_exp"]

        # full-chain efficiency
        efficiency_chain = (
            full_chain_exp_per_run / full_chain_time_per_run
            if full_chain_time_per_run > 0 else 0
        )

        # time to reach 10 million EXP (focused)
        time_to_10m_cycle = (
            (10_000_000 / focused_run_exp) * smelt_cycle_duration
            if focused_run_exp > 0 else float("inf")
        )

        # time to reach 10 million EXP (full chain)
        time_to_10m_chain = (
            (10_000_000 / full_chain_exp_per_run) * full_chain_time_per_run
            if full_chain_exp_per_run > 0 else float("inf")
        )

        time_to_10m_chain_hm = format_hm(time_to_10m_chain)
        time_to_10m_cycle_hm = format_hm(time_to_10m_cycle)

        records.append({
            "item": item,
            "recipe": r["recipe"],
            "raw_materials": r["raw_materials"],

            "recipe_exp": r["recipe_exp"],
            "recipe_chain_exp": r["recursive_smithing_exp"],
            "recipe_total_exp": r["total_smithing_exp"],

            "bag_slot_cost": slot_cost,
            "bag_total_per_run": per_run,

            "smelt_cycle_materials": focused_run_recipe,
            "smelt_cycle_exp": focused_run_exp,
            "smelt_cycle_duration": smelt_cycle_duration,
            "smelt_chain_duration": total_time_per_recipe,

            "cycle_efficiency": round(efficiency_focused_time, 1),
            "chain_efficiency": round(efficiency_chain, 1),

            "cycle_10m_xp": time_to_10m_cycle_hm,
            "chain_10m_xp": time_to_10m_chain_hm,

            "cycle_tier": tier_efficiency(round(efficiency_focused_time, 1)),
            "chain_tier": tier_efficiency(round(efficiency_chain, 1)),
        })

    # Build columns list
    columns = list(records[0].keys()) if records else []

    # Unsorted table
    unsorted_rows = [
        [rec[col] for col in columns]
        for rec in records
    ]

    # Sorted table (by cycle_efficiency desc)
    sorted_records = sorted(records, key=lambda r: r["cycle_efficiency"], reverse=True)
    sorted_rows = [
        [rec[col] for col in columns]
        for rec in sorted_records
    ]

    return {
        "sorted": {
            "columns": columns,
            "rows": sorted_rows
        },
        "unsorted": {
            "columns": columns,
            "rows": unsorted_rows
        }
    }

