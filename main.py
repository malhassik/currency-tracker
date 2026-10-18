from tracker import Currency, CurrencyTracker

tracker = CurrencyTracker()

# 1. Пробуем загрузить старую историю (при первом запуске файла нет - будет сообщение)
tracker.load_from_json("history.json")

# 2. Идем в интернет за новыми данными
tracker.fetch_rates()

# 3. Сохраняем обновленную историю на диск
tracker.save_to_json("history.json")

print("\nИтоговая история в памяти:")
for item in tracker.history:
    print(item)

print("\n--- Аналитика ---")
max_usd = tracker.get_max_rate("USD")
if max_usd:
    print(
        f"Максимальный курс доллара в истории: {max_usd.value} руб. (на {max_usd.date})"
    )
else:
    print("Данных по доллару пока нет.")
