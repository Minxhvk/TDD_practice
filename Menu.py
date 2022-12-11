class Menu:

    def __init__(self, name, price, amount) -> None:
        self.name = name
        self.price = price
        self.amount = amount

    def __eq__(self, other: object) -> bool:
        return (self.get_name(), self.get_price(), self.get_amount()) == (other.get_name(), other.get_price(), other.get_amount())

    def __str__(self) -> str:
        return "이름 : {}, 가격 : {}, 수량 : {}".format(self.name, self.price, self.amount)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.amount
