class Menu:

    def __init__(self, name, price, amount) -> None:
        self.__name = name
        self.__price = price
        self.__amount = amount

    def __eq__(self, other: object) -> bool:
        return (self.get_name(), self.get_price(), self.get_amount()) == (other.get_name(), other.get_price(), other.get_amount())

    def __str__(self) -> str:
        return "이름 : {}, 가격 : {}, 수량 : {}".format(self.__name, self.__price, self.__amount)

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_amount(self):
        return self.__amount
