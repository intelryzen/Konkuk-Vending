import sys
from config import config as c

def main():
    while(True):
        # 자판기(vending) 인스턴스 생성
            # 자판기가 파일 데이터를 가져와 초기값 저장. 물론 파일을 디코딩하면서 오류생기면 오류문구 출력 후 종료 (클래스가 직접 가져오던, 먼저 가져와서 자판기 클래스의 초기값을 주던 상관없을 것 같습니다.)
        
        # 모드 프롬프트를 호출
            # 모드 프롬프트 내 반복문 
            # 올바른 입력을 받을 때까지 계속 반복 수행함. (ex. 1(관리자 로그인) 또는 2(음료수 보기)를 리턴)
        # 모드 프롬프트에서 반환한 값을 바탕으로 관리자 로그인 또는 금액 입력 프롬프트 호출
            # ...
        i = input(c.cashFilePath)
        exit()

# 강제 종료
def exit():
    sys.exit()

# 메인 호출
if __name__ == "__main__":
    main()
