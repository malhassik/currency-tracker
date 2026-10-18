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
            print("Ошибка: поле не может быть пустым")
        self._code = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            print("Ошибка: поле не может быть пустым")
        self._name = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, vals):
        if vals > 0:
            print("Ошибка: значение должно быть больше 0")
        self._value = vals

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not value:
            print("Ошибка: поле не может быть пустым")
        self._date = value

    # Переопределение магических методов
    def __str__(self):
        print(f"Доллар США (USD): {self.value} руб. на {self.date}")

    def __repr__(self):
        pass

    # Методы
    def to_dict(self):
        pass
