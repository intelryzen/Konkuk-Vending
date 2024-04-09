from base_parser import BaseParser

'''
관리자
    올바른 입력이 아닙니다. 완
    인자가 없어야 합니다. (잔돈확인, 음료수재고확인) 완
    2개의 인자가 필요합니다. 첫번째 인자는 권종, 두번째 인자는 권종 개수를 입력해주세요. (잔돈수정) 완
    권종의 입력은 (100, 500, 1000, 5000, 10000, 50000)만 허용합니다. (잔돈수정) 완
    권종의 개수는 0과 99사이의 숫자만 입력 가능합니다 (잔돈수정) 완
    2개의 인자가 필요합니다. 첫번째 인자는 번호, 두번째 인자는 개수를 입력해주세요. (음료수 재고 수정) 완
    음료수의 번호는 숫자만 입력할 수 있습니다. (음료수 재고 수정) -> 음료수의 번호는 1과 99사이의 숫자만 허용합니다 로 수정  완
    존재하지 않는 음료수 번호입니다. 자판기에 있는 음료수만 재고를 수정할 수 있습니다 (음료수 재고 수정) 완
    음료수의 개수의 입력은 오직 0과 99사이의 숫자만 허용합니다 (음료수 재고 수정) 완
    4개의 인자가 필요합니다. 첫번째 인자는 번호, 두번째 인자는 이름, 세번째 인자는 개수, 네번째 인자는 가격을 입력해주세요. (음료수 추가) 완
    음료수의 번호는 정규식 (0?[1-9])|([1-9][0-9])에 맞춰 입력해야 합니다. (음료수 추가) 완
    해당 음료수 번호는 중복되어서 사용할 수 없습니다. (음료수 추가) 완
    음료수의 가격 입력시 숫자만 입력해 주세요. (음료수 추가) 완
    음료수의 가격은 최소 100원이어야 합니다. (음료수 추가)  완
    해당 음료수 번호는 이미 선점되었습니다. (음료수 추가) -> 오류: 음료수의 가격은 1000000원 이하이어야 합니다. 완
    음료수의 가격은 100의 배수이어야 합니다. (음료수 추가) 완
    음료수 개수 입력시 0과 99사이의 숫자만 기입해 주세요. (음료수 추가) 완
    명령어 0에 해당하는 인자 개수 확인 완
'''


#음료수 번호와 이름 리스트를 어떤 타입으로 받아올지 -> 파일 담당하시는 분과 상의
# 1번 메뉴와 2번 메뉴 정상 수행 결과, 반환 값 설정 -> 프롬프트 담당하는 분과 상의



class AdminFunctionParser(BaseParser):
    def parser(self, input: str , drinkfilename : str) -> tuple[bool, any]:  
        
        #파일 이름 앞뒤 공백 제거
        file_name = drinkfilename.strip()
        drinknum = []  #음료 번호 리스트      #인자로 받아와야함
        drinkname = [] #음료 이름 리스트

        #파일에 있는 음료 번호, 이름 불러오기 > 음료 번호 리스트와 음료 이름 리스트로 받아오기
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # 앞뒤 공백 제거
                cleaned_line = line.strip()
                # 문자열 분리
                sep = cleaned_line.split()
            if len(parts) >= 2:  # 최소한의 번호와 이름이 있는지 확인
                drinknum.append(sep[0]) #번호 리스트 데이터 삽입
                drinkname.append(sep[1]) #이름 리스트 데이터 삽입

        # 입력 문자열 앞뒤 공백 제거
        input = input.strip()
        
        # 명령어와 인자 분리
        parts = input.split()
        
        # 명령어 유효성 검사
        if not parts or not parts[0].isdigit() or not 0 <= int(parts[0]) <= 5:
            return False, "오류 : 올바른 입력이 아닙니다."
        
        command = int(parts[0])
        
        # 각 명령어별 인자 검사

        # 1번 2번 메뉴
        if command in [1, 2]:
            # 1번 2번 메뉴 인자 개수 확인
            if len(parts) > 1:
                return False, "오류 : 인자가 없어야 합니다."
            if command == 1:
                 return True,"권종별 수량을 비싼 권종부터 하나씩 출력"  #프롬프트 하시는 분들에게 물어봐서 편한 방식으로 수정
            if command == 2:
                 return True,"한 행에 음료수의 번호, 이름, 가격, 개수를 출력"
            
        # 3번 4번 메뉴
        elif command in [3, 4]:
            # 3번 4번 메뉴 인자 개수 확인
            if len(parts) != 3:
                if command == 3:
                    return False, "오류: 2개의 인자가 필요합니다. 첫번째 인자는 권종, 두번째 인자는 권종 개수를 입력해주세요."
                if command == 4:
                    return False, "오류: 2개의 인자가 필요합니다. 첫번째 인자는 번호, 두번째 인자는 개수를 입력해주세요."
                
            # 3번 잔돈 수정 명령어 인자 유효성 검사
            if command == 3:
                if not self.is_money_type(parts[1]):
                    return False, "오류: 권종의 입력은 (100, 500, 1000, 5000, 10000, 50000)만 허용합니다."
                if not self.is_count(parts[2]):
                    return False, "오류: 권종의 개수는 0과 99사이의 숫자만 입력 가능합니다."
                return True,f"{parts[1]}원의 수량이 {parts[2]}개로 변경되었습니다."
            
            # 4번 음료수 재고 수정 명령어 인자 유효성 검사
            if command == 4:
                if not self.is_number(parts[1]):
                    return False, "오류 : 음료수의 번호는 1과 99사이의 숫자만 입력 가능합니다."
                if not parts[1] in drinknum :
                     return False, "오류: 존재하지 않는 음료수 번호입니다. 자판기에 있는 음료수만 재고를 수정할 수 있습니다."
                if not self.is_count(parts[2]):
                    return False, "오류: 음료수의 개수의 입력은 오직 0과 99사이의 숫자만 허용합니다."
                
                index = drinknum.index(parts[1]) # 음료수 번호에 해당하는 인덱스 찾기
                drink_name = drinkname[index]  # 음료수 이름 찾기

                if not parts[2]==0:
                    return True,f"{parts[1]}번 입력한 번호의 {drink_name}의 개수가 {parts[2]}개로 변경되었습니다."
                elif parts[2]==0:
                    return True,f"{parts[1]}번 입력한 번호의 {drink_name}가 삭제되었습니다."  #파일 수정해야함

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
            return True,f"{parts[1]}번 {parts[2]}가 개당 {parts[4]}원으로 {parts[3]} 추가되었습니다."
        
        # 0 입력
        elif command == 0:
            if len(command)!=1 :
                return False, "오류: 인자가 없어야 합니다."
            return True, ""
        
 
