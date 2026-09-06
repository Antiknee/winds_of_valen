import pandas as pd
import numpy as np

# --- dictionaries ---
from smithing.dictionaries.recipes_item import item_recipes
from smithing.dictionaries.recipes_material import material_breakdown_recipes
from smithing.dictionaries.craft_time import craft_time
from smithing.dictionaries.level_req import level_req
from smithing.dictionaries.exp_table import xp_table

# --- engine functions ---
from smithing.functions.resolve import resolve
from smithing.functions.resolve_time import resolve_time
from smithing.functions.is_stackable import is_stackable
from smithing.functions.format_hm import format_hm
from smithing.functions.tier_efficiency import tier_efficiency
from smithing.functions.resolve_chain import resolve_chain
from smithing.functions.is_smelting_item import is_smelting_item
from smithing.functions.immediate_recipe_totals import immediate_recipe_totals
from smithing.functions.best_item_for_level_chain import best_item_for_level_chain
from smithing.functions.leveling_plan_A1 import leveling_plan_A1
from smithing.functions.aggregate_plan_global import aggregate_plan_global
from smithing.functions.LevelWhenXP import LevelWhenXP


def build_smelting_df():
    records = []
    df_items = list(item_recipes.keys()) + list(material_breakdown_recipes.keys())

    for item in df_items:
        r = resolve(item)

        slot_cost = sum(
            1 if is_stackable(ing["name"]) else ing["count"]
            for ing in r["recipe"]
        )

        per_run = 28 // slot_cost if slot_cost > 0 else 0

        focused_run_recipe = [
            {"name": ing["name"], "count": ing["count"] * per_run}
            for ing in r["recipe"]
        ]

        focused_run_exp = per_run * r["recipe_exp"]
        focused_time_per_item = craft_time.get(item, 0)
        smelt_cycle_duration = focused_time_per_item * per_run

        efficiency_focused_time = (
            focused_run_exp / smelt_cycle_duration
            if smelt_cycle_duration > 0 else 0
        )

        total_time_per_recipe = resolve_time(item)
        full_chain_time_per_run = total_time_per_recipe * per_run
        full_chain_exp_per_run = per_run * r["total_smithing_exp"]

        efficiency_chain = (
            full_chain_exp_per_run / full_chain_time_per_run
            if full_chain_time_per_run > 0 else 0
        )

        time_to_10m_cycle = (
            (10_000_000 / focused_run_exp) * smelt_cycle_duration
            if focused_run_exp > 0 else float("inf")
        )

        time_to_10m_chain = (
            (10_000_000 / full_chain_exp_per_run) * full_chain_time_per_run
            if full_chain_exp_per_run > 0 else float("inf")
        )

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
            "cycle_10m_xp": format_hm(time_to_10m_cycle),
            "chain_10m_xp": format_hm(time_to_10m_chain),
            "cycle_tier": tier_efficiency(round(efficiency_focused_time, 1)),
            "chain_tier": tier_efficiency(round(efficiency_chain, 1)),
        })

    df = pd.DataFrame(records)
    return df.sort_values(by="cycle_efficiency", ascending=False)


def build_plan_df():
    df_smelting = build_smelting_df()
    planA1_raw = leveling_plan_A1(1, 60, df_smelting)
    planA1 = aggregate_plan_global(planA1_raw)
    return pd.DataFrame(planA1)
