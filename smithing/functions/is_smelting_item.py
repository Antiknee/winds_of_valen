from smithing.dictionaries.recipes_material import material_breakdown_recipes
from smithing.dictionaries.recipes_item import item_recipes

def is_smelting_item(name: str) -> bool:
    return name in material_breakdown_recipes or name in item_recipes
