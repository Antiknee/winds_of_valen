"""
usage_graph.py

Build a reverse dependency graph mapping:
    ingredient → list of (product, count)

This allows you to see:
- which items depend on a given ingredient
- how many units of that ingredient each product requires
- global usage trees for visualization or reporting
"""

from collections import defaultdict
from winds_of_valen.global_dicts.full_recipes import full_recipes


def build_usage_graph():
    """
    Build a reverse dependency graph mapping:
        ingredient → list of (product, count)

    Returns
    -------
    dict[str, list[tuple[str, int]]]
        Mapping ingredient → list of (product, count)
    """
    uses = defaultdict(list)

    for product, recipe in full_recipes.items():
        for ing in recipe:
            uses[ing["name"]].append((product, ing["count"]))

    return uses


# Precompute global usage graph
uses_graph = build_usage_graph()
