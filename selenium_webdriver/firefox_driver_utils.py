from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def setup_driver(executable_path: str, headless: bool = False) -> webdriver.Firefox:
    """
    Configura e inicializa o WebDriver para Firefox.

    Args:
        executable_path (str): Caminho para o GeckoDriver.
        headless (bool): Se True, o navegador será executado no modo headless.

    Returns:
        webdriver.Firefox: Instância configurada do Firefox WebDriver.
    """

    options = Options()
    if headless:
        options.add_argument("--headless")

    service = Service(executable_path=executable_path)
    driver = webdriver.Firefox(service=service, options=options)
    return driver


def navigate_to_page(driver: webdriver.Firefox, url: str) -> None:
    """
    Navega para a página especificada.

    Args:
        driver (webdriver.Firefox): Instância do WebDriver.
        url (str): URL da página para navegar.
    """
    driver.get(url)


def print_page_title(driver: webdriver.Firefox) -> None:
    """
    Imprime o título da página atual.

    Args:
        driver (webdriver.Firefox): Instância do WebDriver.
    """
    print(driver.title)


def close_driver(driver: webdriver.Firefox) -> None:
    """
    Fecha o WebDriver e encerra o navegador.

    Args:
        driver (webdriver.Firefox): Instância do WebDriver.
    """
    driver.quit()
