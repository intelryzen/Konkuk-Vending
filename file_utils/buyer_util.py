import sys
from config import config as c
from my_parser.base_parser import BaseParser
from model.buyer import Buyer

class BuyerUtils(BaseParser):
    def read(self):
        try:
            with open(c.BUYER_FILE_PATH, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                for line in lines:
                    data = line.split()
                    comment = f"{line}\n"
                    
                    if not line.strip():  # 공백줄 무시
                        continue

                    if not line.endswith('\n'):
                        raise ValueError(f"행 끝에 개행이 없습니다. {comment}")
                    
                    if len(data) != 3:
                        raise ValueError(f"행의 데이터 개수가 맞지 않습니다. {comment}")

                    if not super().is_id(input=data[0]):
                        raise ValueError(f"아이디에 부합하지 않습니다. {comment}")

                    if not super().is_mileage(input=data[1]):
                        raise ValueError(f"마일리지 타입이 아닙니다. {comment}")

                    if not super().is_count(input=data[2]):
                        raise ValueError(f"쿠폰의 <개수>가 문법 규칙을 위반하였습니다. {comment}")

                    if any(buyer.buyer_id == data[0] for buyer in c.buyer_list):
                        raise ValueError(f"사용자 아이디의 중복이 확인되었습니다. {comment}")

                    c.buyer_list.append(Buyer(buyer_id=data[0], money=int(data[1]), coupon_number=int(data[2])))

                if len(c.buyer_list) == 0:
                    print("경고: 구매자 정보 파일 내 데이터가 없습니다.")

        except FileNotFoundError:
            print("경고: 구매자 정보 파일이 없습니다. 파일을 생성합니다.")
            with open(c.BUYER_FILE_PATH, 'w', encoding='utf-8'):
                pass
        except Exception as e:
            print(f"오류: {e}")
            sys.exit()
            
    def __read_records(self):
        with open(c.BUYER_FILE_PATH, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            records = []
            for line in lines:
                record = line.split()
                if line.strip(): 
                    records.append(record)
            return records
    
    def __write_records(self, records):
        with open(c.BUYER_FILE_PATH, 'w', encoding='utf-8') as file:
            file.writelines([f"{record[0]} {record[1]} {record[2]}\n" for record in records])
        
    def update_money_coupon(self, buyer_id:str, money:int, coupon_number:int):
        records = self.__read_records()
        
        for record in records:
            if(record[0] == buyer_id):
                record[1] = money
                record[2] = coupon_number
                break

        self.__write_records(records)
    '''
    def insert_buyer(self, buyer_id:str):
        records = self.__read_records()
        records.append([buyer_id, 0, 0])

        self.__write_records(records)
    '''
    def insert_buyer(self, buyer_id: str) -> bool:
        try:
            records = self.__read_records()
            records.append([buyer_id, 0, 0])
            self.__write_records(records)
            return True 
        except Exception as e:
            return False
