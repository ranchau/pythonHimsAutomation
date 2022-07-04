import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from numpy import random
import Base as newIntakeWebDriver

def edNewIntakeMain():
    print("i am here in intake method")
    driver = newIntakeWebDriver.driver
    print(driver)
    
    # //(Visit questionnaire 1/19)
    # //Do you ever have a problem getting or maintaining an erection that is rigid enough for sex?
    # //Selecting I never have a problem getting or maintaining an erection for as long as I want
    driver.find_element_by_xpath("//*[@for='Question-16201-06843032-2b05-4eca-b551-17df0483f5f6']").click()  

# 2 of 18
# Pick the scenario that best describes your ED. 
    driver.find_element_by_xpath("//*[@for='Question-20132-03165655-a5e4-4cb4-a4e9-ec82936899a1']").click()

# 3 of 18
# How did your ED start? 
    driver.find_element_by_xpath("//*[@for='Question-20133-f95a2043-56bc-43e9-a6ac-7abe12e2a9b0']").click()

# 4 of 18
# Rate the typical hardness of your erection during masturbation. 
    driver.find_element_by_xpath("//*[@for='Question-20260-37594d32-4ba3-4075-8cb6-6bdc5ec48a8d']").click()

# 5 of 18 
# Rate the typical hardness of your spontaneous erections in the middle of the night or the morning.
    driver.find_element_by_xpath("//*[@for='Question-20261-fcc55ab2-1a79-4e1e-9403-f02e2360090a']").click()

# 6 of 18 
# Rate the typical hardness of your erection with a sexual partner.
    driver.find_element_by_xpath("//*[@for='Question-20262-1a0a5a40-7b87-48d4-86d9-27641e4324fe']").click()

# 7 of 18 
# Do you have low sex drive?
    driver.find_element_by_xpath("//*[@for='Question-16233-bef9e377-1ff9-46e3-816b-dd998b2ddbdc']").click()

# 8 of 21
# Do you have a lack of energy?
    driver.find_element_by_xpath("//*[@for='Question-20135-06413916-e994-4227-9e49-b74b3c9fb17e']").click()

# 9 of 21
# Do you have a decrease in strength and/or endurance?
    driver.find_element_by_xpath("//*[@for='Question-20136-22982a4a-6904-4327-b6d9-17e08b49e798']").click()

# 10 of 21
# Are you sad and/or grumpy?
    driver.find_element_by_xpath("//*[@for='Question-20137-83f80b7d-59ab-43c0-b71a-1c9da069712e']").click()

# 11 of 21
# Have you ever been treated with medication for ED?
    driver.find_element_by_xpath("//*[@for='Question-16198-33e79356-9a00-453c-8827-9b5046249594']").click()

# new 12 of 22
# What is your gender?  We ask this question of all of our patients to ensure that we provide you with safe and effective care. We are inclusive of all people.
    driver.find_element_by_xpath("//*[@for='Question-20529-378a5ba5-98eb-4755-b5d1-3236d96d8dec']").click()

# new 13 of 22
# What was your sex assigned at birth? For example, on your original birth certificate.
    driver.find_element_by_xpath("//*[@for='Question-20530-4eec790a-ce95-437d-9c50-b16a008290d7']").click()

# 12 of 21
# When was your most recent in-person checkup with a healthcare provider?
    # driver.find_element_by_xpath("//*[@for='Question-16597-123b013c-a2db-4e6a-bb75-45095bfeaa49']").click()

# 13 of 21
# What was your last blood pressure reading?
# What was your top number?
    # driver.find_element_by_xpath("//*[@for='systolic_90-139']").click()
# What was your bottom number?
    # driver.find_element_by_xpath("//*[@for='diastolic_50-80']").click()

    # intakeBPButton = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-BP-V3-Continue']")
    # driver.execute_script("arguments[0].click()", intakeBPButton)

# 15 of 20
# Do you have any allergies?
# Include any allergies to food, dyes, prescriptions, or over-the-counter medicines (e.g. antibiotics, allergy medications), herbs, vitamins, supplements, or anything else.
    # //Selecting No
    driver.find_element_by_xpath("//*[@for='Question-16271-a581d6be-b65b-467c-ae8c-83bea090b294']").click()

# Have you had any surgeries or hospitalizations?
    intake13 = driver.find_element_by_xpath("//*[@for='Question-20157-dd15206a-9e22-42bd-82c2-29eea108e710']")
    driver.execute_script("arguments[0].click()", intake13)
    # intake13Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake13Button)

    # 20 of 20
# Do you currently or have you within the past 6 months, smoked or used any of the following recreational drugs?

# Do you experience any of the following cardiovascular symptoms?
    intake19 = driver.find_element_by_xpath("//*[@for='Question-16278-b129f833-dd3d-4ec7-8d07-4fa83e01b6dd']")
    driver.execute_script("arguments[0].click()", intake19)
    intake19Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake19Button)

    # Do you have or have you previously been diagnosed with any of the following? Check all that apply.
    intake20 = driver.find_element_by_xpath("//*[@for='Question-20213-a6f901fe-536e-41af-873c-f9969353151f']")
    driver.execute_script("arguments[0].click()", intake20)
    
    intake20Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake20Button)

    # //Do you take any medications, vitamins, or supplements regularly?
    # //Selecting No
    driver.find_element_by_xpath("//*[@for='Question-16269-72551763-a820-439e-8692-037e19d1be90']").click()

#     19 of 20
# In the last 3 months have you experienced any of the following? 
# Fainting, almost fainting, severe headaches, blurry or double vision, recurrent nosebleeds.
    driver.find_element_by_xpath("//*[@for='Question-20965-b45b7623-44b3-4de9-9b90-afa112f65a8b']").click()


# Do you currently or have you within the past 6 months, smoked or used any of the following recreational drugs?
    intake21 = driver.find_element_by_xpath("//*[@for='Question-16273-c8d92f3a-cdf2-47bb-817c-6dfb539e7466']")
    driver.execute_script("arguments[0].click()", intake21)

    intake21Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake21Button)

    # https://www.forhims.com/consultation/ed/prompt-patient-conversation-step

# Is there anything else your healthcare provider should know?
    # intakeTwoWayMessage1 = driver.find_element_by_xpath("//*[@for='Question-provider_question-yes']")
    # driver.execute_script("arguments[0].click()", intakeTwoWayMessage1)

    # intakeTwoWayMessage1Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Radio-Continue']")
    # driver.execute_script("arguments[0].click()", intakeTwoWayMessage1Button)

    
