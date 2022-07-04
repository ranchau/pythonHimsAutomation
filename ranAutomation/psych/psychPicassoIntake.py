import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from numpy import random
import psychBase as psychPicassoIntakMainDriver

driver = psychPicassoIntakMainDriver.driver
username = ("ranjit+cronofy+psychpicasso+0302") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
FirstName = "Testhims"
LastName = "Testhers"
ZipCode = "83209"
# "90064"


def psychPicassoMain():
    # def psychPicassoCreateAccount():
        #  consultation/psychiatry/create-account
    driver.find_element_by_id("email").send_keys(username) 
    driver.find_element_by_id("password").send_keys("asdf96@@PB") 
    driver.find_element_by_id("confirmPassword").send_keys("asdf96@@PB") 
    driver.find_element_by_xpath("//span[@data-testid='ConsultationConsent']").click()
    driver.find_element_by_xpath("//button[contains (text(), 'Get started')]").click()

    # def psychPicassoSelectState():
        #  consultation/psychiatry/select-state-step
    driver.find_element_by_id("firstName").send_keys(FirstName) 
    driver.find_element_by_id("lastName").send_keys(LastName) 
    driver.find_element_by_id("zipCode").send_keys(ZipCode) 
    driver.find_element_by_id("dob").send_keys("10311990") 



    # driver = webdriver.Chrome("/Users/rchaudhary/eclipse-workspace/chromedriver")

    print("i am here in intake method")
    print(driver)

# What can we help you with today?
    driver.find_element_by_xpath("//button[contains (text(), 'Anxiety')]").click()

    time.sleep(2)
    # /consultation/psychiatry/preliminary-screening-landing
    driver.find_element_by_xpath("//button[contains (text(), 'Next')]").click()
    time.sleep(1.5)
    driver.find_element_by_xpath("//button[contains (text(), 'Next')]").click()
    time.sleep(1.5)
    driver.find_element_by_xpath("//button[contains (text(), 'Next')]").click()


    #1 / 17
    #Over the last 2 weeks, how often have you been bothered by little interest or pleasure in doing things?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #        2 / 17
    #Over the last 2 weeks, how often have you been bothered by feeling down, depressed, or hopeless?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #3 / 17
    #Over the last 2 weeks, how often have you been bothered by trouble falling or staying asleep, or sleeping too much? 
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #4 / 17
    #Over the last 2 weeks, how often have you been bothered by feeling tired or having little energy?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #5 / 17
    #Over the last 2 weeks, how often have you been bothered by poor appetite or eating? 
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #6 / 17
    #Over the last 2 weeks, how often have you been bothered by feeling bad about yourself, that you are a failure, or have let yourself or your family down?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #7 / 17
    #Over the last 2 weeks, how often have you been bothered by trouble concentrating on things such as reading the newspaper or watching tv?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #8 / 17
    #Over the last 2 weeks, how often have you been bothered by moving or speaking so slowly that other people have noticed, OR being so fidgety or restless that you have been moving around a lot more than usual?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #9 / 17
    #If you checked any problems, how difficult have they made it for you to do your work, take care of things at home, or get along with other people?
    driver.find_element_by_xpath("//button[contains (text(), 'Somewhat difficult')]").click()

    #10 / 17
    #Over the last 2 weeks, how often have you been bothered by feeling nervous, anxious, or on edge?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #11 / 17
    #Over the last 2 weeks, how often have you been bothered by not being able to control worrying?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #12 / 17
    #Over the last 2 weeks, how often have you been bothered by worrying too much about different things?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #13 / 17
    #Over the last 2 weeks, how often have you been bothered by trouble relaxing?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #14 / 17
    #Over the last 2 weeks, how often have you been bothered by being so restless that it is hard to sit still?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #15 / 17
    #Over the last 2 weeks, how often have you been bothered by becoming easily annoyed or irritable?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #16 / 17
    #Over the last 2 weeks, how often have you been bothered by feeling afraid as if something awful might happen?
    driver.find_element_by_xpath("//button[contains (text(), 'Several days')]").click()

    #17 / 17
    #If you checked any problems, how difficult have they made it for you to do your work, take care of things at home, or get along with other people?
    driver.find_element_by_xpath("//button[contains (text(), 'Somewhat difficult')]").click()


# /consultation/psychiatry/preliminary-screening
    driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

