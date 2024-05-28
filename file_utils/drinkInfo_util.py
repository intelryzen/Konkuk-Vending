import sys

from config import Config as c
from my_parser.base_parser import BaseParser
from model.drink_info import Drink_info

class DrinkInfoUtils(BaseParser):
    def read(self):
        try:
            with open(c.DRINKS_FILE_PATH, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                drink_nums = set()

                for line in lines:
                    data = line.split()
                    comment = f"{line}\n"
                    
                    if not line.strip():  # 공백줄 무시
                        continue

                    if not line.endswith('\n'):
                        raise ValueError(f"행 끝에 개행이 없습니다. {comment}")
                    
                    if len(data) != 3:
                        raise ValueError(f"행의 데이터 개수가 맞지 않습니다. {comment}")

                    if not super().is_number(input=data[0]):
                        raise ValueError(f"음료수 번호에 부합하지 않습니다. {comment}")
                    
                    if not super().is_word(input=data[1]):  
                        raise ValueError(f"음료수 이름 (문법)오류가 확인되었습니다. {comment}")
                      
                    if not super().is_price(input=data[2]):  
                        raise ValueError(f"음료수 가격 오류가 확인되었습니다. {comment}")
                   
                    if any(drink.drink_number == int(data[0]) for drink in c.drinks_list): 
                        raise ValueError(f"음료수 번호의 중복이 확인되었습니다. {comment}")
                   
                    c.drinks_list.append(Drink_info(drink_number=int(data[0]), name=data[1], price=int(data[2]))) 

                if len(c.drinks_list) == 0:
                    print("경고: 자판기 슬롯 파일 내 데이터가 없습니다.")

        except FileNotFoundError:
            print("경고: 음료수 정보 파일이 없습니다. 파일을 생성합니다.")
            with open(c.DRINKS_FILE_PATH, 'w', encoding='utf-8'):
                pass
        except Exception as e:
            print(f"오류: {e}")
            sys.exit()
           
    def __read_drinks_records(self):
        with open(c.DRINKS_FILE_PATH, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            records = []
            for line in lines:
                record = line.split()
                if line.strip(): 
                    records.append(record)
            return records

    def __write_drinks_records(self, records):
        with open(c.DRINKS_FILE_PATH, 'w') as file:
            file.writelines([f"{record[0]} {record[1]} {record[2]}\n" for record in records])

    def delete_drink(self, drink_num:int):
        records = self.__read_drinks_records()
        records = [record for record in records if int(record[0]) != drink_num]
        self.__write_drinks_records(records)

    def update_new_drinks(self, drink_num:int, drink_name:str, price:int):
        records = self.__read_drinks_records()
        new_drink = [str(drink_num), drink_name, str(price)] 
        records.append(new_drink)
        self.__write_drinks_records(records)
