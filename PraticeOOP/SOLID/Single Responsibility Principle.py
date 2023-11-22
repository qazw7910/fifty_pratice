def main():
    pass


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        self.total += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total -= item.price

    # ----------------------------------------------------------------
    # print_receipt() 方法應該被拆分為一個獨立的類別或方法，以實現單一職責原則
    def print_receipt(self):
        print('Items:')
        for item in self.items:
            print(f'{item.name} - ${item.price}')
        print(f'Total: ${self.total}')


if __name__ == '__main__':
    main()
