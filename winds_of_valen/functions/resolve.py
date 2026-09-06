"""
resolve.py

Resolve an item into:
- its immediate recipe
- raw materials required (recursive)
- smithing XP for the recipe
- mining XP for raw materials
- recursive smithing XP for all subcomponents
- total smithing XP
- full dependency chain
"""

from winds_of_valen.global_dicts.global_data import global_data
full_recipes = global_data["full_recipes"]
from winds_of_valen.global_dicts.skill_exp_table import skill_exp_table
from winds_of_valen.global_dicts.mining_exp import mining_exp
from winds_of_valen.global_dicts.global_data import global_data
raw_items = global_data["raw_items"]


def resolve(item: str, qty: int = 1) -> dict:
    """
    Resolve an item into its full crafting breakdown.

    Parameters
    ----------
    item : str
        Item name to resolve.
    qty : int
        Quantity of the item.

    Returns
    -------
    dict
        {
            "recipe": immediate recipe,
            "raw_materials": raw materials only,
            "recipe_exp": smithing XP for final craft,
            "raw_materials_exp": mining XP,
            "recursive_smithing_exp": XP from intermediates,
            "total_smithing_exp": total XP,
            "chain": full dependency chain
        }
    """

    recipe = full_recipes.get(item, [])
    raw_materials = {}
    chain = []

    recursive_smithing_exp = 0
    raw_mining_exp = 0

    def expand(name: str, count: int):
        nonlocal recursive_smithing_exp, raw_mining_exp

        chain.append((name, count))

        # smithing XP for intermediate crafts (exclude final craft)
        if name in skill_exp_table and name != item:
            recursive_smithing_exp += skill_exp_table[name] * count

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

    recipe_exp = skill_exp_table.get(item, 0)
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

