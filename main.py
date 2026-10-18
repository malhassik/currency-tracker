from tracker import Currency, CurrencyTracker

tracker = CurrencyTracker()
tracker.fetch_rates()

print("\nИстория:")
for item in tracker.history:
    print(item)
