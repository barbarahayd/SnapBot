from utils import setup_driver, navigate_to_page, close_driver, print_button_text, take_page_screenshot, \
    print_page_title

# Uso das funções
if __name__ == "__main__":
    # configura o WebDriver
    driver = setup_driver(executable_path='geckodriver', headless=False)

    try:
        # navega para a página, exibe o título e captura um screenshot
        navigate_to_page(driver, "http://localhost:8000/page.php")
    #TODO: add logging for exceptions
        print_page_title(driver)
        take_page_screenshot(driver, "screenshot.png")

    finally:
        # fecha WebDriver
        close_driver(driver)