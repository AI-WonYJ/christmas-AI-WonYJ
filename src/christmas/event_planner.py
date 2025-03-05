from discount_calculator import DiscountCalculator

class EventPlanner:
    def __init__(self, date, order):
        self.date = date
        self.order = order
        self.total_price = self.calculate_total_price()
        self.gift = False
        self.benefits = {}
        self.total_benefits = 0
        self.final_price = 0
        self.badge = ""

    def calculate_total_price(self):
        prices = {
            "양송이수프": 6000, "타파스": 5500, "시저샐러드": 8000,
            "티본스테이크": 55000, "바비큐립": 54000, "해산물파스타": 35000, "크리스마스파스타": 25000,
            "초코케이크": 15000, "아이스크림": 5000,
            "제로콜라": 3000, "레드와인": 60000, "샴페인": 25000
        }
        return sum(prices[item] * quantity for item, quantity in self.order.items())

    def calculate_event(self):
        discount = DiscountCalculator(self.date, self.order)
        self.benefits = discount.calculate_discounts()
        self.total_benefits = sum(self.benefits.values())

        self.final_price = self.total_price - self.total_benefits

        if self.total_price >= 120000:
            self.gift = True
            self.total_benefits += 25000
            
        self.assign_badge()

    def assign_badge(self):
        if self.total_benefits >= 20000:
            self.badge = "산타"
            return
        if self.total_benefits >= 10000:
            self.badge = "트리"
            return
        if self.total_benefits >= 5000:
            self.badge = "별"
