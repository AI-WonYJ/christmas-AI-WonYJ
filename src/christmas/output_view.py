class OutputView:
    @staticmethod
    def print_event_summary(date, order):
        print(f"12월 {date}일에 우테코 식당에서 받을 이벤트 혜택 미리 보기!\n")

        print("<주문 메뉴>")
        for i in order:
            print(f"temp n개")

        print(f"\n<할인 전 총주문 금액>\n temp원")
        print(f"\n<증정 메뉴>\n")
        print(f"\n<혜택 내역>\n")
        print(f"\n<총혜택 금액>\n")
        print(f"\n<할인 후 예상 결제 금액>\n")
        print(f"\n<12월 이벤트 배지>\n")