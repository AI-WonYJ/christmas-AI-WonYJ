class OutputView:
    @staticmethod
    def print_event_summary(planner):
        print(f"\n🎉 12월 {planner.date}일에 우테코 식당에서 받을 이벤트 혜택 미리 보기! 🎉\n")

        print("<주문 메뉴>")
        for item, quantity in planner.order.items():
            print(f"{item} {quantity}개")

        print("\n<할인 전 총주문 금액>")
        print(f"{planner.total_price:,}원")

        print("\n<할인 후 예상 결제 금액>")
        print(f"{planner.total_price:,}원")  # 할인 계산 없이 총 주문 금액 그대로 출력
