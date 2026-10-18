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
