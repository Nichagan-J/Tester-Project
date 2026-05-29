from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
    
    def get_product_item(self, product_name: str):
        return self.page.locator(f".inventory_item:has-text('{product_name}')")
    
    def add_to_cart(self, product_name: str):
        item = self.get_product_item(product_name)
        item.locator("button:has-text('Add to cart')").click()

    def remove_from_cart(self, product_name: str):
        item = self.get_product_item(product_name)
        item.locator("button:has-text('Remove')").click()

    def sort_products_by(self, option_value: str):
        self.sort_dropdown.select_option(value=option_value)

    def get_all_product_prices(self):
        prices_text = self.page.locator(".inventory_item_price").all_inner_texts()
        # Convert text like "$29.99" to float 29.99
        return [float(price.replace('$', '')) for price in prices_text]
    
    def go_to_cart(self):
        self.cart_icon.click()
