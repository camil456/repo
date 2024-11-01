import math

salary = 5000
spend = 6000
months = 10
increase = 0.03

required_capital = 0
current_spend = spend

for month in range(months):
    shortfall = current_spend - salary

    if shortfall > 0:
        required_capital += shortfall

    current_spend *= (1 + increase)

required_capital = math.ceil(required_capital)

print(f'Подушка безопасности, чтобы протянуть 10 месяцев без долгов: {required_capital - 1}')
