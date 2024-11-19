from firefox_driver_utils import setup_driver, navigate_to_page, print_page_title, close_driver

# Uso das funções
if __name__ == "__main__":
    # Configura o WebDriver
    driver = setup_driver(executable_path='geckodriver', headless=True)

    try:
        # Navega para a página e exibe o título
        navigate_to_page(driver, "http://localhost:8000/page.php")
        print_page_title(driver)

    finally:
        # Fecha o WebDriver
        close_driver(driver)