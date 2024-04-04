#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount: int = 0) -> None:
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_item = None

    def add_item(self, title: str, price: float, quantity: int = 1):
        for _ in range(quantity):
            self.items.append(title)

        self.total += price * quantity

        self.last_item = {
            'title': title,
            'price': price,
            'quantity': quantity
        }

    def apply_discount(self):
        if self.discount == 0:
            print('There is no discount to apply.')
        else:
            self.total *= 1 - self.discount / 100
            print(f'After the discount, the total comes to ${round(self.total)}.')

    def void_last_transaction(self):
        for _ in range(self.last_item['quantity']):
            self.items.pop()
        
        self.total -= self.last_item['price'] * self.last_item['quantity']

cash_register_with_discount = CashRegister(20)
cash_register_with_discount.add_item('macbook air', 1000)

print(cash_register_with_discount.void_last_transaction())