def format_hm(seconds):
    """
    Convert seconds → "Hh Mm" format.

    Parameters
    ----------
    seconds : float

    Returns
    -------
    str
        Human-readable duration.
    """

    seconds = float(seconds)
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{hours}h {minutes}m"
