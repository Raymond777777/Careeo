# Generated by Selenium IDE
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

class TestCloudengineer():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cloudengineer(self):
    self.driver.get("https://www.appian.com/careers/search/job/?gh_jid=1937729&job_name=cloud-software-engineer&location=mclean-virginia")
    self.driver.set_window_size(648, 570)
    element = self.driver.find_element(By.CSS_SELECTOR, ".logo > a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.switch_to.frame(4)
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("er")
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(9)").click()
    self.driver.find_element(By.ID, "phone").click()
    self.driver.find_element(By.ID, "phone").send_keys("ere")
    self.driver.find_element(By.LINK_TEXT, "Attach").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(5)
    assert self.driver.switch_to.alert.text == "Invalid file format selected. Allowed formats are: pdf, doc, docx, txt, rtf"
  
