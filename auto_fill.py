'''
########################################################################################

                            Test File of Auto Extract

    Version:            N/A  
    Author:             Mingrui Yang
    Functionality:      This file is a demo of how auto_extract.py, given an html page,
                        can return a list of field id's that can be used in the 
                        selenium commands.

########################################################################################
'''
from auto_extract import AutoExtract
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Application(object):
  def __init__(self, url, usr_info):
    '''
    url:        application url <string> 
    usr_info:   user_information <collections.orderedDict>
    '''
    self.url = url 
    self.usr_info = usr_info               
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.commandObject = AutoExtract() 
    self.commandCores = self.commandObject.extract() 
  
  def apply(self):
    '''
    Selenium commands comes here.
    '''
    self.driver.get(self.url) 
    for cmd in self.commandCores: 
        #time.sleep(1) 
        input_val = self.usr_info[cmd] 
        tag_id = self.commandCores[cmd]  # The actual html id value 
        self.driver.find_element(By.ID, tag_id).send_keys(input_val)
    time.sleep(1)
    self.driver.quit()




