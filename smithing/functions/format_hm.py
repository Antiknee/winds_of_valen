"""
format_hm.py

Convert seconds → "Hh Mm" format.

Parameters
----------
seconds : float

Returns
-------
str
    Human-readable duration.
"""

def format_hm(seconds: float) -> str:
    seconds = float(seconds)
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}h {minutes}m"
