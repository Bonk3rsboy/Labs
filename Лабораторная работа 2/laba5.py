salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_ = 0

for month in range(months):
    if spend > salary:
        total_ += spend - salary
    spend *= (1 + increase)
total_ = round(total_)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", total_)
