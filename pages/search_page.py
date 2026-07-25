"""Страница результатов поиска."""

from pages.base_page import BasePage


class SearchPage(BasePage):
    """Страница результатов поиска Wildberries."""

    LOCATORS = {
        "product_cards": "article.product-card",
        "product_titles": "span.product-card__name",
        "filter_button": "button.dropdown-filter__btn--all",
        "filters_container": "div[class*='filters-desktop']",
        "product_list": "div.product-card-list",
        "autocomplete": "div.autocomplete.search-catalog__autocomplete",
        "results_count": "span.searching-results__count",
    }

    def __init__(self, page):
        super().__init__(page)

    def get_products_count(self) -> int:
        """Возвращает количество найденных товаров."""
        try:
            container = self.page.locator(self.LOCATORS["product_list"])
            if container.count() > 0:
                return container.locator("article.product-card").count()
            return self.page.locator(self.LOCATORS["product_cards"]).count()
        except Exception:
            return 0

    def get_first_product_title(self) -> str:
        """Возвращает название первого товара."""
        try:
            if self.get_products_count() > 0:
                return self.get_text(self.LOCATORS["product_titles"])
        except Exception:
            pass
        return ""

    def get_product_titles_list(self) -> list:
        """Возвращает список названий всех товаров."""
        try:
            titles = self.page.locator(self.LOCATORS["product_titles"]).all()
            result = []
            for title in titles:
                text = title.text_content()
                if text and len(text.strip()) > 0:
                    result.append(text.strip())
            return result
        except Exception:
            return []

    def click_first_product(self) -> None:
        """Кликает на первый товар в результатах поиска."""
        try:
            if self.get_products_count() > 0:
                self.page.locator(self.LOCATORS["product_cards"]).first.click()
                self.page.wait_for_load_state("domcontentloaded")
                self.page.wait_for_timeout(5000)
        except Exception:
            pass

    def open_filters(self) -> bool:
        """Открывает панель фильтров."""
        try:
            button = self.page.locator(self.LOCATORS["filter_button"])
            if button.count() > 0:
                button.first.click()
                self.page.wait_for_timeout(1000)
                return True
            return False
        except Exception:
            return False

    def is_filters_visible(self) -> bool:
        """Проверяет, видимы ли фильтры."""
        try:
            container = self.page.locator(self.LOCATORS["filters_container"])
            return container.count() > 0 and container.first.is_visible()
        except Exception:
            return False

    def get_filter_count(self) -> int:
        """Возвращает количество доступных фильтров."""
        try:
            container = self.page.locator(self.LOCATORS["filters_container"])
            if container.count() > 0:
                return container.locator("a, button, label").count()
            return 0
        except Exception:
            return 0

    def is_autocomplete_visible(self) -> bool:
        """Проверяет, видимо ли автодополнение."""
        try:
            autocomplete = self.page.locator(self.LOCATORS["autocomplete"])
            return autocomplete.count() > 0 and autocomplete.first.is_visible()
        except Exception:
            return False

    def get_results_count_text(self) -> str:
        """Возвращает текст с количеством результатов."""
        try:
            return self.get_text(self.LOCATORS["results_count"])
        except Exception:
            return ""

    def scroll_down(self, amount: int = 1000) -> None:
        """Скроллит страницу вниз."""
        self.page.mouse.wheel(0, amount)
        self.page.wait_for_timeout(1000)
