"""
immediate_recipe_totals.py

Compute totals of immediate recipe components for a given number of cycles.
Does NOT recurse.
"""

from winds_of_valen.global_dicts.full_recipes import full_recipes


def immediate_recipe_totals(item: str, cycles: int) -> dict:
    totals = {}
    for ing in full_recipes.get(item, []):
        totals[ing["name"]] = ing["count"] * cycles
    return totals
