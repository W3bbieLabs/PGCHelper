from selenium import webdriver
from selenium.webdriver.common.by import By
class BrowserSession:
    def __init__(self, targetSite:dict):
        self.targetBrowser  = targetSite["browser"]
        self.targetSite     = targetSite["url"]
        self.targetElement  = targetSite["element"]
        self.sessionDriver  = self.EstablishSessionDriver(self.targetBrowser)
    def GetTargetSite(self):    return self.targetSite
    def GetTargetBrowser(self): return self.targetBrowser
    def GetTargetElement(self): return self.targetElement
    def SetTargetSite(self, targetSite:str): 
        self.targetSite = targetSite
    def SetTargetBrowser(self, browserName):
        self.currentBrowser = browserName
    def SetTargetElement(self, elemenClassName:str):
        self.targetElement = elemenClassName
    def CloseSession(self):
        self.sessionDriver.close()
    def HeadToTargetSite(self):
        self.sessionDriver.get(self.GetTargetSite())
    def EstablishSessionDriver(self, browserArg="firefox"):
        try:
            if (browserArg.lower()=="chrome"):
                self.sessionDriver = webdriver.Chrome()
            elif (browserArg.lower()=="firefox"):
                self.sessionDriver = webdriver.Firefox()
            elif (browserArg.lower()=="safari"):
                self.sessionDriver = webdriver.Safari()
            elif (browserArg.lower()=="edge"):
                self.sessionDriver = webdriver.Edge()
        except Exception as error:
            print("Type of browser not supported.")
            self.sessionDriver = None
    def PrintTitle(self):
        print(f"{self.sessionDriver.name} session @: {self.sessionDriver.title} | {self.sessionDriver.current_url}")
    def FindElementByClass(self, targetElement:str="randomize-button"):
        element = self.sessionDriver.find_element(By.CLASS_NAME, targetElement)
        return element
    def TriggerElementClick(self, element):
        self.sessionDriver.implicitly_wait(0.5)
        element.click()
    def StartSession(self):
        self.EstablishSessionDriver()
        self.HeadToTargetSite()
        self.sessionDriver.implicitly_wait(0.5)
        self.PrintTitle()
    def BeginClicking(self, targetElement:str="randomize-button"):
        sessionElement = self.FindElementByClass(targetElement)
        self.TriggerElementClick(sessionElement)