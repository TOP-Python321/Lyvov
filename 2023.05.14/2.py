def taxi_cost(distance: int, time: int = 0) -> int | None:
    """Возвращает результат вычисления стоимости поездки или None - если вычисление не возможно"""
    fixid = 80
    dop = 6 / 150
    waiting = 3 * time
    fine = 80
    
    if distance >= 0 and time >= 0:
        # КОММЕНТАРИЙ: без этой проверки можно обойтись, равно как и без почти полного повторения выражения в инструкции возврата
        if distance == 0:
            return round(fixid + fine + waiting)
        return round(fixid + distance * dop + waiting)


# ИСПРАВИТЬ: выполняйте ручные тесты в режиме инспекции
print(taxi_cost(1500))
# 140

print(taxi_cost(2560))
# 182

print(taxi_cost(0, 5))
# 175

print(taxi_cost(42130, 8))
# 1789

print(taxi_cost(-300))
# None


# ИТОГ: хорошо — 3/3