#  consultation/psychiatry/plan-selection




    #18 / 42
    #Which mental health condition(s) are you seeking services for?
    #driver.find_element_by_xpath("//button[contains (text(), 'Performance anxiety (eg. stage fright)')]").click()
    time.sleep(1.5)
    #driver.find_element_by_xpath("//button[contains (text(), 'Next')]").click()
    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake18 = driver.find_element_by_xpath("//button[contains (text(), 'Performance anxiety (eg. stage fright)')]")
    #  general anxiety
    intake18 = driver.find_element_by_xpath("//button[contains (text(), 'Generalized anxiety (eg. persistent, general worry),')]")
    driver.execute_script("arguments[0].click()", intake18)

    intake18Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake18Button)


    #19 / 43
    #If you'd like to be evaluated for performance anxiety, please navigate to our offering on the [hims](https://www.forhims.com/well-being/propranolol) or [hers](https://www.forhers.com/well-being/propranolol) website. If you'd like to continue with your mental health visit, please continue.
    # driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

    #20 / 43
    #Are any of these triggers for your mental health condition?
    #driver.find_element_by_xpath("//button[contains (text(), 'Recent relationship issues')]").click()
    #driver.find_element_by_xpath("//button[contains (text(), 'Social situations')]").click()

    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake20A = driver.find_element_by_xpath("//button[contains (text(), 'Recent relationship issues')]")
    driver.execute_script("arguments[0].click()", intake20A)

    intake20B = driver.find_element_by_xpath("//button[contains (text(), 'Social situations')]")
    driver.execute_script("arguments[0].click()", intake20B)

    intake20Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake20Button)

    #21 / 43
    #Is there any new or recent life event that may be impacting how you are feeling?
    #driver.find_element_by_xpath("//button[contains (text(), 'Family or relationship problems')]").click()
    #driver.find_element_by_xpath("//button[contains (text(), 'Life event or transition')]").click()

    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake21A = driver.find_element_by_xpath("//button[contains (text(), 'Family or relationship problems')]")
    driver.execute_script("arguments[0].click()", intake21A)

    intake21B = driver.find_element_by_xpath("//button[contains (text(), 'Life event or transition')]")
    driver.execute_script("arguments[0].click()", intake21B)

    intake21Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake21Button)

    #22 / 43
    #Do you have a history of any of the following mental health conditions?
    #driver.find_element_by_xpath("//button[contains (text(), 'Anxiety')]").click()
    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake22 = driver.find_element_by_xpath("//button[contains (text(), 'Anxiety')]")
    driver.execute_script("arguments[0].click()", intake22)

    intake22Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake22Button)

    #23 / 46
    #Who diagnosed you for anxiety?
    driver.find_element_by_xpath("//button[contains (text(), 'Healthcare provider')]").click()

    #24 of 46
    #When were you diagnosed for anxiety?
    driver.find_element_by_id("19170_TA_ID").send_keys("TEST ORDER Thx DOC!")
    driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()

    #25 of 46
    #Did you treat your anxiety with medications or therapy?
    #If medication, please include name and dosage.
    driver.find_element_by_id("19171_TA_ID").send_keys("TEST ORDER Thx DOC medicine!")
    driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()

    #26 / 46
    #Do you have a family history of any of the following?
    #driver.find_element_by_xpath("//button[contains (text(), 'Anxiety')]").click()

    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake26 = driver.find_element_by_xpath("//button[contains (text(), 'Anxiety')]")
    driver.execute_script("arguments[0].click()", intake26)

    intake26Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake26Button)

    #27 / 46
    #Are you currently using any of the following mental health medications?
    #driver.find_element_by_xpath("//button[contains (text(), 'None apply')]").click()

    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake27 = driver.find_element_by_xpath("//button[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intake27)

    intake27Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake27Button)

    #28 / 46
    #Are you currently taking any of the following other medications?
    #driver.find_element_by_xpath("//button[contains (text(), 'None apply')]").click()

    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake28 = driver.find_element_by_xpath("//button[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intake28)

    intake28Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake28Button)

    #29 / 46
    #Have you ever used any of the following mental health medications in the past?
    #driver.find_element_by_xpath("//button[contains (text(), 'None apply')]").click()

    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake29 = driver.find_element_by_xpath("//button[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intake29)

    intake29Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake29Button)

    #30 / 46
    #Have you ever participated in talk therapy or therapy sessions?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #31 / 46
    #To which gender identity do you most identify with?
    driver.find_element_by_xpath("//button[contains (text(), 'Male')]").click()

    #32 / 46
    #What was your sex assigned at birth?
    driver.find_element_by_xpath("//button[contains (text(), 'Male')]").click()

    #33 / 46
    #How would you describe your physical health?
    driver.find_element_by_xpath("//button[contains (text(), 'Good')]").click()

    #34 / 46
    #Do you have or have you ever had any of the following conditions?
    #driver.find_element_by_xpath("//button[contains (text(), 'None apply')]").click()
    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake34 = driver.find_element_by_xpath("//button[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intake34)

    intake34Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake34Button)

    #35 / 46
    #Now we need to ask a couple common questions about your social history and home life. Honest answers will help your provider offer the best care for you, and your responses are kept private and protected.
    driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

    #36 / 46
    #Do you smoke or use other tobacco products?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #37 / 46
    #How many alcoholic beverages do you drink per week?
    driver.find_element_by_xpath("//button[contains (text(), '0-1 per week')]").click()

    #38 / 46
    #Have you had more than 5 drinks at one time in a row sometime over the past 30 days?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #39 / 46
    #Are you currently using any of the following recreational drugs?
    #driver.find_element_by_xpath("//button[contains (text(), 'None apply')]").click()
    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    intake39 = driver.find_element_by_xpath("//button[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intake39)

    intake39Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    driver.execute_script("arguments[0].click()", intake39Button)

    #40 / 46
    #Do you live alone?
    driver.find_element_by_xpath("//button[contains (text(), 'Yes')]").click()

    #// 41 of 46
    #// Please list the name, relationship, and phone number of your emergency contact.
    #// Your provider may ask your emergency contact to offer support if you are experiencing an emergency.
    #driver.findElement(By.id("19301_TA_ID")).sendKeys("test order 340 bryant st!")
    #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()

    #41 / 46
    #In case of an emergency, is there someone we can contact?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #42 / 46
    #Do you have any other medical conditions?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #43 / 46
    #Have you ever had any surgeries or hospitalizations?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #44 / 46
    #Are you taking any other prescription medication, over-the-counter medication, supplements or herbal remedies?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #45 / 46
    #Do you have any allergies to food, dyes, medication, or anything else?
    driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    #46 / 46
    #Is there anything else your provider should know?
    # driver.find_element_by_xpath("//button[contains (text(), 'No')]").click()

    driver.find_element_by_id("19311_TA_ID").send_keys("TEST ORDER Thx DOC for the review & medicine!")
    driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()
