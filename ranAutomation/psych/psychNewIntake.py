import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from numpy import random
import psychBase as psychIntakMainDriver

driver = psychIntakMainDriver.driver

def psychNewIntakeMain():
    # driver = webdriver.Chrome("/Users/rchaudhary/eclipse-workspace/chromedriver")

    print("i am here in intake method")
    print(driver)


    #1 / 42
    #Over the last 2 weeks, how often have you been bothered by little interest or pleasure in doing things?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #        2 / 42
    #Over the last 2 weeks, how often have you been bothered by feeling down, depressed, or hopeless?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #3 / 42
    #Over the last 2 weeks, how often have you been bothered by trouble falling or staying asleep, or sleeping too much? 
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #4 / 42
    #Over the last 2 weeks, how often have you been bothered by feeling tired or having little energy?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #5 / 42
    #Over the last 2 weeks, how often have you been bothered by poor appetite or eating? 
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #6 / 42
    #Over the last 2 weeks, how often have you been bothered by feeling bad about yourself, that you are a failure, or have let yourself or your family down?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #7 / 42
    #Over the last 2 weeks, how often have you been bothered by trouble concentrating on things such as reading the newspaper or watching tv?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #8 / 42
    #Over the last 2 weeks, how often have you been bothered by moving or speaking so slowly that other people have noticed, OR being so fidgety or restless that you have been moving around a lot more than usual?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #9 / 42
    #If you checked any problems, how difficult have they made it for you to do your work, take care of things at home, or get along with other people?
    driver.find_element_by_xpath("//p[contains (text(), 'Somewhat difficult')]").click()

    #10 / 42
    #Over the last 2 weeks, how often have you been bothered by feeling nervous, anxious, or on edge?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #11 / 42
    #Over the last 2 weeks, how often have you been bothered by not being able to control worrying?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #12 / 42
    #Over the last 2 weeks, how often have you been bothered by worrying too much about different things?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #13 / 42
    #Over the last 2 weeks, how often have you been bothered by trouble relaxing?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #14 / 42
    #Over the last 2 weeks, how often have you been bothered by being so restless that it is hard to sit still?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #15 / 42
    #Over the last 2 weeks, how often have you been bothered by becoming easily annoyed or irritable?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #16 / 42
    #Over the last 2 weeks, how often have you been bothered by feeling afraid as if something awful might happen?
    driver.find_element_by_xpath("//p[contains (text(), 'Several days')]").click()

    #17 / 42
    #If you checked any problems, how difficult have they made it for you to do your work, take care of things at home, or get along with other people?
    driver.find_element_by_xpath("//p[contains (text(), 'Somewhat difficult')]").click()

    #18 / 42
    #Which mental health condition(s) are you seeking services for?
    #driver.find_element_by_xpath("//p[contains (text(), 'Performance anxiety (eg. stage fright)')]").click()
    time.sleep(2)

#  /c/mh/phq-gad-results

    driver.find_element_by_xpath("//button[@data-testid='footerButton']").click()
    time.sleep(2)
#  /c/mh/understanding-your-results
    driver.find_element_by_xpath("//button[@data-testid='footerButton']").click()
    time.sleep(2)
# /c/mh/bigger-picture
    driver.find_element_by_xpath("//button[@data-testid='footerButton']").click()
    time.sleep(2)
# /c/mh/history
    driver.find_element_by_xpath("//button[@data-testid='footerButton']").click()
    time.sleep(2)

#  /c/mh/history-questions?offset=0

    # intake18 = driver.find_element_by_xpath("//p[contains (text(), 'Performance anxiety (eg. stage fright)')]")
    #  general anxiety
    intake18 = driver.find_element_by_xpath("//p[contains (text(), 'Generalized anxiety (e.g. persistent, general worry)')]")
    driver.execute_script("arguments[0].click()", intake18)

    intake18Button = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    driver.execute_script("arguments[0].click()", intake18Button)
    time.sleep(2)

#  How have you been feeling for the past few weeks?
    driver.find_element_by_xpath("//p[contains (text(), 'Sad')]").click()
    intakeHistorySadButton = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    driver.execute_script("arguments[0].click()", intakeHistorySadButton)
    time.sleep(2)


# Have you been diagnosed or have a history of any of the following mental health conditions?
    intakeHistoryOffset2 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intakeHistoryOffset2)

    # intakeHistoryOffset2Button = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    # driver.execute_script("arguments[0].click()", intakeHistoryOffset2Button)
    # time.sleep(2)

