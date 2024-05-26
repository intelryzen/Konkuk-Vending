from my_parser.admin_function_parser import AdminFunctionParser
from file_utils.cash_util import Cash_Utils
from file_utils.slot_util import SlotUtils
from file_utils.drinkInfo_util import DrinkInfoUtils
from model.drink_info import Drink_info
from model.slot import Slot
from config import Config as config


class AdminPrompt:
    '''
        관리자 프롬프트
        command:
            0: 모드 선택 프롬프트로 이동
            1: 자판기 내의 음료수 재고 상황을 출력
            2: 자판기 내의 현금 상황을 출력
            3: 자판기 내의 현금 상황을 수정
            4: 자판기 내 특정 번호의 음료수 재고를 수정
            5: 자판기의 특정 번호에 음료수를 추가
            비정상: 오류 메시지 + 관리자 프롬프트로 이동
    '''    
    def __init__(self):
        self.parser = AdminFunctionParser()

    # 관리자 프롬프트
    def admin_prompt(self):
        while True:
            print("\n<관리자>")
            print("1. 잔돈 확인")
            print("2. 음료수 슬롯별 재고 확인")
            print("3. 잔돈 수정")
            print("4. 자판기 슬롯별 음료수 재고 수정")
            print("5. 자판기 슬롯에 음료수 할당")
            print("6. 음료수 정보 추가")
            print("7. 음료수 정보 삭제")
            print("(0.로그아웃)")
            print("-------------------------------------------")
            admin_input = input(">>>")

            is_valid, command = self.parser.parser(admin_input)
            
            if is_valid:
                admin_input = admin_input.strip()
                parts = admin_input.split()
                
                if command == 1:
                    sorted_currency_list = sorted(config.currency_list, key=lambda x: x.value, reverse=True)
                    for Currency in sorted_currency_list:
                        print(f"{Currency.value}원 {Currency.quantity}개")            
                    
                elif command == 2:
                    # 음료수 슬롯별 재고 확인
                    self.print_drinks_admin()
                    
                elif command == 3:
                    # 잔돈 수정
                    parts = [int(i) for i in parts]
                    cash_utils_instance = Cash_Utils()  # Cash_Utils 클래스의 인스턴스 생성
                    cash_utils_instance.change_currency(parts[1], parts[2])
                    from model.cash import Currency
                    currency = Currency(parts[1], parts[2])
                    cash_utils_instance.save_currencies(config.CASH_FILE_PATH, currency)

                elif command == 4:
                    # 자판기 슬롯별 음료수 재고 수정
                    self.modify_slot_stock(parts[1], parts[2])
                    
                elif command == 5:
                    # 자판기 슬롯에 음료수 할당
                    self.assign_drink_slot(parts[1], parts[2], parts[3])

                elif command == 6:
                    #음료수 정보 추가
                    self.append_drink_info(parts[1], parts[2], parts[3])

                elif command == 7:
                    #음료수 정보 삭제
                    self.remove_drink_info(parts[1])

                elif command == 0:
                    return command
                    '''
                    from prompt.mode import Mode
                    modeselect = Mode()
                    modeselect.mode_selection_prompt()
                    '''
            else:
                print(command)  # 오류 메시지 출력
                continue

    def print_drinks_admin(self):
        '''
        인자: 없음
        음료수를 출력할 때 사용
        번호와 음료수를 출력
        '''
        for slot in config.slots_list:
            drink_info = self.find_drink_info(slot.drink_number)
            print(f"{slot.slot_number} {drink_info.drink_number} {drink_info.name} {drink_info.price}원 {slot.stock}개")

    def find_slot(self, slot_number):
        x = int(slot_number)

        for slot in config.slots_list:
            if(slot.slot_number == x):
                return slot
        return None
    
    def find_slots_with_same_drink_number(self, drink_number):
        dN = int(drink_number)
        slots = list()
        for slot in config.slots_list:
            if(slot.drink_number == dN):
                slots.append(slot)

        return slots

    def find_drink_info(self, drink_number):
        x = int(drink_number)

        for drink_info in config.drinks_list:
            if(drink_info.drink_number == x):
                return drink_info
        return None

    def modify_slot_stock(self, slot_number:str, stock:str):
        slot = self.find_slot(slot_number)
        s = int(stock)
        slot.stock = s
        SlotUtils().update_stock(slot.slot_number, slot.stock)

        drink_info = self.find_drink_info(slot.drink_number)
        print(f'{slot.slot_number}번 {drink_info.name}의 개수가 {slot.stock}개로 변경되었습니다.')

        if(s == 0):
            self.check_all_zero(slot.drink_number)

    def check_all_zero(self, drink_number:int):
        slots = list()

        for slot in config.slots_list:
            if(slot.drink_number == drink_number):
                if(slot.stock != 0):
                    return
                else:
                    slots.append(slot)

        for slot in slots:
            config.slots_list.remove(slot)
        SlotUtils().delete_slots_used_same_drink(drink_number)
        return

    def assign_drink_slot(self, slot_number:str, drink_number:str, stock:str):
        sN = int(slot_number)
        dN = int(drink_number)
        s = int(stock)
        config.slots_list.append(Slot(sN, dN, s))
        SlotUtils().insert_slot(sN, dN, s)
        drink_info = self.find_drink_info(dN)
        print(f"{sN}번 슬롯에 {drink_info.drink_number}번 {drink_info.name}가 개당 {drink_info.price}원으로 {s}개 추가되었습니다.")

    def append_drink_info(self, drink_number:str, name:str, price:str):
        dN = int(drink_number)
        p = int(price)
        config.drinks_list.append(Drink_info(dN, name, p))
        DrinkInfoUtils().update_new_drinks(dN, name, p)
        print(f"{dN}번 {name}가 개당 {p}원으로 추가되었습니다.")
    
    def remove_drink_info(self, drink_number:str):
        drink_info = self.find_drink_info(drink_number)
        config.drinks_list.remove(drink_info)
        DrinkInfoUtils().delete_drink(drink_info.drink_number)

        print(f"{drink_info.drink_number}번 {drink_info.name} {drink_info.price}원이 삭제되었습니다.")
            
if __name__ == "__main__":
    # 관리자 프롬프트 테스트
    AdminPrompt()
