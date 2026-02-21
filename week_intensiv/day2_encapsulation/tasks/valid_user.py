class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd):
        self.username = user
        self._password = pwd

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, val):
        if len(val) >= 8 and any(i.isdigit() for i in val):
            self._password = val
