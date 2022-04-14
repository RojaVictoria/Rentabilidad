subscription_price = input('Ingrese el precio de suscripción (ingrese un decimal separado por punto):')
number_of_users = input('Ingrese el número de usuarios (ingrese un número entero):')
total_expenses = input('Ingrese el gasto total (ingrese un decimal separado por punto):')
last_year_profit = input('Ingrese la utilidad del año anterior (ingrese un número entero):')

profit = float(subscription_price) * int(number_of_users) - float(total_expenses)

profit_ratio = profit/float(last_year_profit)

print(f'La razón entre la utilidad del año anterior "{last_year_profit}" y la de este año "{profit}" es: {profit_ratio:.2f}')