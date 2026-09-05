"""
print_global_forest.py

Print usage forests for all bar types:
    Bronze, Iron, Steel, Mithril, Silver, Gold

Uses:
- global_totals (full material usage)
- print_usage_tree (recursive usage printer)
"""

from winds_of_valen.pipelines.global_material_totals import build_global_material_totals
from winds_of_valen.functions.print_usage_tree import print_usage_tree


# Precompute global totals once
global_totals, _ = build_global_material_totals()


def print_global_forest():
    """
    Print usage forests for all bar types.
    """

    # Bronze
    bronze_bars = global_totals.get("Bronze Bar", 0)
    if bronze_bars > 0:
        print("\n=== BRONZE CHAIN ===")
        print(f"Copper Ore × {bronze_bars * 1}  &  Tin Ore × {bronze_bars * 1}")
        print_usage_tree("Bronze Bar")

    # Iron
    iron_bars = global_totals.get("Iron Bar", 0)
    if iron_bars > 0:
        print("\n=== IRON CHAIN ===")
        print(f"Iron Ore × {iron_bars * 2}")
        print_usage_tree("Iron Bar")

    # Steel
    steel_bars = global_totals.get("Steel Bar", 0)
    if steel_bars > 0:
        print("\n=== STEEL CHAIN ===")
        print(f"Iron Ore × {steel_bars * 1}  &  Coal Ore × {steel_bars * 1}")
        print_usage_tree("Steel Bar")

    # Mithril
    mithril_bars = global_totals.get("Mithril Bar", 0)
    if mithril_bars > 0:
        print("\n=== MITHRIL CHAIN ===")
        print(f"Mithril Ore × {mithril_bars * 1}  &  Coal Ore × {mithril_bars * 2}")
        print_usage_tree("Mithril Bar")

    # Silver
    silver_bars = global_totals.get("Silver Bar", 0)
    if silver_bars > 0:
        print("\n=== SILVER CHAIN ===")
        print(f"Silver Ore × {silver_bars * 7}")
        print_usage_tree("Silver Bar")

    # Gold
    gold_bars = global_totals.get("Gold Bar", 0)
    if gold_bars > 0:
        print("\n=== GOLD CHAIN ===")
        print(f"Gold Ore × {gold_bars * 8}")
        print_usage_tree("Gold Bar")
