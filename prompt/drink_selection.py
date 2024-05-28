from my_parser.drink_selection_parser import DrinkSelectionParser
from config import Config as c
from .change import Change
from file_utils.slot_util import SlotUtils
from file_utils.buyer_util import BuyerUtils
from prompt.coupon import Coupon

class DrinkSelection:
    '''
    음료수 선택 프롬프트
    command:
        0: 거스름돈 출력하고 음료수 선택 프롬프트, 잔액 0원이면 금액 입력 프롬프트로 이동
        정상: 잔액 업데이트, 음료수 목록 업데이트 후 출력, 음료수 재고 0이면 drinks.txt에서 삭제
        비정상: 음료수 선택 프롬프트로 이동
    '''

    # 음료수 선택 프롬프트
    def drink_selection_prompt(self):
        self.command = input("\n구매하실 음료수 번호를 입력해주세요.(0. 거스름 돈 반환 및 뒤로가기)\n>>>")
        parser = DrinkSelectionParser()
        drink_check, parsed_command = parser.parse(self.command)
        drink_price=0
        
        # 0: 거스름돈 출력하고 음료수 목록 출력 후 금액입력 프롬프트로 이동
        if  drink_check == True:
            if parsed_command ==0:
                c.cash_by_cus =0
                canChange, msg = Change(0) # 거스름 돈 출력
                print(msg)
                for i in range(6):
                    c.customer_list[i].quantity = 0 #사용자가 투입한 금액 0으로 초기화
                self.print_drinks_cus() #음료수 리스트 출력
                return
            else :
                # 구매자가 선택한 음료의 가격을 drink_price 변수로 저장
                num_coup = 0
                cus_money = 0
                id = c.logged_in_buyer
                for i in range(0, len(c.buyer_list)):
                    if c.buyer_list[i].buyer_id == id:
                        num_coup = c.buyer_list[i].coupon_number
                        cus_money = c.buyer_list[i].money
                use_coupon = Coupon.coupon_prompt(num_coup)
                for i in range (0, len(c.drinks_list)):
                    if int(c.drinks_list[i].drink_number) == int(parsed_command):
                        drink_price = c.drinks_list[i].price
                        if use_coupon == 1:
                            drink_price -= 1000
                            num_coup -= 1
                            if drink_price < 0:
                                drink_price = 0
                if self.cash_by_custom() < drink_price: #투입금이 음료수 가격보다 적을 때
                    print("오류: 금액이 부족합니다. 다른 음료수를 선택해주세요")
                    return self.drink_selection_prompt()
                else:
                    canChange, msg = Change(drink_price)
                    if not canChange: #거스름돈 없음
                        print(msg)
                        return self.drink_selection_prompt()
                    else:
                        if use_coupon == 1:
                            print("쿠폰을 사용하였습니다.")
                        elif use_coupon == 2:
                            print("쿠폰을 미사용하였습니다.")
                        print("보유 쿠폰 개수:" + str(num_coup) + "개")
                        cus_money = cus_money + drink_price
                        added_coup = int(cus_money / 10000)
                        print(added_coup)
                        num_coup += added_coup
                        cus_money %= 10000
                        rem = 10000 - cus_money
                        bu = BuyerUtils()
                        bu.update_money_coupon(str(id), int(cus_money), int(num_coup))
                        self.buy_drink(str(parsed_command)) # 해당 위치에서 음료수 목록 파일 업데이트
                        if self.cash_by_custom() == 0:
                            if added_coup > 0:
                                print("누적 결제금액이 10000원을 초과하여 1000원 할인쿠폰이 발급되었습니다.")
                                print("다음 쿠폰 발급까지" + str(rem) + "원 남았습니다.")
                                print("보유 쿠폰 개수:" + str(num_coup) + "개")
                            self.print_drinks_cus() # 음료수 목록 출력
                            return
                        else:
                            print ("잔돈: ", self.cash_by_custom())
                            if added_coup > 0:
                                print("누적 결제금액이 10000원을 초과하여 1000원 할인쿠폰이 발급되었습니다.")
                                print("다음 쿠폰 발급까지" + str(rem) + "원 남았습니다.")
                                print("보유 쿠폰 개수:" + str(num_coup) + "개")
                            print("-------------------------------------------")
                            self.print_drinks_cus() # 음료수 목록 출력
                            return self.drink_selection_prompt()
            '''
            if not canChange:
                c.cash_by_cus += drink_price
            '''
        else:
            print(parsed_command)       
            return self.drink_selection_prompt()

        # 정상: 잔액과 업데이트 된 음료수 목록 출력 후 음료수 선택 프롬프트로 이동

    def cash_by_custom(self):
         ret = 0
         for i in range(6):
             ret += (c.customer_list[i].value * c.customer_list[i].quantity)
         return ret
    
    def find_drink_info(self, drink_number):
        x = int(drink_number)

        for drink_info in c.drinks_list:
            if(drink_info.drink_number == x):
                return drink_info
        return None
    
    def print_drinks_cus(self):
        print("\n<음료수 목록>")
        for slot in c.slots_list:
            drink_info = self.find_drink_info(slot.drink_number)
            print(f"{slot.slot_number}. {drink_info.name} {drink_info.price}원 {slot.stock}개")
        print("(0. 뒤로가기)")
        print("-------------------------------------------")
    
    # 돈 처리는 완료되었다고 가정
    def buy_drink(self, slot_number:str):
        target_slot = self.find_slot(slot_number)

        if(target_slot.stock != 0):
            target_slot.stock -= 1
            SlotUtils().update_stock(target_slot.slot_number, target_slot.stock)
        else:
            slots = self.find_slots_with_same_drink_number(target_slot.drink_number)
            for slot in slots:
                if(slot.stock != 0):
                    target_slot = slot
                    target_slot.stock -= 1
                    SlotUtils().update_stock(target_slot.slot_number, target_slot.stock)
                    break
        
        if(target_slot.stock == 0):
            self.check_all_zero(target_slot.drink_number)

    def find_slot(self, slot_number):
            x = int(slot_number)

            for slot in c.slots_list:
                if(slot.slot_number == x):
                    return slot
            return None
    
    def check_all_zero(self, drink_number:int):
        for slot in c.slots_list:
            if(slot.drink_number == drink_number):
                if(slot.stock != 0):
                    return False
        return True

    def check_all_zero(self, drink_number:int):
        slots = list()

        for slot in c.slots_list:
            if(slot.drink_number == drink_number):
                if(slot.stock != 0):
                    SlotUtils().update_stock(slot_number=slot.slot_number, stock=slot.stock - 1)
                    return
                else:
                    slots.append(slot)

        for slot in slots:
            c.slots_list.remove(slot)
        SlotUtils().delete_slots_used_same_drink()
        return

    def find_slots_with_same_drink_number(self, drink_number:int):
        slots = list()
        for slot in c.slots_list:
            if(slot.drink_number == drink_number):
                slots.append(slot)

        return slots

if __name__ == "__main__":
    # 음료수 선택 프롬프트 테스트
    drinkselection = DrinkSelection()

# 37번 권종개수 초과, 잔돈부족 오류 - drink_selection_parser에서 만든 후 추가 예정

