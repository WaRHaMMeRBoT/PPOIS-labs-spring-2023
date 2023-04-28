def clamp(val, min_val, max_val):
    return min(max(min_val, val), max_val)

def is_clamp(*args):
    return clamp(*args) == args[0]
