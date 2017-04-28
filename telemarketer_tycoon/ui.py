def format_money(value: float):
    return f"£{format_float(value)}"


def format_float(value: float):
    return f"{value:,.2f}"