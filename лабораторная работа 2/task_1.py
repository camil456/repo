money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0
current_capital = money_capital

while current_capital >= spend:
    current_capital += salary - spend
    months += 1
    spend *= (1 + increase)

print(f'Количество месяцев, которое можно протянуть без долгов: {months + 1}') # +1 потому что в первом месяце трат не было
