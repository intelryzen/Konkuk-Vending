import os
import sys
sys.path.append(os.getcwd())

from config import Config as config
from model.drink_info import Drink_info
from model.slot import Slot
from my_parser.base_parser import BaseParser

class wrongData(Exception):
    def __init__(self, msg="문법규칙 미준수", line = ""):
        self.msg = f"최초 오류 발생 행: {line}"
        self.msg += "오류: "+msg
    def __str__(self):
        return self.msg

class Drinks_util:
    def add_drink(self, drink):
        '''
            개수가 0개이면 그냥 추가 안함.
            파일 읽고 추가하는 거라서 
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
        bp = BaseParser()

        flag = True
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()
                for line in lines:
                    if flag and line.strip() == '':
                        raise wrongData("개행으로 파일이 시작하면 안됩니다.", line)
                    flag = False
                    if not line.endswith('\n'):
                        raise wrongData("행 끝에 개행이 없습니다.", line+"\n")
                    data = line.split()
                    if len(data) != 0 and len(data) != 4:
                        raise wrongData("행의 데이터 개수가 맞지 않습니다.", line)
                        # raise wrongData(line)
                    if len(data) == 4:
                        number = data[0].lstrip("0")
                        name = data[1]
                        if(not data[2].isdecimal() or not data[3].isdecimal()):
                            raise wrongData("가격 또는 개수가 0~9로만 이루어져있지 않습니다.", line)
                            # raise wrongData(line)
                        price = int(data[2])
                        stock = int(data[3])
                        if((bp.is_number(number) == None) or (bp.is_word(name) == None) or (bp.is_count(str(stock))==None)):
                            #iscount가 문자열만 받으려나?
                            raise wrongData("행의 데이터 중 최소 하나가 잘못되었습니다.", line)
                            # raise wrongData(line)
                        if(price<100 or price>1000000 or price%100 != 0):
                            raise wrongData("가격이 범위 밖이거나 100의 배수가 아닙니다.", line)
                            # raise wrongData(line)
                        self.add_drink(Drink(number, name, price, stock))

        except FileNotFoundError:
            print("경고: “음료수 리스트 파일이 없습니다. 파일을 생성합니다.”")
            with open(filename, 'w'):
                pass

        except wrongData as wd:
            print(wd)
            os.system('pause')
            sys.exit()
        # except UnicodeDecodeError:
        #     print("파일을 올바르게 디코딩할 수 없습니다.")
        #     pass
        if(len(config.drinks_list)==0):
            print("경고: “음료수 리스트 파일 내 데이터가 없습니다.”")

        if(self.check_duplicate_numbers()):
            print("오류: “번호의 중복이 확인되었습니다.”")
            os.system('pause')
            sys.exit()

    def write_to_file(self, filename=config.DRINKS_FILE_PATH, encoding='utf-8'):
        '''
        인자: filename = config.DRINKS_FILE_PATH
        파일에 config.drinks_list의 요소들을 한 행에 하나씩 저장
        프롬프트에서 직접적으로 호출할 필요 없음.
        '''
        with open(filename, 'w', encoding=encoding) as file:
            for drink in config.drinks_list:
                file.write(f"{drink.number} {drink.name} {drink.price} {drink.stock}\n")
    
    def check_duplicate_drink_number():
        numbers = set()
        for drink_info in config.drinks_list:
            if drink_info.number in numbers:
                return True
            numbers.add(drink_info.number)
        return False
    
    def check_duplicate_slot_number():
        numbers = set()
        for slot in config.slots_list:
            if slot.number in numbers:
                return True
            numbers.add(slot.number)
        return False

    def print_drinks_cus(self):
        '''
        인자: 없음
        '''
        for slot in config.slots_list:
            drink_info = self.find_drink_info(slot.drink_number)
            print(f"{slot.slot_number}. {drink_info.name} {drink_info.price}원 {slot.stock}개")
    
    def print_drinks_admin(self):
        '''
        인자: 없음
        음료수를 출력할 때 사용
        번호와 음료수를 출력
        '''
        for slot in config.drinks_list:
            drink_info = self.find_drink_info(slot.drink_number)
            print(f"{slot.number} {drink_info.drink_number} {drink_info.name} {drink_info.price}원 {slot.stock}개")

    def find_slot(slot_number):
        x = int(slot_number)

        for slot in config.slots_list:
            if(slot.slot_number == x):
                return slot
        return None

    def find_drink_info(drink_number):
        x = int(drink_number)

        for drink_info in config.drinks_list:
            if(drink_info.drink_number == x):
                return drink_info
        return None

    def modify_slot_stock(self, slot_number:str, stock:str):
        '''
        인자: 슬롯 번호, 개수
        슬롯 번호는 이미 존재하는 슬롯 번호임.
        음료수 재고 수정 후 파일 재작성까지 처리 완.
        '''
        slot = self.find_slot(slot_number)
        stock = int(stock)
        slot.stock = stock

        if(stock == 0):
            self.check_all_zero(slot.drink_number)
        else:
            drink_info = self.find_drink_info(slot.drink_number)
            print(f'{slot.slot_number}번 {drink_info.name}의 개수가 {slot.stock}개로 변경되었습니다.')
            self.write_to_file(config.SLOTS_FILE_PATH)

    def check_all_zero(self, drink_number):
        for slot in config.slots_list:
            if(slot.drink_number == drink_number):
                if(slot.stock != 0):
                    break
                else:
                    config.slots_list.remove(slot)

        self.write_to_file(config.SLOTS_FILE_PATH)

    def add_new_drink(self, number:str, name:str, price:str, stock:str):
        '''
        인자: 번호, 이름, 가격, 개수
        새로운 음료수를 추가하는 함수.
        '''
        number = str(number).lstrip("0")
        self.add_drink(Drink(number, str(name), int(price), int(stock)))
        print(f"{number}번 {name}가 개당 {price}원으로 {stock} 추가되었습니다.")
        self.write_to_file(config.DRINKS_FILE_PATH)

    # 돈 처리는 완료되었다고 가정
    def buy_drink(self, number:str):
        number = number.lstrip("0")
        target = self.find_drink(number)
        '''
        인자: 목록 상 번호
        음료수 구매 시 개수를 차감하는 함수.
        개수 차감 후 0개가 되면 목록에서 삭제
        구매 완료 후 파일 재작성까지 완.
        '''
        if(target!=None):
            tStock = target.stock - 1
            # 수량이 0개가 된 경우 목록에서 삭제
            if(tStock == 0):
                config.drinks_list.remove(target)
            else:
                target.stock = tStock
            self.write_to_file()
        else:
            print("오류: 올바른 입력이 아닙니다.")


# 테스트
if __name__ == "__main__":
    du = Drinks_util()
    du.read_from_file()
    du.print_drinks_cus()
    du.write_to_file()
    # du.print_drinks()
    # du.add_new_drink(7,"이에로사이다",1800,30)
    # du.add_new_drink(8,"화르르멘션사이다",2500,30)
    # du.buy_drink('1')
    # du.modify_stock('8', 9)
    # print()
    # du.print_drinks()
