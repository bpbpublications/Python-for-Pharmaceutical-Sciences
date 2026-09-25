# pharmacy_utils.py

def calculate_concentration(amount_mg, volume_ml):
    """Return concentration in mg/mL."""
    return amount_mg / volume_ml

def calculate_percent_yield(actual_yield_g, theoretical_yield_g):
    """Return percentage yield."""
    return (actual_yield_g / theoretical_yield_g) * 100

def stock_status(available_stock, reorder_level):
    """Return a simple classroom stock status."""
    if available_stock < reorder_level:
        return "REORDER"
    return "SUFFICIENT