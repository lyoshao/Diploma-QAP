"""Страница карточки товара."""

from pages.base_page import BasePage


class ProductPage(BasePage):
    """Карточка товара Wildberries."""

    LOCATORS = {
        "product_name": "h2[class*='mo-typography_variant_title3']",
        "product_price": "span[class*='priceBlockPrice'] ins",
        "add_to_cart_button": "button[aria-label='Добавить в корзину']",
        "buy_now_button": "button[aria-label='Купить сейчас']",
        "favorite_button": "button[class*='toFavourite'][class*='favouriteButton']",
        "show_details_button": "button[class*='btnDetail']",
        "product_characteristics": "div.content--zb_r9",
        "size_list": "ul.sizesList--EwFfe",
        "product_image": "div[class*='imageContainer'] img",
        "cart_link": "span.navbar-pc__notify",
        "rating": "span[class*='productReviewRating']",
        "share_button": "button.btnShare--cdooq",
        "seller_info": "div[class*='sellerInfoNameDefault']",
        "delivery_info": "div[class*='deliveryInfoWrap']",
        "fullscreen_image": "div[class*='mainSlider--Bp49v']",
        "breadcrumbs": "div[class*='breadcrumb'], nav[class*='breadcrumb']",
        "similar_products": "section[class*='cards-list']",
        "reviews_block": "div[class*='productPageUserActivity']",
        "color_slider": "div[class*='swiper--ccyHx']",
        "size_popup": "div[class*='popupNarrow']",
        "popup_close": "button[class*='popup__close']",
    }

    def __init__(self, page):
        super().__init__(page)

    def get_product_name(self) -> str:
        """Получает название товара."""
        try:
            element = self.page.locator(self.LOCATORS["product_name"])
            if element.count() > 0:
                text = element.first.text_content()
                return text.strip() if text else ""
            return ""
        except Exception:
            return ""

    def get_product_price(self) -> str:
        """Получает цену товара."""
        try:
            element = self.page.locator(self.LOCATORS["product_price"])
            if element.count() > 0:
                text = element.first.text_content()
                return text.strip() if text else ""
            return ""
        except Exception:
            return ""

    def add_to_cart(self) -> bool:
        """Добавляет товар в корзину."""
        try:
            button = self.page.locator(self.LOCATORS["add_to_cart_button"])
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1500)
                return True
            return False
        except Exception:
            return False

    def buy_now(self) -> bool:
        """Нажимает на кнопку 'Купить сейчас'."""
        try:
            button = self.page.locator(self.LOCATORS["buy_now_button"])
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def show_details(self) -> bool:
        """Нажимает на кнопку, чтобы показать характеристики."""
        try:
            button = self.page.locator(self.LOCATORS["show_details_button"])
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def get_characteristics(self) -> str:
        """Получает характеристики товара."""
        try:
            self.show_details()
            element = self.page.locator(self.LOCATORS["product_characteristics"])
            if element.count() > 0:
                text = element.first.text_content()
                return text.strip() if text else ""
            return ""
        except Exception:
            return ""

    def is_size_available(self) -> bool:
        """Проверяет, есть ли выбор размера."""
        try:
            size_list = self.page.locator(self.LOCATORS["size_list"])
            return size_list.count() > 0 and size_list.first.is_visible()
        except Exception:
            return False

    def select_size(self, size: str) -> bool:
        """Выбирает размер товара."""
        try:
            sizes = self.page.locator(f"{self.LOCATORS['size_list']} button").all()
            for size_btn in sizes:
                btn_text = size_btn.text_content()
                if btn_text is not None and size in btn_text:
                    size_btn.click()
                    self.page.wait_for_timeout(500)
                    return True
        except Exception:
            return False

    def add_to_favorites(self) -> bool:
        """Добавляет товар в избранное."""
        try:
            button = self.page.locator(self.LOCATORS["favorite_button"])
            if button.count() > 0 and button.first.is_visible():
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def is_favorite_button_visible(self) -> bool:
        """Проверяет, видима ли кнопка 'Добавить в избранное'."""
        try:
            return self.is_element_visible(self.LOCATORS["favorite_button"])
        except Exception:
            return False

    def is_add_to_cart_visible(self) -> bool:
        """Проверяет, видима ли кнопка 'Добавить в корзину'."""
        try:
            return self.is_element_visible(self.LOCATORS["add_to_cart_button"])
        except Exception:
            return False

    def click_product_image(self) -> bool:
        """Кликает по изображению товара."""
        try:
            image = self.page.locator(self.LOCATORS["product_image"])
            if image.count() > 0:
                image.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def is_size_popup_visible(self) -> bool:
        """Проверяет, видима ли плашка с выбором размера."""
        try:
            popup = self.page.locator(self.LOCATORS["size_popup"])
            return popup.count() > 0 and popup.first.is_visible()
        except Exception:
            return False

    def is_cart_opened(self) -> bool:
        """Проверяет, открылась ли корзина."""
        try:
            return "cart" in self.page.url.lower()
        except Exception:
            return False

    def close_size_popup(self) -> bool:
        """Закрывает плашку с выбором размера."""
        try:
            close_button = self.page.locator(self.LOCATORS["popup_close"])
            if close_button.count() > 0:
                close_button.first.click()
                self.page.wait_for_timeout(500)
                return True
            return False
        except Exception:
            return False

    def is_cart_updated(self) -> bool:
        """Проверяет, обновилась ли корзина."""
        try:
            cart_link = self.page.locator(self.LOCATORS["cart_link"])
            return cart_link.count() > 0
        except Exception:
            return False

    def has_product_images(self) -> bool:
        """Проверяет, есть ли изображения товара."""
        try:
            image = self.page.locator(self.LOCATORS["product_image"])
            return image.count() > 0
        except Exception:
            return False

    def is_rating_displayed(self) -> bool:
        """Проверяет, отображается ли рейтинг."""
        try:
            rating = self.page.locator(self.LOCATORS["rating"])
            return rating.count() > 0
        except Exception:
            return False

    def is_share_button_visible(self) -> bool:
        """Проверяет, видима ли кнопка 'Скопировать ссылку'."""
        try:
            share_button = self.page.locator(self.LOCATORS["share_button"])
            return share_button.count() > 0 and share_button.first.is_visible()
        except Exception:
            return False

    def is_seller_info_visible(self) -> bool:
        """Проверяет, отображается ли информация о продавце."""
        try:
            seller = self.page.locator(self.LOCATORS["seller_info"])
            return seller.count() > 0 and seller.first.is_visible()
        except Exception:
            return False

    def is_delivery_info_visible(self) -> bool:
        """Проверяет, отображается ли информация о доставке."""
        try:
            delivery = self.page.locator(self.LOCATORS["delivery_info"])
            return delivery.count() > 0 and delivery.first.is_visible()
        except Exception:
            return False

    def is_fullscreen_image_visible(self) -> bool:
        """Проверяет, открыто ли полноэкранное изображение."""
        try:
            fullscreen = self.page.locator(self.LOCATORS["fullscreen_image"])
            return fullscreen.count() > 0 and fullscreen.first.is_visible()
        except Exception:
            return False

    def are_breadcrumbs_visible(self) -> bool:
        """Проверяет, отображается ли навигационная цепочка."""
        try:
            breadcrumbs = self.page.locator(self.LOCATORS["breadcrumbs"])
            return breadcrumbs.count() > 0
        except Exception:
            return False

    def scroll_to_bottom(self) -> None:
        """Скроллит страницу вниз."""
        self.page.mouse.wheel(0, 1000)
        self.page.wait_for_timeout(2000)

    def is_similar_products_visible(self) -> bool:
        """Проверяет, видим ли блок 'Смотрите также'."""
        try:
            similar = self.page.locator(self.LOCATORS["similar_products"])
            return similar.count() > 0 and similar.first.is_visible()
        except Exception:
            return False

    def are_reviews_visible(self) -> bool:
        """Проверяет, видим ли блок с отзывами."""
        try:
            reviews = self.page.locator(self.LOCATORS["reviews_block"])
            return reviews.count() > 0 and reviews.first.is_visible()
        except Exception:
            return False

    def are_color_options_visible(self) -> bool:
        """Проверяет, есть ли выбор цвета."""
        try:
            color_slider = self.page.locator(self.LOCATORS["color_slider"])
            return color_slider.count() > 0 and color_slider.first.is_visible()
        except Exception:
            return False
