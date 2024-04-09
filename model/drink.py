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
        if drink.stock != 0:
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
        if(len(self.drinks)==0):
            print("경고: 음료수 리스트 파일 내 데이터가 없습니다.")

        self.check_duplicate_numbers()

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for drink in self.drinks:
                file.write(f"{drink.number} {drink.name} {drink.price} {drink.stock}\n")
                
    def check_duplicate_numbers(self):
        numbers = set()
        for drink in self.drinks:
            if drink.number in numbers:
                print("오류: 번호의 중복이 확인되었습니다.")
                return False
        return True
        # duplicates = set()
        # for drink in self.drinks:
        #     if drink.number in numbers:
        #         duplicates.add(drink.number)
        #     else:
        #         numbers.add(drink.number)
        # if duplicates:
        #     print("오류: 번호의 중복이 확인되었습니다.")
        #     return False
        # return True

    def print_drinks(self):
        for drink in self.drinks:
            print(drink)

    def find_drink(self, x):
        for drink in self.drinks:
            if(drink.number == x):
                return drink
        print("오류: 존재하지 않는 번호입니다.")
        return None

    def modify_stock(self, x:str, stock:str):
    # 프롬프트에서 공백 처리될 것이라고 가정
    # x, stock은 문자열만
        if(len(x)==0 or len(x)>2):
            # 1~2자리만 허용
            print("오류: 올바른 입력이 아닙니다.")
        x = x.lstrip("0")
        if(int(x)<1 or int(x)>99):
            print("오류: 올바른 입력이 아닙니다.")
        if(not x.isdecimal()):
            print("오류: 올바른 입력이 아닙니다.")
        else:
            target = self.find_drink(x)
            if(target != None):
                if(len(stock)==0 or len(stock)>2):
                    # 1~2자리만 허용
                    print("오류: 음료수 개수 입력시 0과 99사이의 숫자만 기입해 주세요.")
                # 정수 외의 문자열
                elif(not stock.isdecimal()):
                    print("오류: 음료수 개수 입력시 0과 99사이의 숫자만 기입해 주세요.")
                stock = int(stock)
                # 범위 이탈
                if(stock<0 or stock>99):
                    print("오류: 음료수 개수 입력시 0과 99사이의 숫자만 기입해 주세요.")
                elif(stock == 0):
                    print(f'{target.number}번 {target.name}가 삭제되었습니다.')
                    self.drinks.remove(target)
                else:
                    target.stock = stock
                    print(f'{target.number}번 {target.name}의 개수가 {target.stock}개로 변경되었습니다.')
                    
                # self.print_drinks() # 정상적으로 수정되는 지 확인하기 위한 라인

# 테스트
drinkList = DrinkList()

drinkList.read_from_file('drinks.txt')

drinkList.modify_stock("2", "5")
drinkList.modify_stock("2", "0")


drinkList.write_to_file('test.txt')