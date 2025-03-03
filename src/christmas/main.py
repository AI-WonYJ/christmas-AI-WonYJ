from input_view import InputView

def main():
    print("안녕하세요! 우테코 식당 12월 이벤트 플래너입니다.")

    date = InputView.read_date()
    order = InputView.read_order()

    print(order)

if __name__ == "__main__":
    main()
