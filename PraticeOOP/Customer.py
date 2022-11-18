class Customer:
    def __init__(self, name:str, membership_type:str):
        self.name = name
        self.membership_type = membership_type
        print('customer created')

if __name__ == '__main__':
    customers = [Customer('Caleb', 'Gold'), Customer('Brad', 'Bronze')]
    print(customers[0].name)
