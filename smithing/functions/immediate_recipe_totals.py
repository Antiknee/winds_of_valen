from smithing.dictionaries.full_recipes import full_recipes

def immediate_recipe_totals(item: str, cycles: int) -> dict:
    totals = {}
    for ing in full_recipes.get(item, []):
        totals[ing["name"]] = ing["count"] * cycles
    return totals
