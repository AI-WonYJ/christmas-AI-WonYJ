class InputView:
    def read_date():
        while True:
            try:
                date = int(input("12월 중 식당 예상 방문 날짜는 언제인가요? (숫자만 입력해 주세요!)\n"))
                if 1 <= date <= 31:
                    return date
                raise ValueError
            except ValueError:
                print("[ERROR] 유호하지 않은 날짜입니다. 다시 입력해 주세요.")