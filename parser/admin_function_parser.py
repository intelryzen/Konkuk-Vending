from base_parser import BaseParser
from config import config as c
#config.py import




class AdminFunctionParser(BaseParser):
    def parser(self, input: str ) -> tuple[bool,any]:  
        
        #파일 이름 앞뒤 공백 제거
        drinknum = []  #음료 번호 리스트    
        drinkname = [] #음료 이름 리스트


        #drinklist에서 drinknum , drinkname 분리하기
        numpos = 0
        namepos = 0
        for i in range(len(c.drinks_list)):
            if i%4==0:
                drinknum[numpos] = c.drinks_list[i]
                numpos+=1
            if i%4==1:
                drinkname[namepos] = c.drinks_list[i]
                namepos+=1



        # 입력 문자열 앞뒤 공백 제거
        input = input.strip()
        
        # 명령어와 인자 분리
        parts = input.split()
        
        # 명령어 유효성 검사
        if not parts or not parts[0].isdigit() or not 0 <= int(parts[0]) <= 5:
            return False , "오류 : 올바른 입력이 아닙니다."
        
        command = int(parts[0])
        
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
                    return False , "오류: 2개의 인자가 필요합니다. 첫번째 인자는 번호, 두번째 인자는 개수를 입력해주세요."
                
            # 3번 잔돈 수정 명령어 인자 유효성 검사
            if command == 3:
                if not self.is_money_type(parts[1]):
                    return False , "오류: 권종의 입력은 (100, 500, 1000, 5000, 10000, 50000)만 허용합니다."
                if not self.is_count(parts[2]):
                    return False , "오류: 권종의 개수는 0과 99사이의 숫자만 입력 가능합니다."
                return True,command  #f"{parts[1]}원의 수량이 {parts[2]}개로 변경되었습니다."
            
            # 4번 음료수 재고 수정 명령어 인자 유효성 검사
            if command == 4:
                if not self.is_number(parts[1]):
                    return False , "오류 : 음료수의 번호는 1과 99사이의 숫자만 입력 가능합니다."
                if not parts[1] in drinknum :
                     return False #  "오류: 존재하지 않는 음료수 번호입니다. 자판기에 있는 음료수만 재고를 수정할 수 있습니다."
                if not self.is_count(parts[2]):
                    return False, "오류: 음료수의 개수의 입력은 오직 0과 99사이의 숫자만 허용합니다."
                
                index = drinknum.index(parts[1]) # 음료수 번호에 해당하는 인덱스 찾기
                drink_name = drinkname[index]  # 음료수 이름 찾기

                if not parts[2]==0:
                    return True,command#f"{parts[1]}번 입력한 번호의 {drink_name}의 개수가 {parts[2]}개로 변경되었습니다."
                elif parts[2]==0:
                    return True,command#f"{parts[1]}번 입력한 번호의 {drink_name}가 삭제되었습니다."  #파일 수정해야함

        # 5번 메뉴
        elif command == 5:
            # 5번 메뉴 인자 개수 확인
            if len(parts) != 5:
                return False, "오류: 4개의 인자가 필요합니다. 첫번째 인자는 번호, 두번째 인자는 이름, 세번째 인자는 개수, 네번째 인자는 가격을 입력해주세요.(음료수 추가)"
            
            # 5번 음료수 추가 명령어인자 유효성 검사

            if not self.is_number(parts[1]):
                return False, "오류: 음료수의 번호는 1과 99사이의 숫자만 허용합니다."
            if parts[1] in drinknum :
                return False, "오류: 해당 음료수 번호는 중복되어서 사용할 수 없습니다."
            if not parts[4].isdigit :
                return False, "오류: 음료수의 가격 입력시 숫자만 입력해 주세요."
            if parts[4]<100: 
                return False, "오류: 음료수의 가격은 최소 100원이어야 합니다."
            if parts[4]>1000000: 
                return False, "오류: 음료수의 가격은 1000000원 이하이어야 합니다."
            if parts[4]%100 != 0: 
                return False, "오류: 음료수의 가격은 100의 배수이어야 합니다."
            if not self.is_count(parts[3]):
                return False, "오류: 음료수 개수 입력시 0과 99사이의 숫자만 기입해 주세요."
            return True,command
        
        # 0 입력
        elif command == 0:
            if len(command)!=1 :
                return False, "오류: 인자가 없어야 합니다."
            return True,command# ""
        
 
