from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ścieżka do sterownika przeglądarki, np. dla Chrome
driver_path = '/ścieżka/do/sterownika/chromedriver'

# Inicjalizacja przeglądarki
driver = webdriver.Chrome(executable_path=driver_path)

# Adres URL strony, na której chcesz przeprowadzić test
url = 'https://www.przykladowastrona.com'
driver.get(url)

try:
    # Znalezienie pola do wpisywania tekstu (przykładowo za pomocą XPath)
    input_field = driver.find_element_by_xpath('//input[@name="nazwa_pola"]')

    # Wpisanie tekstu do pola
    input_field.send_keys('Przykładowe dane do wpisania')

    # Poczekanie chwilę (opcjonalnie)
    driver.implicitly_wait(5)

    # Zatwierdzenie wprowadzonego tekstu (przykładowo za pomocą klawisza Enter)
    input_field.send_keys(Keys.RETURN)

finally:
    # Zamknięcie przeglądarki po zakończeniu testu
    driver.quit()