# Do you currently have any desire to harm yourself or others?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Are you currently worried that you might harm yourself or others?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Do you have a family history of any mental health conditions?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Is there a specific mental health medication you are interested in and would like to discuss with your provider?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Have you ever taken or are you currently taking any mental health medication?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Are you currently taking other prescription medication, over-the-counter medication, supplements or herbal remedies?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# What is your gender?
    driver.find_element_by_xpath("//p[contains (text(), 'Woman')]").click()

# What was your sex assigned at birth?
    driver.find_element_by_xpath("//p[contains (text(), 'Female')]").click()

# Are you currently pregnant?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Are you currently breastfeeding?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Do you have or have you ever had any of the following conditions?
    intakeHistoryOffset13 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intakeHistoryOffset13)

    # intakeHistoryOffset13Button = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    # driver.execute_script("arguments[0].click()", intakeHistoryOffset13Button)
    # time.sleep(2)

# Do you have any other medical conditions?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Have you ever had any surgeries or hospitalizations?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# Do you have any allergies to food, dyes, medication, or anything else?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()
    time.sleep(2)

#  /c/mh/lifestyle
    intakeLifestyleButton = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    driver.execute_script("arguments[0].click()", intakeLifestyleButton)
    time.sleep(2)

#  Do you smoke or use other tobacco products?
    driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

# How often in the last year have you had 5 or more alcoholic drinks (male), or 3 or more alcoholic drinks (female) on one occasion?
    driver.find_element_by_xpath("//p[contains (text(), 'Never')]").click()

# Are you currently using any of the following recreational drugs?
    intakeLifeStyleOffset2 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    driver.execute_script("arguments[0].click()", intakeLifeStyleOffset2)

    intakeLifeStyleOffset2Button = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    driver.execute_script("arguments[0].click()", intakeLifeStyleOffset2Button)
    time.sleep(2)

# /c/mh/contact
    # driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()
    # intakeContactButton = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    # driver.execute_script("arguments[0].click()", intakeContactButton)
    time.sleep(2)
    
# In case of an emergency, is there someone we can contact?
    intakeContactOffset0 = driver.find_element_by_xpath("//p[contains (text(), 'No')]")
    driver.execute_script("arguments[0].click()", intakeContactOffset0)
    time.sleep(2)

# /c/mh/patient-dialogue
# Is there anything else you would like your provider to know? Or any questions for your provider?
    driver.find_element_by_xpath("//textarea[@data-testid='patient-dialogue']").send_keys("No questions")
    intakePatientDialogueButton = driver.find_element_by_xpath("//button[@data-testid='footerButton']")
    driver.execute_script("arguments[0].click()", intakePatientDialogueButton)
    time.sleep(6)

# /c/mh/get-personalized
    # intakePersonalizedButton = driver.find_element_by_xpath("//button[contains (text(), 'See my treatment options')]")
    # driver.execute_script("arguments[0].click()", intakePersonalizedButton)

# /c/mh/your-treatment
    intakeYourTreatmentButton = driver.find_element_by_xpath("//button[contains (text(), 'Continue')]")
    driver.execute_script("arguments[0].click()", intakeYourTreatmentButton)
    time.sleep(2)

