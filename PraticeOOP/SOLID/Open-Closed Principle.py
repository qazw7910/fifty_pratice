class Shopcart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# ----------------------------------------------------------------
# 在這個修正過後的範例中，我們將 get_total_price() ****方法重構為使用 Discount 策略類別，而 Discount ****策略類別定義了一個共通的介面
class Discount:
    def calculate_discount(self, total_price):
        return total_price


class TenPercentDiscount(Discount):
    def calculate_discount(self, total_price):
        return total_price * 0.9


# ----------------------------------------------------------------

class ShoppingCartWithDiscount:
    def __init__(self, discount: Discount):
        self.items = []
        self.discount = discount

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return self.discount.calculate_discount(total_price)


if __name__ == '__main__':
    apple = Item("蘋果", 10)
    orange = Item("橙子", 10)
    banana = Item("香蕉", 10)

    # 當我們需要新增一種不同類型的折扣時，只需要創建一個新的策略類別並將其傳遞給 ShoppingCartWithDiscount 即可，而無需修改現有的程式碼
    cart = ShoppingCartWithDiscount(TenPercentDiscount())

    cart.add_item(apple)
    cart.add_item(orange)
    cart.add_item(banana)

    total_price = cart.get_total_price()
    print(total_price)
