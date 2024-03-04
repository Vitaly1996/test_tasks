def get_seconds(year, mon, day, h, m, s):
    day_in_month: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = (year - 1) * 365 + sum(day_in_month[:mon - 1]) + (day - 1)
    seconds = (days * 24 * 60 * 60) + (h * 60 * 60) + (m * 60) + s
    return seconds


date_1 = list(map(int, input('Начало (год,мес,день,час,мин,с)->').split()))
date_2 = list(map(int, input('Конец (год,мес,день,час,мин,с)->').split()))
SECOND_PER_ONE_DAY: int = 24 * 60 * 60
day, second = divmod(get_seconds(*date_2) - get_seconds(*date_1),
                     SECOND_PER_ONE_DAY)
print(day, second)
