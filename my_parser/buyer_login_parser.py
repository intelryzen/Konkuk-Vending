from .base_parser import BaseParser
from config import Config as c
from model.buyer import Buyer
from file_utils.buyer_util import BuyerUtils

'''
구매자 로그인(2차 확장)##
    올바른 입력이 아닙니다.
    아이디가 입력규칙을 준수하지 않습니다.
'''

# 허용 명령어
allows = [0]

class BuyerLoginParser(BaseParser):
    # 반환 형식: (정상 여부[bool], 정상일 경우 뒤로가기(0)나 None을, 비정상일 경우 오류메시지[str], id와 일치하지 않는 경우 파일 업데이트 후 true, none)
    def parse(self, input: str, id: str) -> tuple[bool, any]:
        command = self.parse_command(input)

        # 뒤로가기
        if command in allows:
            return True, command
        
        input = self.parse_all(input)

        if input == None or (len(input) == 1 and input[0] == ""):
            return False, "오류: 올바른 입력이 아닙니다."

        if len(input) == 1 and len(input[0]) <= 10 and self.is_word(input[0]):
            found = False
            for buyer in c.buyer_list:
                if input[0] == buyer.buyer_id:
                    found = True
                    c.logged_in_buyer = input[0]
                    return True, "로그인 성공"

            if not found:
                buyer_utils = BuyerUtils()
                # 아이디가 이미 존재하는지 확인 후 존재하지 않을 때만 아이디 생성
                if not any(buyer.buyer_id == input[0] for buyer in c.buyer_list):
                    success = buyer_utils.insert_buyer(input[0])
                    if success:
                        # 새로운 아이디가 생성되면 c.buyer_list에도 추가
                        new_buyer = Buyer(input[0],0,0)
                        c.buyer_list.append(new_buyer)
                        ''' buyer_list 출력확인
                        for buyer in c.buyer_list:
                            print(buyer)
                        '''
                        c.logged_in_buyer = input[0]
                        return True, f"{input[0]} 아이디를 생성하였습니다."
                    else:
                        return False, "아이디 생성을 실패했습니다."
                else:
                    return False, "아이디가 이미 존재합니다."

        return False, "오류: 아이디가 입력규칙을 준수하지 않습니다."

