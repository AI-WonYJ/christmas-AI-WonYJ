class InputView:
    @staticmethod
    def read_date():
        while True:
            try:
                date = int(input("12월 중 식당 예상 방문 날짜는 언제인가요? (숫자만 입력해 주세요!)\n"))
                if 1 <= date <= 31:
                    return date
                raise ValueError
            except ValueError:
                print("[ERROR] 유호하지 않은 날짜입니다. 다시 입력해 주세요.")

    @staticmethod
    def read_order():
        while True:
            try:
                order_input = input("주문하실 메뉴를 메뉴와 개수를 알려 주세요. (e.g. 해산물파스타-2,레드와인-1,초코케이크-1)\n")
                return order_input
            except ValueError:
                print("[ERROR]")