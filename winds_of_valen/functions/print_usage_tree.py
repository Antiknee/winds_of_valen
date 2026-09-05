"""
print_usage_tree.py

Pretty‑print a global usage tree for any item.

Features:
- avoids infinite recursion
- skips zero‑count items entirely
- prints quantities from global_totals
- uses the reverse dependency graph (uses_graph)
"""

from winds_of_valen.pipelines.global_material_totals import build_global_material_totals
from winds_of_valen.functions.usage_graph import uses_graph


# Precompute global totals once
global_totals, _ = build_global_material_totals()


def print_usage_tree(item: str, indent: str = "", seen=None):
    """
    Print a global usage tree for an item.

    Parameters
    ----------
    item : str
        The item whose usage tree to print.
    indent : str
        Indentation for nested levels.
    seen : set
        Tracks visited nodes to avoid recursion loops.
    """

    if seen is None:
        seen = set()

    qty = global_totals.get(item, 0)
    if qty == 0:
        return  # skip zero-count items entirely

    if item in seen:
        print(f"{indent}↳ {item} (recursive)")
        return
    seen.add(item)

    print(f"{indent}{item} × {qty}")

    children = uses_graph.get(item, [])
    if not children:
        return

    next_indent = indent + "    "
    for product, _ in children:
        # Only print children with non-zero totals
        if global_totals.get(product, 0) > 0:
            print_usage_tree(product, next_indent, seen.copy())
