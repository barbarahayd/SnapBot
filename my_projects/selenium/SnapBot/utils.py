import time
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


def print_button_text(driver: webdriver.Firefox) -> None:
    """
    Imprime o texto do botao.

    Args:
        driver (webdriver.Firefox): Instância do WebDriver.
    """
    button = driver.find_element("id", "testButton")

    if button:
        print(button.text)
    else:
        print("Botão não encontrado.")

def print_page_title(driver: webdriver.Firefox) -> None:
    """
    Imprime o título da página.

    Args:
        driver (webdriver.Firefox): Instância do WebDriver.
    """
    print(driver.title)

def take_page_screenshot(driver: webdriver.Firefox, filename: str) -> None:
    """
    Tira um screenshot da página e salva em um arquivo.

    Args:
        driver (webdriver.Firefox): Instância do WebDriver.
        filename (str): Nome do arquivo de saída.
    """
    driver.save_screenshot(filename)

def close_driver(driver: webdriver.Firefox) -> None:
    """
    Fecha o WebDriver e encerra o navegador.

    Args:
        driver (webdriver.Firefox): Instância do WebDriver.
    """
    driver.quit()
