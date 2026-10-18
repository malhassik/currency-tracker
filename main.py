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
