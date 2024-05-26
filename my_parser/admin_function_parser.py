from my_parser.base_parser import BaseParser
from config import Config as c



allows = [0,1,2,3,4,5,6,7] ##0~7 까지 명령어
class AdminFunctionParser(BaseParser):
    def parser(self, input: str ) -> tuple[bool,any]:  
        
        
        drinknum = []  #음료 번호 리스트    
        s_num = [] ## 슬롯 번호 리스트
        s_drink_num = [] ##슬롯에 있는 음료 번호 리스트
        
        

        #drinklist에서 drinknum , drinkname 분리하기
        for i in range(len(c.drinks_list)):
                drinknum.append(c.drinks_list[i].drink_number)  # .append()를 사용하여 값을 추가
        
        #슬롯의 정보 가져오기
        for i in range(len(c.slots_list)):
                s_num.append(c.slots_list[i].slot_number)
                s_drink_num.append(c.slots_list[i].drink_number)  
        

        # 입력 문자열 앞뒤 공백 제거
        input = input.strip()
        
        # 명령어와 인자 분리
        parts = input.split()
        
        # 명령어 유효성 검사
        if not parts:
            return False, "오류: 올바른 입력이 아닙니다."
        
        command = self.parse_command(parts[0])
        if command not in allows:
            return False, "오류: 올바른 입력이 아닙니다."
        # 각 명령어별 인자 검사

        # 1번 2번 메뉴
        if command in [1, 2]:
            # 1번 2번 메뉴 인자 개수 확인
            if len(parts) > 1:
                return False , "오류 : 인자가 없어야 합니다."
            else :
                return True,command
            
        # 3번 4번 메뉴
        elif command in [3, 4]:
            # 3번 4번 메뉴 인자 개수 확인
            if len(parts) != 3:
                if command == 3:
                    return False , "오류: 2개의 인자가 필요합니다. 첫번째 인자는 권종, 두번째 인자는 권종 개수를 입력해주세요."
                if command == 4:
                    return False , "오류: 2개의 인자가 필요합니다. 첫번째 인자는 슬롯 번호, 두번째 인자는 개수를 입력해주세요."
                
            # 3번 잔돈 수정 명령어 인자 유효성 검사
            if command == 3:
                if not self.is_money_type(parts[1]):
                    return False , "오류: 권종의 입력은 (100, 500, 1000, 5000, 10000, 50000)만 허용합니다."
                if not self.is_count(parts[2]):
                    return False , "오류: 권종의 개수는 0과 99사이의 숫자만 입력 가능합니다."
                return True,command  #f"{parts[1]}원의 수량이 {parts[2]}개로 변경되었습니다."
            
            # 4번 자판기 슬롯별 음료수 재고 수정 인자 유효성 검사
            if command == 4:
                if not self.is_number(parts[1]):
                    return False , "오류 : 음료수의 슬롯 번호는 숫자만 입력할 수 있습니다." # 0이어도 오류로 인식2
                if not(int(parts[1]) in s_num) :
                     return False, "오류: 존재하지 않는 음료수 슬롯 번호입니다. 사용하는 슬롯만 재고를 수정할 수 있습니다."
                if not self.is_count(parts[2]):
                    return False, "오류: 음료수의 개수의 입력은 오직 0과 99사이의 숫자만 허용합니다."
                return True,command
              


        # 0 입력
        elif command == 0:
            if len(parts)!=1 :
                return False, "오류: 인자가 없어야 합니다."
            return True,command# ""
        
        # 5번 6번 메뉴
        elif command in [5,6]:
            # 5,6번 메뉴 인자 개수 확인
            if len(parts) != 4:
                if command == 5:
                    return False, "오류: 3개의 인자가 필요합니다. 첫번째 인자는 슬롯 번호, 두번째 인자는 음료수 번호, 세번째 인자는 개수를 입력해주세요."
                elif command == 6:
                    return False,"오류: 3개의 인자가 필요합니다. 첫번째 인자는 음료수 번호, 두번째 인자는 이름, 세번째 인자는 가격을 입력해주세요."
            
            # 5번 자판기 슬롯에 음료수 할당 인자 유효성 검사
            if command == 5:
                if not self.is_number(parts[1]):
                    return False, "오류: 음료수의 슬롯 번호는 1과 99사이의 숫자만 허용합니다."
                if not self.is_number(parts[2]):
                    return False, "오류: 음료수의 번호는 1과 99사이의 숫자만 허용합니다."
                if not int(parts[2]) in drinknum :   
                    return False, "오류 : 해당 음료수 번호는 존재하지 않습니다."
                if int(parts[1]) in s_num :
                    return False, "오류: 해당 슬롯 번호는 중복되어서 사용할 수 없습니다."
                if not self.is_count(parts[3]):
                    return False, "오류: 음료수 개수 입력시 0과 99사이의 숫자만 기입해 주세요."
                return True,command
            # 6번  음료수 정보 추가 명령어 인자 유효성 검사
            if command == 6:
                if not self.is_number(parts[1]):
                    return False, "오류 : 음료수 번호는 1과 99사이의 숫자만 허용합니다."
                if int(parts[1]) in drinknum :
                    return False, "오류: 해당 음료수 번호는 중복되어서 사용할 수 없습니다."
                if not parts[3].isdecimal() :
                    return False, "오류: 음료수의 가격 입력시 숫자만 입력해 주세요."
                price = int(parts[3])
                if price<100: 
                    return False, "오류: 음료수의 가격은 최소 100원이어야 합니다."
                if price>1000000: 
                    return False, "오류: 음료수의 가격은 1000000원 이하이어야 합니다."
                if price%100 != 0: 
                    return False, "오류: 음료수의 가격은 100의 배수이어야 합니다."
                return True,command
          
        elif command == 7:
            # 1번 2번 메뉴 인자 개수 확인
            if not len(parts) == 2:
                return False , "오류: 1개의 인자가 필요합니다. 인자는 음료수 번호를 입력해주세요."
            if not self.is_number(parts[1]):
                return False, "오류 : 음료수 번호는 1과 99사이의 숫자만 허용합니다."
            if not int(parts[1]) in drinknum :   
                return False, "오류 : 해당 음료수 번호는 존재하지 않습니다."
            return True,command
 
