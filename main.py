from tracker import Currency

usd = Currency("USD", "Доллар США", 95.5, "2026-10-18")

print(usd)
print(repr(usd))
print(usd.to_dict())

try:
    usd.value = -10
except ValueError as e:
    print(f"Ошибка: {e}")
