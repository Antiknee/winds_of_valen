"""
resolve.py

Resolves an item into:
- its immediate recipe
- raw materials required (recursive)
- smithing XP for the recipe
- mining XP for raw materials
- recursive smithing XP for all subcomponents
- total smithing XP
- full dependency chain
"""

from smithing.dictionaries.full_recipes import full_recipes
from smithing.dictionaries.exp_table import exp_table
from smithing.dictionaries.mining_exp import mining_exp
from smithing.dictionaries.raw_items import raw_items


def resolve(item: str, qty: int = 1) -> dict:
    recipe = full_recipes.get(item, [])
    raw_materials = {}
    chain = []

    recursive_smithing_exp = 0
    raw_mining_exp = 0

    def expand(name: str, count: int):
        nonlocal recursive_smithing_exp, raw_mining_exp

        chain.append((name, count))

        # smithing XP for intermediate crafts (exclude final craft)
        if name in exp_table and name != item:
            recursive_smithing_exp += exp_table[name] * count

        # mining XP for raw materials
        if name in mining_exp:
            raw_mining_exp += mining_exp[name] * count

        # lowest-tier raw material
        if name in raw_items:
            raw_materials[name] = raw_materials.get(name, 0) + count
            return

        # crafted component: recurse into its recipe
        for ing in full_recipes.get(name, []):
            expand(ing["name"], ing["count"] * count)

    expand(item, qty)

    recipe_exp = exp_table.get(item, 0)
    total_smithing_exp = recipe_exp + recursive_smithing_exp

    return {
        "recipe": recipe,
        "raw_materials": raw_materials,
        "recipe_exp": recipe_exp,
        "raw_materials_exp": raw_mining_exp,
        "recursive_smithing_exp": recursive_smithing_exp,
        "total_smithing_exp": total_smithing_exp,
        "chain": chain,
    }
