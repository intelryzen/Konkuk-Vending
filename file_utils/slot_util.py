import sys
from config import Config as c
from my_parser.base_parser import BaseParser
from model.slot import Slot

class SlotUtils(BaseParser):
    def read(self):
        try:
            with open(c.SLOTS_FILE_PATH, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                drink_nums = set()
                for drink in c.drinks_list:
                    drink_nums.add(drink.drink_number)

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
                        raise ValueError(f"자판기 슬롯 번호에 부합하지 않습니다. {comment}")

                    if not super().is_number(input=data[1]):
                        raise ValueError(f"음료수 번호 (문법)오류가 확인되었습니다. {comment}")

                    if int(data[1]) not in drink_nums:
                        raise ValueError(f"음료수 번호 (의미)오류가 확인되었습니다. {comment}")

                    if not super().is_count(input=data[2]):
                        raise ValueError(f"음료수 개수 오류가 확인되었습니다. {comment}")

                    if any(slot.slot_number == int(data[0]) for slot in c.slots_list):
                        raise ValueError(f"슬롯 번호의 중복이 확인되었습니다. {comment}")

                    c.slots_list.append(Slot(slot_number=int(data[0]), drink_number=int(data[1]), stock=int(data[2])))

                if len(c.slots_list) == 0:
                    print("경고: 자판기 슬롯 파일 내 데이터가 없습니다.")

        except FileNotFoundError:
            print("경고: 자판기 슬롯 파일이 없습니다. 파일을 생성합니다.")
            with open(c.SLOTS_FILE_PATH, 'w', encoding='utf-8'):
                pass
        except Exception as e:
            print(f"오류: {e}")
            sys.exit()
            
    def __read_records(self):
        with open(c.SLOTS_FILE_PATH, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            records = []
            for line in lines:
                record = line.split()
                if line.strip(): 
                    records.append(record)
            return records
    
    def __write_records(self, records):
        with open(c.SLOTS_FILE_PATH, 'w', encoding='utf-8') as file:
            file.writelines([f"{record[0]} {record[1]} {record[2]}\n" for record in records])
        
    def update_stock(self, slot_number:int, stock:int):
        records = self.__read_records()
        
        for record in records:
            if(int(record[0]) == slot_number):
                record[2] = stock
                break

        self.__write_records(records)

    
    def delete_slots_used_same_drink(self, drink_number:int):
        records = self.__read_records()
        records = [record for record in records if int(record[1]) != drink_number]

        self.__write_records(records)

    def delete_slot(self, slot_number:int):
        records = self.__read_records()
        records = [record for record in records if int(record[0]) != slot_number]
        
        self.__write_records(records)

    def insert_slot(self, slot_number:int, drink_number:int, stock:int):
        records = self.__read_records()
        records.append([slot_number, drink_number, stock])
        
        self.__write_records(records)
