class OutputView:
    """ 이벤트 결과를 출력하는 클래스 """

    @staticmethod
    def print_event_summary(planner):
        """ 주문 및 할인 적용 결과를 출력한다. """
        print(f"\n12월 {planner.date}일에 우테코 식당에서 받을 이벤트 혜택 미리 보기!\n")
        
        OutputView.print_order_menu(planner.order)
        OutputView.print_total_price(planner.total_price)
        OutputView.print_gift_menu(planner.gift)
        OutputView.print_benefits(planner.benefits)
        OutputView.print_total_benefits(planner.benefits)
        OutputView.print_final_price(planner.final_price)
        OutputView.print_event_badge(planner.badge)

    @staticmethod
    def print_order_menu(order):
        """ 주문한 메뉴 리스트를 출력한다. """
        print("<주문 메뉴>")
        for item, quantity in order.items():
            print(f"{item} {quantity}개")

    @staticmethod
    def print_total_price(total_price):
        """ 할인 전 총 주문 금액을 출력한다. """
        print("\n<할인 전 총주문 금액>")
        print(f"{total_price:,}원")  # 숫자에 콤마 추가

    @staticmethod
    def print_gift_menu(gift):
        """ 증정 메뉴 여부를 출력한다. """
        print("\n<증정 메뉴>")
        print("샴페인 1개" if gift else "없음")  # 3항 연산자 제거 가능

    @staticmethod
    def print_benefits(benefits):
        """ 혜택 내역을 출력한다. """
        print("\n<혜택 내역>")
        if benefits:
            for benefit, amount in benefits.items():
                print(f"{benefit}: -{amount:,}원")  # 숫자에 콤마 추가
            return
        print("없음")  # 적용된 할인 없을 경우

    @staticmethod
    def print_total_benefits(benefits):
        """ 총혜택 금액을 출력한다. """
        print("\n<총혜택 금액>")
        print(f"-{sum(benefits.values()):,}원" if benefits else "0원")

    @staticmethod
    def print_final_price(final_price):
        """ 할인 후 예상 결제 금액을 출력한다. """
        print("\n<할인 후 예상 결제 금액>")
        print(f"{final_price:,}원")

    @staticmethod
    def print_event_badge(badge):
        """ 12월 이벤트 배지를 출력한다. """
        print("\n<12월 이벤트 배지>")
        print(badge if badge else "없음")  # 3항 연산자 제거 가능
