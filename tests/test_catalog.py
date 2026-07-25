"""Тесты для каталога."""

import allure
import pytest

from pages.main_page import MainPage


@allure.epic("UI тестирование")
@allure.feature("Каталог")
class TestCatalog:
    """Тесты для каталога Wildberries."""

    CATEGORIES_WITH_SUB = (
        "Женщинам",
        "Мужчинам",
        "Электроника",
        "Дом",
        "Спорт",
        "Акции"
    )

    EXPECTED_CATEGORIES = (
        "Женщинам",
        "Мужчинам",
        "Детям",
        "Дом",
        "Красота",
        "Электроника"
    )

    @allure.title("Проверка наличия кнопки каталога")
    def test_catalog_button_exists(self, page):
        """Тест 1: Проверка наличия кнопки каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        assert main_page.is_element_visible(
            main_page.LOCATORS["catalog_button"]
        ), "Кнопка каталога не найдена"

    @allure.title("Проверка, что кнопка каталога видна после перехода на другую страницу")
    def test_catalog_button_visible_after_navigation(self, page):
        """Тест 2: Проверка, что кнопка каталога не исчезает после перехода."""
        main_page = MainPage(page)
        main_page.open_main_page()
    
        main_page.search_product("телефон")
    
        assert main_page.is_element_visible(
            main_page.LOCATORS["catalog_button"]
        ), "Кнопка каталога исчезла после перехода"

    @allure.title("Проверка открытия панели каталога")
    def test_catalog_panel_opens(self, page):
        """Тест 3: Проверка открытия панели каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        result = main_page.open_catalog()
        assert result, "Не удалось открыть панель каталога"
        assert main_page.is_catalog_panel_open(), "Панель каталога не открылась"

    @allure.title("Проверка наличия основных категорий в панели")
    def test_catalog_panel_has_categories(self, page):
        """Тест 4: Проверка наличия основных категорий в панели каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        found_categories = []
        for category in self.EXPECTED_CATEGORIES:
            if main_page.is_category_exists(category):
                found_categories.append(category)

        assert len(found_categories) >= 4, \
            f"Найдено только {len(found_categories)} из {len(self.EXPECTED_CATEGORIES)} категорий: {found_categories}"

    @allure.title("Проверка появления подкатегорий при клике на категорию")
    def test_catalog_panel_has_subcategories(self, page):
        """Тест 5: Проверка появления подкатегорий при клике на категорию."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        found_subcategories = False
        for category in self.CATEGORIES_WITH_SUB:
            if main_page.is_category_exists(category):
                if main_page.click_category(category):
                    if len(main_page.get_subcategory_texts()) > 0:
                        found_subcategories = True
                        break

        assert found_subcategories, "Не удалось найти подкатегории ни для одной категории"

    @allure.title("Проверка закрытия панели каталога")
    def test_catalog_panel_close(self, page):
        """Тест 6: Проверка закрытия панели каталога."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        assert main_page.is_catalog_panel_open(), "Панель не открылась"
        main_page.close_catalog()
        assert main_page.is_catalog_panel_closed(), "Панель не закрылась"

    @allure.title("Проверка наличия категории {category}")
    @pytest.mark.parametrize("category", [
        "Электроника",
        "Дом",
        "Красота",
        "Спорт",
        "Бренды"
    ])
    def test_catalog_panel_has_category(self, page, category):
        """Тесты 7-11: Проверка наличия конкретных категорий."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()
        assert main_page.is_category_exists(category), f"Категория '{category}' не найдена"

    @allure.title("Проверка наличия категорий для женщин и мужчин")
    def test_catalog_panel_has_clothing(self, page):
        """Тест 12: Проверка наличия категорий 'Женщинам' и 'Мужчинам'."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        assert main_page.is_category_exists("Женщинам"), "Категория 'Женщинам' не найдена"
        assert main_page.is_category_exists("Мужчинам"), "Категория 'Мужчинам' не найдена"

    @allure.title("Проверка наличия категорий для детей")
    def test_catalog_panel_has_children(self, page):
        """Тест 13: Проверка наличия категорий для детей."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        has_children = (
            main_page.is_category_exists("Детям") or
            main_page.is_category_exists("Игрушки")
        )
        assert has_children, "Категория 'Детям' не найдена"

    @allure.title("Проверка наличия раздела со скидками")
    def test_catalog_panel_has_sale(self, page):
        """Тест 14: Проверка наличия раздела со скидками."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        has_sale = (
            main_page.is_category_exists("Акции") or
            main_page.is_category_exists("Скидки WB Клуба")
        )
        assert has_sale, "Раздел со скидками не найден"

    @allure.title("Клик по категории 'Акции' и проверка страницы акций")
    def test_catalog_panel_click_promotions(self, page):
        """Тест 15: Клик по категории 'Акции' и проверка страницы акций."""
        main_page = MainPage(page)
        main_page.open_main_page()
        main_page.open_catalog()

        assert main_page.is_category_exists("Акции"), "Категория 'Акции' не найдена"

        result = main_page.click_promotions_category()
        assert result, "Не удалось кликнуть на категорию 'Акции'"

        assert main_page.is_promotions_banner_visible(), "Баннер 'Сделано в Беларуси' не найден"
        assert main_page.get_banner_size() == (660, 210), "Неверный размер баннера"
