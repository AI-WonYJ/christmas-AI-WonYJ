class DiscountCalculator:
    """ 주문에 대한 다양한 할인 적용을 수행하는 클래스 """

    def __init__(self, date, order):
        """ 할인 계산을 위한 초기화. """
        self.date = date
        self.order = order
        self.benefits = {}

    def calculate_discounts(self):
        """ 모든 할인 적용을 수행한 후, 할인 내역을 반환한다. """
        self.apply_christmas_discount()
        self.apply_weekday_weekend_discount()
        self.apply_special_discount()
        return self.benefits

    def apply_christmas_discount(self):
        """ 크리스마스 디데이 할인 적용 (12월 1일 ~ 25일). """
        if 1 <= self.date <= 25:
            self.benefits["크리스마스 디데이 할인"] = 900 + (self.date * 100)

    def apply_weekday_weekend_discount(self):
        """ 평일 및 주말 할인 적용. """
        if self.date % 7 in [0, 1, 2, 3, 4]:
            discount = sum(self.order.get(d, 0) * 2023 for d in ["초코케이크", "아이스크림"])
            if discount:
                self.benefits["평일 할인"] = discount
            return

        discount = sum(self.order.get(m, 0) * 2023 for m in ["티본스테이크", "바비큐립", "해산물파스타", "크리스마스파스타"])
        if discount:
            self.benefits["주말 할인"] = discount

    def apply_special_discount(self):
        """ 특별 할인 적용 (달력에 별이 있는 날). """
        if self.date not in [3, 10, 17, 24, 25, 31]:
            return

        self.benefits["특별 할인"] = 1000