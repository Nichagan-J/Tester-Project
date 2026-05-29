from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_items = page.locator(".cart_item")
    
    def verify_item_in_cart(self, product_name: str) -> bool:
        return self.page.locator(f".inventory_item_name:has-text('{product_name}')").is_visible()
    
    def remove_item(self, product_name: str):
        item = self.page.locator(f".cart_item:has-text('{product_name}')")
        item.locator("button:has-text('Remove')").click()

    def is_cart_empty(self) -> bool:
        return self.cart_items.count() == 0

    def proceed_to_checkout(self):
        self.checkout_button.click()
