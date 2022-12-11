class Menu:

    def __init__(self, name, price, amount) -> None:
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self) -> str:
        return "이름 : {}, 가격 : {}, 수량 : {}".format(self.name, self.price, self.amount)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.amount

    def equals(self, menu):
        return menu.get_name() == self.get_name() \
            and menu.get_price() == self.get_price() \
            and menu.get_amount() == self.get_amount()
