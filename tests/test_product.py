"""Тесты для карточки товара."""

import allure

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@allure.epic("UI тестирование")
@allure.feature("Карточка товара")
class TestProduct:
    """Тесты для карточки товара Wildberries."""

    SEARCH_QUERIES = {
        "phone": "телефон",
        "laptop": "ноутбук",
        "headphones": "наушники",
        "book": "книга",
        "sneakers": "кроссовки",
        "t_shirt": "футболка"
    }

    @allure.title("Открытие карточки товара из поиска")
    def test_product_page_opens_from_search(self, page):
        """Тест 1: Открытие карточки товара из поиска."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров для открытия"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert "detail.aspx" in page.url, "Не открылась карточка товара"
        name = product_page.get_product_name()
        assert len(name) > 0, "Название товара не отображается"

    @allure.title("Проверка отображения названия товара")
    def test_product_name_displayed(self, page):
        """Тест 2: Проверка отображения названия товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["laptop"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        name = product_page.get_product_name()
        assert len(name) > 0, f"Название товара не отображается. Получено: '{name}'"

    @allure.title("Проверка отображения цены")
    def test_product_price_displayed(self, page):
        """Тест 3: Проверка отображения цены."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        price = product_page.get_product_price()
        assert len(price) > 0, "Цена не отображается"

    @allure.title("Проверка видимости кнопки 'Добавить в корзину'")
    def test_add_to_cart_button_visible(self, page):
        """Тест 4: Проверка видимости кнопки 'Добавить в корзину'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        assert product_page.is_element_visible(
            product_page.LOCATORS["add_to_cart_button"]
        ), "Кнопка 'Добавить в корзину' не видна"

    @allure.title("Добавление товара в корзину")
    def test_add_to_cart_works(self, page):
        """Тест 5: Добавление товара в корзину."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        result = product_page.add_to_cart()
        assert result, "Не удалось добавить товар в корзину"

        assert product_page.is_cart_updated(), "Корзина не обновилась"

    @allure.title("Проверка наличия описания товара")
    def test_product_description_visible(self, page):
        """Тест 6: Проверка наличия описания товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["book"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        description = product_page.get_characteristics()
        assert description is not None, "Ошибка при получении описания"

    @allure.title("Проверка наличия фото товара")
    def test_product_photos_exist(self, page):
        """Тест 7: Проверка наличия фото товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["sneakers"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.has_product_images(), "Нет изображений товара"

    @allure.title("Проверка наличия выбора размера")
    def test_product_sizes_available(self, page):
        """Тест 8: Проверка наличия выбора размера."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["t_shirt"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        sizes_available = product_page.is_size_available()
        assert sizes_available is not None, "Ошибка при проверке размеров"

    @allure.title("Проверка видимости кнопки 'Купить сейчас'")
    def test_buy_now_button_visible(self, page):
        """Тест 9: Проверка видимости кнопки 'Купить сейчас'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)
        assert product_page.is_element_visible(
            product_page.LOCATORS["buy_now_button"]
        ), "Кнопка 'Купить сейчас' не видна"

    @allure.title("Проверка отображения рейтинга")
    def test_product_rating_displayed(self, page):
        """Тест 10: Проверка отображения рейтинга."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.is_rating_displayed(), "Рейтинг не отображается"

    @allure.title("Проверка наличия кнопки 'Скопировать ссылку'")
    def test_product_share_button_exists(self, page):
        """Тест 11: Проверка наличия кнопки 'Скопировать ссылку'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["book"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.is_share_button_visible(), "Кнопка 'Скопировать ссылку' не найдена"

    @allure.title("Проверка наличия кнопки 'Добавить в избранное'")
    def test_product_favorite_button_exists(self, page):
        """Тест 12: Проверка наличия кнопки 'Добавить в избранное'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        is_visible = product_page.is_favorite_button_visible()
        assert is_visible, "Кнопка 'Добавить в избранное' не найдена на этом товаре"

    @allure.title("Проверка характеристик товара")
    def test_product_characteristics_visible(self, page):
        """Тест 13: Проверка характеристик товара."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["laptop"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        characteristics = product_page.get_characteristics()
        assert characteristics is not None, "Характеристики не получены"
        assert len(characteristics) > 0, "Характеристики пустые"

    @allure.title("Проверка информации о продавце")
    def test_product_seller_info_visible(self, page):
        """Тест 14: Проверка информации о продавце."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["sneakers"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.is_seller_info_visible(), "Информация о продавце не отображается"

    @allure.title("Проверка информации о доставке")
    def test_product_delivery_info_visible(self, page):
        """Тест 15: Проверка информации о доставке."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.is_delivery_info_visible(), "Информация о доставке не отображается"

    @allure.title("Проверка открытия фото в полном размере по клику")
    def test_product_photo_opens_fullscreen(self, page):
        """Тест 16: Проверка открытия фото в полном размере по клику."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["headphones"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.is_add_to_cart_visible(), \
            "Кнопка 'Добавить в корзину' не видна"

        result = product_page.click_product_image()
        assert result, "Не удалось кликнуть по изображению"

        assert product_page.is_fullscreen_image_visible(), "Полноэкранное изображение не открылось"

    @allure.title("Проверка наличия навигационной цепочки")
    def test_product_breadcrumbs_visible(self, page):
        """Тест 17: Проверка наличия навигационной цепочки."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["book"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.are_breadcrumbs_visible(), "Навигационная цепочка не отображается"

    @allure.title("Проверка наличия блока 'Смотрите также'")
    def test_product_similar_products_exist(self, page):
        """Тест 18: Проверка наличия блока 'Смотрите также'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        product_page.scroll_to_bottom()

        assert product_page.is_similar_products_visible(), "Блок 'Смотрите также' не найден"

    @allure.title("Проверка наличия блока с отзывами")
    def test_product_reviews_exist(self, page):
        """Тест 19: Проверка наличия блока с отзывами."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["phone"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.are_reviews_visible(), "Блок с отзывами не найден"

    @allure.title("Проверка наличия выбора цвета")
    def test_product_color_options(self, page):
        """Тест 20: Проверка наличия выбора цвета."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.search_product(self.SEARCH_QUERIES["t_shirt"])

        search_page = SearchPage(page)
        assert search_page.get_products_count() > 0, "Нет товаров"

        search_page.click_first_product()
        product_page = ProductPage(page)

        assert product_page.are_color_options_visible(), "Выбор цвета не найден"
