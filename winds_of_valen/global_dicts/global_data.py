"""
full_recipes.py

Merged dictionary combining:
- material_breakdown_recipes
- item_recipes

Used as the unified lookup table for all crafting resolution.
"""

from winds_of_valen.global_dicts.global_data import global_data
material_breakdown_recipes = global_data["material_breakdown_recipes"]
from winds_of_valen.global_dicts.global_data import global_data
item_recipes = global_data["item_recipes"]

full_recipes: dict[str, list[dict]] = {
    **material_breakdown_recipes,
    **item_recipes,
}

