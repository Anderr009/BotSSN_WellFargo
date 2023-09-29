from selenium import webdriver
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.common.by import By
from time import sleep

class SsnPage:
    _options = Options()
    _url = "https://oam.wellsfargo.com/oamo/identity/help/passwordhelp#/"
    def __init__(self):
        self._options.page_load_strategy = 'eager'

    #Xpth = xpath  
    _ssnInpXpth = '//*[@id="ssn"]'  
    _ssnInpId = 'ssn'
    _birthInpXpth = '//*[@id="dob"]' 
    _btnSendSsnXpth = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/button[1]'
    _btnSendXpth = '//*[@id="SNPCICUH"]'
    _btnSendBirthXpth = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/form/div[2]/button[1]'
    #msj success
    _msjPin = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div'
    _msjMobileNumber = '//*[@id="TIPOFEPP"] '
    #msj error
    _msjNotEnrolled = '/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[1]/header/div/div[1]/h2/span'
    _msjAccount = '//*[@id="accountNumber"]'

    def sendRequest(self,data):
        edgeDriver = webdriver.Edge(options=self._options)
        edgeDriver.get(self._url)
        sleep(3)
        #enviando Ssn al input
        self.sendTxtByXpath(edgeDriver,self._ssnInpXpth,data[0])
        sleep(1.2)
        self.clickBtnByXpath(edgeDriver,self._btnSendSsnXpth)
        #enviando el birth
        sleep(2)
        self.sendTxtByXpath(edgeDriver,self._birthInpXpth,data[1])
        self.clickBtnByXpath(edgeDriver,self._btnSendBirthXpth)
        sleep(6)
        edgeDriver.quit()


    def detectErrors(driver):
        pass

    def detectSuccess(driver):
        pass

    def sendTxtByXpath(self,driver,path,data):
        element = driver.find_element(By.XPATH,path)
        element.send_keys(data)

    def clickBtnByXpath(self,driver,path):
        element = driver.find_element(By.XPATH,path)
        element.click()
