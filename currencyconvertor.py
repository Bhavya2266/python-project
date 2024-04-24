from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    conversion_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * conversion_rate
    return converted_amount

def main():
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()