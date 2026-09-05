from smithing.functions.immediate_recipe_totals import immediate_recipe_totals
from smithing.functions.format_hm import format_hm

def aggregate_plan_global(plan):
    aggregated = {}

    for step in plan:
        item = step["item"]

        if item not in aggregated:
            aggregated[item] = {
                "item": item,
                "start_level": step["from_level"],
                "end_level": step["to_level"],
                "total_cycles": 0,
                "total_exp": 0,
                "total_time_seconds": 0,
                "materials": {},
                "immediate_recipe_totals": {},
                "total_output": 0
            }
        else:
            aggregated[item]["end_level"] = step["to_level"]

        aggregated[item]["total_cycles"] += step["cycles"]
        aggregated[item]["total_exp"] += step["exp_gained"]
        aggregated[item]["total_time_seconds"] += step["time_seconds"]

        for mat, qty in step["materials"].items():
            aggregated[item]["materials"][mat] = (
                aggregated[item]["materials"].get(mat, 0) + qty
            )

        imm = immediate_recipe_totals(item, step["cycles"])
        for mat, qty in imm.items():
            aggregated[item]["immediate_recipe_totals"][mat] = (
                aggregated[item]["immediate_recipe_totals"].get(mat, 0) + qty
            )

        aggregated[item]["total_output"] += step["cycles"]

    for block in aggregated.values():
        block["time_hm"] = format_hm(block["total_time_seconds"])
        block["materials"] = ", ".join(f"{k}: {v}" for k, v in block["materials"].items())
        block["immediate_recipe_totals"] = ", ".join(
            f"{k}: {v}" for k, v in block["immediate_recipe_totals"].items()
        )

    return list(aggregated.values())
