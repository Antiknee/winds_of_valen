"""
raw_items.py

Set of items considered raw mining materials.
These generate mining XP and terminate recursion in resolve_chain().
"""

raw_items: set[str] = {
    "Copper Ore",
    "Tin Ore",
    "Iron Ore",
    "Coal Ore",
    "Mithril Ore",
    "Silver Ore",
    "Gold Ore",
    # "Ebony Ore",
}
