"""
full_recipes.py

Merged dictionary combining:
- material_breakdown_recipes
- item_recipes

Used as the unified lookup table for all crafting resolution.
"""

from winds_of_valen.global_dicts.material_breakdown_recipes import material_breakdown_recipes
from winds_of_valen.global_dicts.item_recipes import item_recipes

full_recipes: dict[str, list[dict]] = {
    **material_breakdown_recipes,
    **item_recipes,
}
