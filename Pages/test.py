import asyncio
from pyppeteer import launch


async def completar_formulario():
    # Inicia una instancia de Chromium (puede ser headless o no)
    # Si deseas modo headless, cambia a headless=True
    ssnInpXpth = '//*[@id="ssn"]'
    _ssnInpId = 'ssn'
    _birthInpXpth = '//*[@id="dob"]'
    _btnSendSsnXpth = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/button[1]'
    _btnSendXpth = '//*[@id="SNPCICUH"]'
    _btnSendBirthXpth = '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/form/div[2]/button[1]'
    # msj success
    #
    _msjPin = '.ResponsiveModalHeader__modalHeader___L8ckB > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > span:nth-child(1)'
    _msjMobileNumber = '/html/body/div[2]/div[5]/div/div/div/div/div/div/div/div[2]'
    _msjSuccess = [[_msjPin, "Pin"], [_msjMobileNumber, "Numero de telefono"]]
    # msj error
    _msjNotEnrolled = '/html/body/div[2]/div[4]/div/div/div/div/div/div/div/div[1]/header/div/div[1]/h2/span'
    _msjAccount = '//*[@id="accountNumber"]'
    _msjErrors = [_msjNotEnrolled, _msjAccount]
    browser = await launch(headless=False)
    bueno = False

    # Crea una nueva página
    page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36')
    # Navega a la página web con el formulario
    await page.goto('https://oam.wellsfargo.com/oamo/identity/help/passwordhelp')
    await asyncio.sleep(4)
    # Rellena el formulario (ajusta los selectores y valores según tu formulario)
    await page.type('#ssn', '556837212')
    await asyncio.sleep(2)
    await page.click("button.Button__modern___cqCp7:nth-child(1)")
    await asyncio.sleep(10)
    await page.type("#dob", "11/16/1983")
    await asyncio.sleep(2)
    await page.click("#identify-dob > div.Identification__buttonContainer___b20TE > button.Button__button___Jo8E3.Button__modern___cqCp7.Button__responsive___Xx9EJ.Button__primary___tsDHA")
    await asyncio.sleep(12)
    try:

        await page.waitForSelector(".ResponsiveModalHeader__modalHeader___L8ckB > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > span:nth-child(1)")
        bueno = True
        print("bueno")
    except:
        print("malo")
    # Espera un momento para que el formulario se envíe o realice otras acciones si es necesario
    await asyncio.sleep(5)  # Espera 5 segundos (ajusta según tus necesidades)

    # Cierra el navegador
    await browser.close()
    if bueno == True:
        return [_msjSuccess[0][0], True]

# Ejecuta la función asincrónica
asyncio.get_event_loop().run_until_complete(completar_formulario())
