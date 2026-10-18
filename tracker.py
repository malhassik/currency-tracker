import requests
import json


class Currency:

    # Конструктор класса
    def __init__(self, code, name, value, date):
        self.code = code
        self.name = name
        self.value = value
        self.date = date

    # properties и setters
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        if not value:
            raise ValueError("Ошибка: поле не может быть пустым")
        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Ошибка: поле не может быть пустым")
        self._name = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, vals):
        if vals < 0:
            raise ValueError("Ошибка: значение должно быть больше 0")
        self._value = vals

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not value:
            raise ValueError("Ошибка: поле не может быть пустым")
        self._date = value

    # Переопределение магических методов
    def __str__(self):
        return f"{self.name}({self.code}): {self.value} руб. на {self.date}"

    def __repr__(self):
        return f"Currency(code={self.code}, value={self.value})"

    # Методы
    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "value": self.value,
            "date": self.date,
        }


class CurrencyTracker:

    def __init__(self):
        self.history = []  # Список, где будут храниться объекты Currency

    def fetch_rates(self):
        """Делает запрос к API ЦБ и сохраняет курсы валют в историю."""
        print("Запрашиваем данные у ЦБ")
        url = "https://www.cbr-xml-daily.ru/daily_json.js"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            date_str = data["Date"][:10]  # Берем только YYYY-MM-DD

            valute_dict = data["Valute"]

            for code in ["USD", "EUR"]:
                if code in valute_dict:
                    v_info = valute_dict[code]

                    # 1. Проверяем, есть ли уже такая валюта на эту дату
                    is_duplicate = False
                    for item in self.history:
                        if item.code == code and item.date == date_str:
                            is_duplicate = True
                            break

                    if not is_duplicate:
                        currency = Currency(
                            code=code,
                            name=v_info["Name"],
                            value=v_info["Value"],
                            date=date_str,
                        )
                        self.history.append(currency)
                        print(f"Добавлено: {currency}")
                    else:
                        print(
                            f"Курс {code} на {date_str} уже есть в истории, пропускаем."
                        )

        except requests.exceptions.RequestException as e:
            print(f"Ошибка сети: {e}")
        except KeyError as e:
            print("Ошибка в структуре данных API:", e)

    def get_max_rate(self, code):
        """Возвращает объект Currency с самым высоким курсом для указанной валюты."""
        # 1. Отфильтровываем историю, оставляя только нужную валюту (например, USD)
        filtered = [curr for curr in self.history if curr.code == code]

        # 2. Если истории по этой валюте нет — возвращаем None
        if not filtered:
            return None

        # 3. Ищем максимум по полю value
        # Используем функцию max и лямбду, чтобы указать, что сравнивать нужно по value
        best_rate = max(filtered, key=lambda curr: curr.value)
        return best_rate

    # Методы сохранения в файл JSON и загрузки из файла
    def save_to_json(self, path):
        data_to_save = []

        for curr in self.history:
            data_to_save.append(curr.to_dict())

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data_to_save, file, ensure_ascii=False, indent=2)
        print(f"История сохранена в {path}")

    def load_from_json(self, path):
        try:
            with open(path, encoding="utf-8") as file:
                data = json.load(file)

            self.history = []

            for item in data:
                curr = Currency(
                    code=item["code"],
                    name=item["name"],
                    value=item["value"],
                    date=item["date"],
                )
                self.history.append(curr)

            print(f"Загружено {len(self.history)} записей из {path}")

        except FileNotFoundError:
            print("Файл истории не найден. Начинаем с чистого листа.")
