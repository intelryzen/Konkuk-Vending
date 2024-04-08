class Drink:
    def __init__(self, number, name, price, stock):
        self.number = number
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Number: {self.number}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"

class DrinkList:
    def __init__(self):
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)

    def read_from_file(self, filename, encoding = 'utf-8'):
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()
                for line in lines:
                    data = line.split()
                    if len(data) == 4:
                        number = data[0].lstrip("0")
                        name = data[1]
                        price = int(data[2])
                        stock = int(data[3])
                        self.add_drink(Drink(number, name, price, stock))
        except FileNotFoundError:
            print("오류: 음료수 리스트 파일이 없습니다. 파일을 생성합니다.")
            with open(filename, 'w'):
                pass
        # except UnicodeDecodeError:
        #     print("파일을 올바르게 디코딩할 수 없습니다.")
        #     pass

        # VV 이거 다시
        print(len(drinkList.drinks))
        if(len(self.drinks)==0):
            print("경고: 음료수 리스트 파일 내 데이터가 없습니다.")

        elif(self.check_duplicate_numbers()):
            print("오류: 번호의 중복이 확인되었습니다.")

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for drink in self.drinks:
                file.write(f"{drink.number} {drink.name} {drink.price} {drink.stock}\n")
    # VV이거 다시
    def check_duplicate_numbers(self):
        numbers = set()
        duplicates = set()
        for drink in self.drinks:
            if drink.number in numbers:
                duplicates.add(drink.number)
            else:
                numbers.add(drink.number)
        if duplicates:
            print("오류: 번호의 중복이 확인되었습니다.")
            return False
        return True

    def print_drinks(self):
        for drinks in self.drinks:
            print(drinks)

# 테스트
drinkList = DrinkList()
print(len(drinkList.drinks))

drinkList.read_from_file('drinks.txt')
drinkList.print_drinks()

if(len(drinkList.drinks)==0):
    print("경고")