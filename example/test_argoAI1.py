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

class TestArgoAI():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_argoAI(self):
    self.driver.get("https://www.argo.ai/join-us/#j1857622")
    self.driver.set_window_size(1280, 680)
    '''self.driver.switch_to.frame(0)
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "span").click()
    assert self.driver.switch_to.alert.text == "Confirm you’d like to apply for this job with LinkedIn. Linkedin.com will send your information to https://boards.greenhouse.io"
    self.driver.switch_to.alert.accept()
    self.driver.switch_to.default_content()'''
    time.sleep(2)
    self.driver.find_element(By.ID, "phone").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "phone").send_keys("7375296126")
    self.driver.find_element(By.ID, "application").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(10)").click()
    self.driver.find_element(By.ID, "job_application_location").click()
    self.driver.find_element(By.ID, "ui-id-32").click()
    self.driver.find_element(By.ID, "job_application_location").send_keys("Pittsburgh, Pennsylvania, United States")
    self.driver.find_element(By.CSS_SELECTOR, ".education:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_education_school_name_0 .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_education_degree_0 .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_education_degree_0 .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".select2-default > .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".select2-default > .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.NAME, "job_application[educations][][start_date][month]").click()
    self.driver.find_element(By.NAME, "job_application[educations][][start_date][month]").send_keys("05")
    self.driver.find_element(By.NAME, "job_application[educations][][start_date][year]").send_keys("2022")
    self.driver.find_element(By.NAME, "job_application[educations][][end_date][month]").click()
    self.driver.find_element(By.NAME, "job_application[educations][][start_date][year]").click()
    self.driver.find_element(By.NAME, "job_application[educations][][start_date][year]").send_keys("2018")
    self.driver.find_element(By.NAME, "job_application[educations][][end_date][month]").click()
    self.driver.find_element(By.NAME, "job_application[educations][][end_date][month]").send_keys("08")
    self.driver.find_element(By.NAME, "job_application[educations][][end_date][year]").send_keys("2022")
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_job_application_answers_attributes_0_answer_selected_options_attributes_0_question_option_id .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_job_application_answers_attributes_0_answer_selected_options_attributes_0_question_option_id .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.CSS_SELECTOR, "#custom_fields > .field:nth-child(2)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_job_application_answers_attributes_1_answer_selected_options_attributes_1_question_option_id .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_job_application_answers_attributes_1_answer_selected_options_attributes_1_question_option_id .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.ID, "s2id_autogen9").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_job_application_answers_attributes_3_boolean_value .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_job_application_answers_attributes_3_boolean_value .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "select2-drop-mask")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#s2id_job_application_answers_attributes_4_boolean_value .select2-chosen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.ID, "application_form").click()
    self.driver.find_element(By.ID, "job_application_answers_attributes_5_text_value").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(5) > label:nth-child(5) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, "#demographic_questions > .field:nth-child(6)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(6) > label:nth-child(5) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(17) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(8) > label:nth-child(11) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(9) > label:nth-child(7) > input").click()
    self.driver.find_element(By.ID, "application").click()
    self.driver.find_element(By.ID, "application").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(6) > label:nth-child(7) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(6) > label:nth-child(5) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(5) > label:nth-child(9) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(5) > label:nth-child(5) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".field:nth-child(12) a:nth-child(1)").click()

