from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class SsnPage:
    _options = Options()
    _url = "https://oam.wellsfargo.com/oamo/identity/help/passwordhelp#/"

    def __init__(self):
        self._options.page_load_strategy = 'eager'

    # Xpth = xpath
    _ssnInpXpth = '//*[@id="ssn"]'
    _ssnInpId = 'ssn'
    _birthInpXpth = '//*[@id="dob"]'
    _btnSendSsnXpth = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/button[1]'
    _btnSendXpth = '//*[@id="SNPCICUH"]'
    _btnSendBirthXpth = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/form/div[2]/button[1]'
    # msj success
    #
    _msjPin = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[2]'
    _msjMobileNumber = '/html/body/div[2]/div[5]/div/div/div/div/div/div/div/div[2]'
    _msjSuccess = [[_msjPin, "Pin"], [_msjMobileNumber, "Numero de telefono"]]
    # msj error
    _msjNotEnrolled = '/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[1]/header/div/div[1]/h2/span'
    _msjAccount = '//*[@id="accountNumber"]'
    _msjErrors = [_msjNotEnrolled, _msjAccount]

    def sendRequest(self, data):
        edgeDriver = webdriver.Edge(options=self._options)
        edgeDriver.get(self._url)
        sleep(8)
        # enviando Ssn al input
        self.sendTxtByXpath(edgeDriver, self._ssnInpXpth, data[0])
        sleep(3)
        self.clickBtnByXpath(edgeDriver, self._btnSendSsnXpth)
        # enviando el birth
        sleep(4)
        self.sendTxtByXpath(edgeDriver, self._birthInpXpth, data[1])
        self.clickBtnByXpath(edgeDriver, self._btnSendBirthXpth)
        sleep(12)
        element = self.detectErrorsByXpath(edgeDriver)

        if element == False:
            # en caso de que detecte que encontro algo almacenarlo
            success = self.detectSuccessByXpath(edgeDriver)
            if success[1]:
                element = [f"SSN:{data[0]} Birth:{data[1]} Tipo: {success[0]}",success[1],
                           ]
            else:
                element = success
        edgeDriver.quit()
        return element

    # en otro mantenimiento encapsular ambas funciones para detectar errores y mensajes de success
    def detectErrorsByXpath(self, driver):
        for err in self._msjErrors:
            if self.detectElementByXpath(driver, err) ==  True:
                driver.quit()
                return ["Not rated", True]
        return False

    def detectSuccessByXpath(self, driver):
        for succ in self._msjSuccess:
            if self.detectElementByXpath(driver, succ[0]) == True:
                return [succ[1], True]
        return ["Not rated", False]

    def detectElementByXpath(self, driver, path):
        try:
            driver.find_element(By.XPATH, path)
            return True
        except NoSuchElementException:
            return False

    def sendTxtByXpath(self, driver, path, data):
        element = driver.find_element(By.XPATH, path)
        element.send_keys(data)

    def clickBtnByXpath(self, driver, path):
        element = driver.find_element(By.XPATH, path)
        element.click()
