"""
classify.py

Classify an item into:
- Bar
- Intermediate item
- Final Item

Classification is based on simple name patterns:
    "Bar", "Plate", "Rod", "Large"
"""

def classify(item: str) -> str:
    if "Bar" in item:
        return "Bar"
    if "Plate" in item and "Large" in item:
        return "Intermediate item"
    if "Plate" in item:
        return "Intermediate item"
    if "Rod" in item and "Large" in item:
        return "Intermediate item"
    if "Rod" in item:
        return "Intermediate item"
    return "Final Item"
