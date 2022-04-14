subscription_price = input('Ingrese el precio de suscripción normal:')
number_of_normal_users = input('Ingrese el número de usuarios normales:')
number_of_premium_users = input('Ingrese el número de usuarios premium:')
total_expenses = input('Ingrese el gasto total:')

subscription_price_num = float(subscription_price)
number_of_normal_users_num = int(number_of_normal_users)
number_of_premium_users_num = int(number_of_premium_users)
total_expenses_num = float(total_expenses)

profit = ((subscription_price_num * number_of_normal_users_num) + ((subscription_price_num * 1.5) * number_of_premium_users_num)) - total_expenses_num

print(f'La utilidad del proyecto es: {profit}')