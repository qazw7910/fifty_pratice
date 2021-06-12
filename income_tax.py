
TAX_RATE = {
    0 : 0.1,
    10000 : 0.2,
    50000 : 0.3,
    100000: 0.4,
    500000: 0.5
}

def find_tax_rage(amount):
    result = 0.0
    for income, rate in TAX_RATE.items():
        if amount >= income :
            result = rate
    return result

def calculate_tax(amount):
    if not (isinstance(amount, int) or isinstance(amount, float)):
        raise ValueError('Parameter "amount" has to be a number')
    return amount * find_tax_rage(amount)



