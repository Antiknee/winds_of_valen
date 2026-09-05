"""
full_recipes.py

Unified crafting recipe dictionary combining:
- material_breakdown_recipes (intermediate materials)
- item_recipes (final items)

Used by resolve(), resolve_chain(), immediate_recipe_totals(),
build_usage_graph(), print_usage_tree(), and print_global_forest().
"""

from smithing.dictionaries.recipes_material import material_breakdown_recipes
from smithing.dictionaries.recipes_item import item_recipes

full_recipes: dict[str, list[dict]] = {
    **material_breakdown_recipes,
    **item_recipes,
}
