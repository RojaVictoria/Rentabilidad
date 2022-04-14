subscription_price = input('Ingrese el precio de suscripción:')
number_of_users = input('Ingrese el número de usuarios:')
total_expenses = input('Ingrese el gasto total:')

profit = int(subscription_price) * int(number_of_users) - int(total_expenses)

print(f'La utilidad del proyecto es: {profit}')