"""
level_req.py

Minimum smithing level required to craft each item.

Used by:
- best_item_for_level()
- best_item_for_level_chain()
- leveling_plan_A1()
"""

level_req: dict[str, int] = {
    "Bronze Bar": 1,
    "Iron Bar": 10,
    "Steel Bar": 20,
    "Mithril Bar": 30,
    "Gold Bar": 40,
    "Silver Bar": 40,

    "Bronze Sword": 2,
    "Bronze Platelegs": 4,
    "Bronze Platebody": 6,
    "Bronze Helmet": 8,

    "Iron Sword": 12,
    "Iron Platelegs": 14,
    "Iron Platebody": 16,
    "Iron Helmet": 18,

    "Steel Sword": 22,
    "Steel Platelegs": 24,
    "Steel Platebody": 26,
    "Steel Helmet": 28,

    "Mithril Sword": 32,
    "Mithril Platelegs": 34,
    "Mithril Platebody": 36,
    "Mithril Helmet": 38,

    "Iron Plate": 10,
    "Iron Rod": 11,
    "Steel Plate": 20,
    "Steel Rod": 21,
    "Large Steel Plate": 21,
    "Large Steel Rod": 23,
    "Mithril Plate": 30,
    "Mithril Rod": 31,
    "Large Mithril Plate": 31,
    "Large Mithril Rod": 33,

    "Silver Plate": 40,
    "Silver Foil": 45,

    "Gold Plate": 40,
    "Golden Shield Frame": 50,
}