# /c/mh/shipping-address

    # #21 / 43
    # #Is there any new or recent life event that may be impacting how you are feeling?
    # #driver.find_element_by_xpath("//p[contains (text(), 'Family or relationship problems')]").click()
    # #driver.find_element_by_xpath("//p[contains (text(), 'Life event or transition')]").click()

    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake21A = driver.find_element_by_xpath("//p[contains (text(), 'Family or relationship problems')]")
    # driver.execute_script("arguments[0].click()", intake21A)

    # intake21B = driver.find_element_by_xpath("//p[contains (text(), 'Life event or transition')]")
    # driver.execute_script("arguments[0].click()", intake21B)

    # intake21Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake21Button)

    # #22 / 43
    # #Do you have a history of any of the following mental health conditions?
    # #driver.find_element_by_xpath("//p[contains (text(), 'Anxiety')]").click()
    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake22 = driver.find_element_by_xpath("//p[contains (text(), 'Anxiety')]")
    # driver.execute_script("arguments[0].click()", intake22)

    # intake22Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake22Button)

    # #23 / 46
    # #Who diagnosed you for anxiety?
    # driver.find_element_by_xpath("//p[contains (text(), 'Healthcare provider')]").click()

    # #24 of 46
    # #When were you diagnosed for anxiety?
    # driver.find_element_by_id("19170_TA_ID").send_keys("TEST ORDER Thx DOC!")
    # driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()

    # #25 of 46
    # #Did you treat your anxiety with medications or therapy?
    # #If medication, please include name and dosage.
    # driver.find_element_by_id("19171_TA_ID").send_keys("TEST ORDER Thx DOC medicine!")
    # driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()

    # #26 / 46
    # #Do you have a family history of any of the following?
    # #driver.find_element_by_xpath("//p[contains (text(), 'Anxiety')]").click()

    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake26 = driver.find_element_by_xpath("//p[contains (text(), 'Anxiety')]")
    # driver.execute_script("arguments[0].click()", intake26)

    # intake26Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake26Button)

    # #27 / 46
    # #Are you currently using any of the following mental health medications?
    # #driver.find_element_by_xpath("//p[contains (text(), 'None apply')]").click()

    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake27 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    # driver.execute_script("arguments[0].click()", intake27)

    # intake27Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake27Button)

    # #28 / 46
    # #Are you currently taking any of the following other medications?
    # #driver.find_element_by_xpath("//p[contains (text(), 'None apply')]").click()

    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake28 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    # driver.execute_script("arguments[0].click()", intake28)

    # intake28Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake28Button)

    # #29 / 46
    # #Have you ever used any of the following mental health medications in the past?
    # #driver.find_element_by_xpath("//p[contains (text(), 'None apply')]").click()

    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake29 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    # driver.execute_script("arguments[0].click()", intake29)

    # intake29Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake29Button)

    # #30 / 46
    # #Have you ever participated in talk therapy or therapy sessions?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #31 / 46
    # #To which gender identity do you most identify with?
    # driver.find_element_by_xpath("//p[contains (text(), 'Male')]").click()

    # #32 / 46
    # #What was your sex assigned at birth?
    # driver.find_element_by_xpath("//p[contains (text(), 'Male')]").click()

    # #33 / 46
    # #How would you describe your physical health?
    # driver.find_element_by_xpath("//p[contains (text(), 'Good')]").click()

    # #34 / 46
    # #Do you have or have you ever had any of the following conditions?
    # #driver.find_element_by_xpath("//p[contains (text(), 'None apply')]").click()
    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake34 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    # driver.execute_script("arguments[0].click()", intake34)

    # intake34Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake34Button)

    # #35 / 46
    # #Now we need to ask a couple common questions about your social history and home life. Honest answers will help your provider offer the best care for you, and your responses are kept private and protected.
    # driver.find_element_by_xpath("//p[contains (text(), 'Continue')]").click()

    # #36 / 46
    # #Do you smoke or use other tobacco products?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #37 / 46
    # #How many alcoholic beverages do you drink per week?
    # driver.find_element_by_xpath("//p[contains (text(), '0-1 per week')]").click()

    # #38 / 46
    # #Have you had more than 5 drinks at one time in a row sometime over the past 30 days?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #39 / 46
    # #Are you currently using any of the following recreational drugs?
    # #driver.find_element_by_xpath("//p[contains (text(), 'None apply')]").click()
    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()

    # intake39 = driver.find_element_by_xpath("//p[contains (text(), 'None apply')]")
    # driver.execute_script("arguments[0].click()", intake39)

    # intake39Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
    # driver.execute_script("arguments[0].click()", intake39Button)

    # #40 / 46
    # #Do you live alone?
    # driver.find_element_by_xpath("//p[contains (text(), 'Yes')]").click()

    # #// 41 of 46
    # #// Please list the name, relationship, and phone number of your emergency contact.
    # #// Your provider may ask your emergency contact to offer support if you are experiencing an emergency.
    # #driver.findElement(By.id("19301_TA_ID")).sendKeys("test order 340 bryant st!")
    # #driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()

    # #41 / 46
    # #In case of an emergency, is there someone we can contact?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #42 / 46
    # #Do you have any other medical conditions?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #43 / 46
    # #Have you ever had any surgeries or hospitalizations?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #44 / 46
    # #Are you taking any other prescription medication, over-the-counter medication, supplements or herbal remedies?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #45 / 46
    # #Do you have any allergies to food, dyes, medication, or anything else?
    # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # #46 / 46
    # #Is there anything else your provider should know?
    # # driver.find_element_by_xpath("//p[contains (text(), 'No')]").click()

    # driver.find_element_by_id("19311_TA_ID").send_keys("TEST ORDER Thx DOC for the review & medicine!")
    # driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Textarea-Continue']").click()
