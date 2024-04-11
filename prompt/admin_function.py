class Admin:
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
        self.admin_prompt()

    # 관리자 프롬프트
    def admin_prompt(self):
        while True:
            print("\n<관리자>")
            print("1. 잔돈 확인")
            print("2. 음료수 재고 확인")
            print("3. 잔돈 수정")
            print("4. 음료수 재고 수정")
            print("5. 음료수 추가")
            print("(0.로그아웃)")
            print("-------------------------------------------")
            admin_input = input(">>>")

            is_valid, result = self.parser.parser(admin_input)

            if is_valid:
                if command == '1':
                    # 잔돈 목록 출력, 비싼 권종에서 싼 권종 순으로
                    sorted_currency_list = sorted(currency_list, key=lambda x: x.value, reverse=True)
                    for Currency in sorted_currency_list:
                        print(f"{Currency.value}원 {Currency.quantity}개")
                    
                elif command == '2':
                    # 음료수 재고 확인 기능 구현 1번 부터 정렬
                    sorted_drink_list = sorted(drink_list, key=lambda x: x.number)
                    for Drink in sorted_drink_list:
                        print(f"{Drink.number} {Drink.name} {Drink.quantity}개 {Drink.value}원")
                elif command == '3':
                    # 잔돈 수정 기능 구현
                    currency_value = int(parts[1])
                    currency_amount = int(parts[2])
                    result = self.change_currency(currency_list, Currency, currency_value, currency_amount)
                    print(result)
                elif command == '4':
                    # 음료수 재고 수정 기능 구현
                    drink_stock = int(parts[2])
                    result = self.change_currency(drink_list, Drink, drink_stock)
                    print(result)
                elif command == '5':
                    # 음료수 추가 기능 구현
                    drink_stock = int(parts[1])
                    drink_stock = str(parts[2])
                    drink_stock = int(parts[3])
                    drink_stock = int(parts[4])
                    result = self.change_currency(drink_list, Drink, drink_stock)
                    print(result)
                elif command == '0':
                    Mode() # 입력 0이면 모드 선택 프롬프트로 이동
            else:
                print(result)  # 오류 메시지 출력
                continue

# 관리자 프롬프트 테스트
Admin()
