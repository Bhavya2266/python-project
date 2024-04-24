from forex_python.converter import CurrencyRates

def convert_currency(amount, cur_from, cur_to):
    c = CurrencyRates()
    rate = c.get_rate(cur_from, cur_to)
    converted_amount = amount * rate
    output = f"{amount} {cur_from} = {converted_amount} {cur_to}"
    print(output)

# Example usage:
convert_currency(1, "USD", "INR")