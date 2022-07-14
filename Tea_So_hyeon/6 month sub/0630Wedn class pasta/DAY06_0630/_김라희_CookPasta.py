class CookPasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def payment(self, approval=False):
        total = 12900
        print(f'total ￦{int(total)}')
        customer_pay = input()
        if int(total) == customer_pay:
            return True

    def getready(self):
        pass

    def poaching(self):
        pass

    def flambe(self):
        pass

    def plating(self):
        dish = 'Have a great meal time'
        print(dish)


def pasta(types=''):
    if not types: return types


def runapp():
    # give a menu to customers
    types = [
        'Macceroni', 'Farfalle', 'Cannelloni',
        'Conchiglie', 'Anelli', 'Penne',
        'Spaghetti', 'Fusilli', 'Bucatini',
        'Gnochhi', 'Fettuccine', 'Gemelli'
        'Creste di galli', 'Cavatappi', 'Rigatoni'
    ]
    print(types)
    choose = input('which types of pasta do you want? ')
    cook = CookPasta(pasta(types=choose))

    # payment process
    if cook.payment():
        cook.getready()
        cook.poaching()
        cook.flambe()
        cook.plating()


if __name__ == '__main__':
    runapp()
