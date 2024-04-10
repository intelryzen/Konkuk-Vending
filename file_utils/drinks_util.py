# VVV 얘가 안됨. VVV
from config import Config as config
from model.drink import Drink

#for the test
# class config:
#     drinks_list = []
#     DRINKS_FILE_PATH = 'drinks.txt'

# class Drink:
#     def __init__(self, number, name, price, stock):
#         self.number = number
#         self.name = name
#         self.price = price
#         self.stock = stock

#     def __str__(self):
#         return f"{self.number} {self.name} {self.price}원 {self.stock}개"

class Drinks_util:
    def __init__(self):
        self.read_from_file()

    def add_drink(self, drink):
        '''
            개수가 0개이면 그냥 추가 안함.
        '''
        if drink.stock != 0:
            config.drinks_list.append(drink)

    def read_from_file(self, filename=config.DRINKS_FILE_PATH, encoding = 'utf-8'):
        '''
        인자: filename = config.DRINKS_FILE_PATH, encoding = 'utf-8'
        파일을 읽어와서 음료수의 번호의 선행 0 지우고 개수가 0인 경우를 제외하여 config.drinks_list에 추가한다.
        파일 없는 경우 처리 완.
        파일 내의 데이터가 없는 경우 처리 완.
        음료수들의 번호 중복 처리 완.
        '''
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
            print("경고: 음료수 리스트 파일이 없습니다. 파일을 생성합니다.")
            with open(filename, 'w'):
                pass
        # except UnicodeDecodeError:
        #     print("파일을 올바르게 디코딩할 수 없습니다.")
        #     pass
        if(len(config.drinks_list)==0):
            print("경고: 음료수 리스트 파일 내 데이터가 없습니다.")

        if(self.check_duplicate_numbers()):
            print("오류: 번호의 중복이 확인되었습니다.")
            exit()

    def write_to_file(self, filename=config.DRINKS_FILE_PATH):
        '''
        인자: filename = config.DRINKS_FILE_PATH
        파일에 config.drinks_list의 요소들을 한 행에 하나씩 저장
        프롬프트에서 직접적으로 호출할 필요 없음.
        '''
        with open(filename, 'w') as file:
            for drink in config.drinks_list:
                file.write(f"{drink.number} {drink.name} {drink.price} {drink.stock}\n")
                
    def check_duplicate_numbers(self):
        '''
        인자: 없음
        파일 읽어올 때 번호 중복을 확인하기 위한 함수로
        프롬프트에서 직접적으로 호출할 필요 없음.
        '''
        numbers = set()
        for drink in config.drinks_list:
            if drink.number in numbers:
                return True
        return False
        # duplicates = set()
        # for drink in config.drinks_list:
        #     if drink.number in numbers:
        #         duplicates.add(drink.number)
        #     else:
        #         numbers.add(drink.number)
        # if duplicates:
        #     print("오류: 번호의 중복이 확인되었습니다.")
        #     return False
        # return True

    #프롬프트별 출력 다름 주의
    #관리자 프롬프트에서의 음료수 재고 출력
    def print_drinks_for_admin(self):
        '''
        인자: 없음
        관리자 프롬프트에서 음료수를 출력할 때 사용
        번호와 음료수를 출력
        '''
        for drink in config.drinks_list:
            print(drink)
    #음료수 목록 출력
    def print_drinks_for_customer(self):
        '''
        인자: 없음
        모드 선택 프롬프트에서 금액 입력 프롬프트로 넘어가기 전 출력에서 사용
        목록 순서대로 번호가 붙어 출력
        '''
        i = 1
        for drink in config.drinks_list:
            print(f"{i}. {drink.name} {drink.price}원 {drink.stock}개")
            i=i+1

    # 프롬프트에서 호출할 때 인자는 이미 검사 완료되었다고 생각함. 따라서 x는 항상 형식에 맞고 존재하는 번호이다.
    def find_drink(self, x):
        '''
        인자: 번호
        음료수 재고 수정 시 대상 음료를 찾을 때 사용하는 함수
        프롬프트에서 직접적으로 호출할 필요 없음.
        '''
        for drink in config.drinks_list:
            if(drink.number == x):
                return drink

    def modify_stock(self, number:str, stock:str):
        '''
        인자: 번호, 개수
        음료수 재고 수정 프롬프트에서 사용.
        0개가 입력된 경우 음료 삭제.
        음료수 재고 수정 후 파일 재작성까지 처리 완.
        '''
        number = number.lstrip("0")
        target = self.find_drink(number)
        stock = int(stock)
        if(stock == 0):
            # print(f'{target.number}번 {target.name}가 삭제되었습니다.')
            config.drinks_list.remove(target)
        else:
            target.stock = stock
            # print(f'{target.number}번 {target.name}의 개수가 {target.stock}개로 변경되었습니다.')
        self.write_to_file(config.DRINKS_FILE_PATH)

    def add_new_drink(self, number:str, name:str, price:str, stock:str):
        '''
        인자: 번호, 이름, 가격, 개수
        새로운 음료수를 추가하는 함수.
        '''
        number = number.lstrip("0")
        self.add_drink(Drink(number, name, price, stock))

    # 돈 처리는 완료되었다고 가정
    def buy_drink(self, listNum:str):
        '''
        인자: 목록 상 번호
        음료수 구매 시 개수를 차감하는 함수.
        개수 차감 후 0개가 되면 목록에서 삭제
        구매 완료 후 파일 재작성까지 완.
        '''
        # 목록 내의 번호가 아닌 경우
        listNum = int(listNum)
        if(listNum<1 or len(config.drinks_list)<listNum ):
            print("올바른 입력이 아닙니다.")
        else:
            tStock = config.drinks_list[listNum-1].stock - 1
            # 수량이 0개가 된 경우 목록에서 삭제
            if(tStock == 0):
                config.drinks_list.remove(listNum-1)
            else:
                config.drinks_list[listNum-1].stock = tStock
            self.write_to_file()


# 테스트
if __name__ == "__main__":
    du = Drinks_util()
    du.read_from_file()
    du.print_drinks_for_admin()
    du.print_drinks_for_customer()
    du.modify_stock('7', '0')
    du.buy_drink('0')
    du.print_drinks_for_admin()
    du.print_drinks_for_customer()