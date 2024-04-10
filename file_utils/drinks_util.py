from config import config
from model.drink import Drink

class Drinks_util:
    def add_drink(self, drink):
        '''
            개수가 0개이면 그냥 추가 안함.
        '''
        if drink.stock != 0:
            config.drinks_list.append(drink)

    def read_from_file(self, filename=config.DRINKS_FILE_PATH, encoding = 'utf-8'):
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
        if(len(config.drinks_list)==0):
            print("경고: 음료수 리스트 파일 내 데이터가 없습니다.")

        self.check_duplicate_numbers()

    def write_to_file(self, filename=config.DRINKS_FILE_PATH):
        with open(filename, 'w') as file:
            for drink in config.drinks_list:
                file.write(f"{drink.number} {drink.name} {drink.price} {drink.stock}\n")
                
    def check_duplicate_numbers(self):
        numbers = set()
        for drink in config.drinks_list:
            if drink.number in numbers:
                print("오류: 번호의 중복이 확인되었습니다.")
                return False
        return True
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
    def print_drinks_for_admin():
        for drink in config.drinks_list:
            print(drink)
    #음료수 목록 출력
    def print_drinks_for_customer():
        i = 1
        for drink in config.drinks_list:
            print(f"{i}. {drink.name} {drink.price}원 {drink.stock}개")
            i=i+1

    # 프롬프트에서 호출할 때 인자는 이미 검사 완료되었다고 생각함. 따라서 x는 항상 형식에 맞고 존재하는 번호이다.
    def find_drink(self, x):
        for drink in config.drinks_list:
            if(drink.number == x):
                return drink

    def modify_stock(self, number:str, stock:str):
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
        number = number.lstrip("0")
        self.add_drink(Drink(number, name, price, stock))

    # def buy_drink(self, listNum:str, name)
        
# if __name__ == "__main__":
Drinks_util.read_from_file()
Drinks_util.print_drinks_for_admin()
Drinks_util.print_drinks_for_customer()
