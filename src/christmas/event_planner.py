"""
12월 이벤트 플래너 프로그램의 이벤트 플래너.
"""

from christmas.discount_calculator import DiscountCalculator


class EventPlanner:
    """이벤트 할인 및 주문을 관리하는 클래스"""

    def __init__(self, date, order):
        """초기화: 방문 날짜, 주문 내역, 총 주문 금액, 할인 정보 설정"""
        self.date = date  # 방문 날짜
        self.order = order  # 주문 내역 (딕셔너리)
        self.total_price = self.calculate_total_price()  # 총 주문 금액
        self.benefits = {}  # 적용된 할인 내역
        self.final_price = 0  # 할인 후 결제 금액
        self.badge = ""  # 이벤트 배지
        self.gift_included = False  # 증정 이벤트 여부 (샴페인)

    def calculate_total_price(self):
        """총 주문 금액을 계산한다."""
        prices = {
            "양송이수프": 6000, "타파스": 5500, "시저샐러드": 8000,
            "티본스테이크": 55000, "바비큐립": 54000, "해산물파스타": 35000, 
            "크리스마스파스타": 25000, "초코케이크": 15000, "아이스크림": 5000,
            "제로콜라": 3000, "레드와인": 60000, "샴페인": 25000
        }
        return sum(prices[item] * quantity for item, quantity in self.order.items())

    def calculate_event(self):
        """모든 할인 및 증정 이벤트 적용 후 최종 결제 금액을 계산한다."""
        # 할인 적용
        discount = DiscountCalculator(self.date, self.order)
        self.benefits = discount.calculate_discounts()

        # 총혜택 금액 계산
        total_benefits = sum(self.benefits.values())

        # 증정 이벤트 적용 (샴페인 25,000원)
        if self.total_price >= 120000:
            self.gift_included = True
            self.benefits["증정 이벤트"] = 25000
            total_benefits += 25000

        # 최종 결제 금액 계산
        self.final_price = self.total_price - total_benefits

        # 이벤트 배지 부여
        self.assign_badge(total_benefits)

    def assign_badge(self, total_benefits):
        """총혜택 금액을 기준으로 이벤트 배지를 부여한다."""
        if total_benefits >= 20000:
            self.badge = "산타"
            return
        if total_benefits >= 10000:
            self.badge = "트리"
            return
        if total_benefits >= 5000:
            self.badge = "별"
