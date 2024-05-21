import re

'''
공통으로 사용되는 파서 기능이 있다면 본 base 클래스에서 정의 및 구현하고, 각 프롬프트별 파서가 해당 클래스를 상속
'''

'''
모드, 금액 입력, 음료수 선택, 관리자, 관리자 로그인
    올바른 입력이 아닙니다.
음료수 선택
    금액이 부족합니다. 다른 음료수를 선택해주세요.
    잔돈이 부족합니다.
    잔돈이 포화상태입니다. 관리자에게 문의하거나 타 권종을 이용해주세요.
구매자 로그인(2차 확장)##
    올바른 입력이 아닙니다.
    아이디가 입력규칙을 준수하지 않습니다.
금액 입력(2차 수정)##
    올바른 입력이 아닙니다.
    권종 개수 짝이 안맞을 때 -> 오류, 권종 개수가 섞여있을 때 -> 오류
음료수 선택(2차 수정)##
    올바른 입력이 아닙니다.
    금액이 부족합니다. 다른 음료수를 선택해주세요.
    잔돈이 부족합니다.
쿠폰 입력 프롬프트(2차 확장)##
    올바른 입력이 아닙니다.
    y -> 거스름돈이 부족합니다. 관리자에게 문의하거나 타 음료수를 선택해주세요.
    n -> 거스름돈이 부족합니다. 관리자에게 문의하거나 타 음료수를 선택해주세요.
    쿠폰 사용 후 -> 금액이 부족합니다. 다른 음료수를 선택해주세요.
    쿠폰 사용 X -> 금액이 부족합니다. 다른 음료수를 선택해주세요.
    쿠폰이 포화상태입니다. 쿠폰을 사용하시거나 다른 음료수를 선택해주세요.
관리자 로그인
    올바른 입력이 아닙니다.
    아이디와 비밀번호를 구분하여 입력해주세요. 아이디와 비밀번호 사이에는 적어도 하나의 횡공백류열이 필요합니다.
    아이디 또는 비밀번호가 입력규칙을 준수하지 않습니다.
    아이디 또는 비밀번호가 일치하지 않습니다.
관리자 (명령어별 분리) (2차 수정)##
1,2(잔돈확인, 음료수 슬롯별 재고 확인)    
    인자가 없어야 합니다.
3(잔돈수정)
    2개의 인자가 필요합니다. 첫번째 인자는 권종, 두번째 인자는 권종 개수를 입력해주세요. 
    권종의 입력은 (100, 500, 1000, 5000, 10000, 50000)만 허용합니다.
    권종의 개수는 0과 99사이의 숫자만 입력 가능합니다
4(슬롯별 음료수 재고 수정)##
    2개의 인자가 필요합니다. 첫번째 인자는 슬롯 번호, 두번째 인자는 개수를 입력해주세요. 
    음료수의 슬롯 번호는 숫자만 입력할 수 있습니다.
    존재하지 않는 슬롯 번호입니다. 사용하는 슬롯만 재고를 수정할 수 있습니다.
    음료수의 개수의 입력은 오직 0과 99사이의 숫자만 허용합니다.
5(자판기 슬롯에 음료수 할당 추가)##
    3개의 인자가 필요합니다. 첫번째 인자는 슬롯 번호, 두번째 인자는 음료수 번호, 세번째 인자는 개수를 입력해주세요.
    슬롯 번호는 1과 99사이의 숫자만 허용합니다.
    음료수 번호는 1과 99사이의 숫자만 허용합니다.
    해당 음료수 번호는 존재하지 않습니다.
    해당 슬롯 번호는 중복되어서 사용할 수 없습니다.
    음료수 개수 입력시 0과 99사이의 숫자만 기입해 주세요.
6(음료수 정보 추가)##
    3개의 인자가 필요합니다. 첫번째 인자는 음료수 번호, 두번째 인자는 이름, 세번째 인자는 가격을 입력해주세요.
    음료수 번호는 1과 99사이의 숫자만 허용합니다.
    해당 음료수 번호는 중복되어서 사용할 수 없습니다.
    음료수의 가격 입력시 숫자만 입력해 주세요. 
    음료수의 가격은 최소 100원이어야 합니다.
    음료수의 가격은 1000000원 이하이어야 합니다.
    음료수의 가격은 100의 배수이어야 합니다.
7(음료수 정보 삭제)##
    1개의 인자가 필요합니다. 인자는 음료수 번호를 입력해주세요.
    음료수 번호는 1과 99사이의 숫자만 허용합니다.
    해당 음료수 번호는 존재하지 않습니다.
'''
class BaseParser():

    # 올바른 '권종'인지 확인 (50000|10000|5000|1000|500|100)
    def is_money_type(self, input: str) -> bool:
        return str(input) in ['50000', '10000', '5000', '1000', '500', '100']
    
    # 올바른 '개수'인지 확인 (0?[0-9])|([1-9][0-9])
    def is_count(self, input: str) -> bool:
        pattern = r'^(0?[0-9]|[1-9][0-9])$'
        return re.match(pattern, input)
    
    # 올바른 '번호'인지 확인 (0?[1-9])|([1-9][0-9])
    def is_number(self, input: str) -> bool:
        pattern = r'^(0?[1-9]|[1-9][0-9])$'
        return re.match(pattern, input)
    
    def is_id(self, input: str) -> bool:
        return len(input) <= 10 and self.is_word(input)
    
    def is_price(self, input: str) -> bool:
        pattern = r'^(1000000|[1-9][0-9]{0,3}00)$'
        return re.match(pattern, input)
    
    def is_mileage(self, input: str) -> bool:
        pattern = r'^(0|1000000|[1-9][0-9]{0,3}00)$'
        return re.match(pattern, input) and int(input) < 10000
    
    # 개행이 포함되어 있는지 확인
    def contains_newline(self, input: str):
        if '\n' in input:
            return True
        return False
    
    # 단어인지 확인
    def is_word(self, input: str) -> bool:
        return input.isprintable() and not any(c in input for c in " \n\t")
    
    #모든 속성이 0인지 확인
    def is_all_quantity_zero(self, input : list, Currency) -> bool:
        for Currency in input:
            if Currency.quantity != 0:
                return False  # 하나라도 quantity가 0이 아니면 False 반환
        return True

    # 한 자리 수 숫자인지
    def is_digit_0_to_9(self, input: str) -> bool:
        pattern = r'^[0-9]$'
        return re.match(pattern, input) is not None

    # 〈횡공백류열0〉 〈명령어〉 〈횡공백류열0〉
    def parse_command(self, input: str) -> int:
        if self.contains_newline(input):
            return -1
        
        input = input.strip()
        if self.is_digit_0_to_9(input):
            return int(input)
        else:
            return -1

    # 〈횡공백류열0〉 <단어> 〈횡공백류열1〉 〈단어〉 (〈횡공백류열1〉 〈단어〉)^* 〈횡공백류열0〉
    def parse_all(self, input: str) -> list:
        if self.contains_newline(input):
            return None

        pattern = r"[\s\t\v\f]+"
        
        # 〈횡공백류열1〉를 기준으로 분할
        parts = re.split(pattern, input.strip())
        
        # 받은 쪽에서 [''] 경우와 \n 처리해줘야 함.
        return parts

# 테스트
if __name__ == "__main__":
    parser = BaseParser()
    test_input = "   \t\f\v명령어 \v\f\t권종  \f\v\t3   \t"
    t = parser.parse_all(test_input)
    print(t)
