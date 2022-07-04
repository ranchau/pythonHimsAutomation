
import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from numpy import random
import psychBase as psychMainDriver

import psychNewIntake
import psychPicassoIntake

FirstName = "TestHims"
LastName = "TestHers"
AddressLine1 = "3121 Diablo Ave"
AddressLine2 = " "
City = "Hayward"
Zip = "94545"
Phonenumber = "888" + "555" + str(random.rand()*1000)
username = ("ranjit+mh+0820") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
# username = "ranjitnp2001@gmail.com"

CC = "4085380151154156"
ExpDate = "0622"
CVC = "908"

driver = psychMainDriver.driver
driver.maximize_window()
driver.implicitly_wait(20)

# url = "https://www.forhers.com/consultation/mental-health"    &experiment.mhThreeMonthOptionV3=treatment

# url = "https://www.forhers.com/c/mh?experiment.mhMedInterest=treatment&experiment.mhMultiMonthV4=treatment&experiment.mhTofRedesign=control&experiment.mhPHQGADRedesign=control"

url = "https://master-staging.dev.forhers.com/c/mh?experiment.mhMedInterest=treatment&experiment.mhMultiMonthV4=treatment&experiment.mhTofRedesign=control&experiment.mhPHQGADRedesign=control"

#  ### [SX-21181] - MH PHQ&GAD redesign experiment #8664  https://8664-prod.dev.forhers.com?experiment.mhPHQGADRedesign=treatment

#  ***** [Sx 20132] Hers Psych Google Shopping launch #8448 - hersGSpsychflow productId=XODzKimh

# https://8569.dev.forhims.com/c/mh?experiment.mhTherapyCouponField=treatment&coupon=active

    #  **** https://8358-prod.dev.forhims.com/?experiment.intakeV2AntiAging=treatment


#  ******** They are in TX and AZ 1KMW81tbwohttps://github.com/Clubroom/hers/pull/8499
# ***** [SX-21207] - MH shipping cadence experiment mhMultiMonthV4 #8494

def getURL():
	driver.get(url)
        # [SX-12489] scheduling via Wheel also along with cronofy #5441 ?experiment.newSchedulingApi=treatment
        # [SX-15873][SX-15872] - Psych allow modality change to sync and remove psych scheduling for async visit modalities #6553

# Mental health: https://6499.dev.forhims.com/consultation/mental-health?coupon=free-visit
# Primary care: https://6499.dev.forhims.com/consultation/primary-care?coupon=free-visit

getURL()

time.sleep(3)
# psychPicassoIntake.psychPicassoMain()
        # // clicking the CTA **** 
        # /consultation/mental-health/welcome
driver.find_element_by_xpath("//button[@data-testid='footerButton']").click()

# consultation/mental-health/check-in
driver.find_element_by_xpath("//button[@data-testid='footerButton']").click()

# ///consultation/mental-health/your-mood
driver.find_element_by_xpath("//figure[@data-testid='moodCard-Sad']").click()

# /consultation/mental-health/to-mindfulness
driver.find_element_by_xpath("//button[@data-testid='footerButton']").click()

# /consultation/mental-health/your-name


time.sleep(2)

# //https://www.forhers.com/consultation/mental-health/your-name
driver.find_element_by_xpath("//input[@data-testid='inputField']").send_keys("Testhims")
driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

# Transition Step
time.sleep(3)

# https://www.forhers.com/consultation/mental-health/select-state
driver.find_element_by_xpath("//*[@name='state']").send_keys("California")
# driver.find_element_by_xpath("//*[@placeholder='state']").send_keys("West Virginia")
# driver.find_element_by_xpath("//*[@placeholder='state']").send_keys("Arizona")
# driver.find_element_by_xpath("//*[@placeholder='state']").send_keys("Illinois")


# driver.find_element_by_xpath("//button[@data-testid='suggestedState']").click()

driver.find_element_by_xpath("//span[@data-testid='ConsultationConsent']").click()
driver.find_element_by_xpath("//button[@data-testid='SelectStateFormSubmitButton']").click()


# intakeLegalAgreementCheckbox = driver.find_element_by_xpath("//label[contains (text(), 'I agree to the')]")
# driver.execute_script("arguments[0].click()", intakeLegalAgreementCheckbox)

# driver.find_element_by_xpath("//button[@data-testid='ConsultationConsent']").click()

# driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

# https://www.forhers.com/consultation/mental-health/date-of-birth

driver.find_element_by_xpath("//*[@name='dob']").send_keys("10311980")
driver.find_element_by_xpath("//button[@data-testid='DateOfBirthFormSubmitButton']").click()


# driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

# https://www.forhers.com/consultation/mental-health/select-treatment

def selectPsychTreatment():
    # Select Medication     
    driver.find_element_by_xpath("//figure[@data-testid='cardWithImage-Medication']").click()
    # Select Therapy
    # driver.find_element_by_xpath("//figure[@data-testid='cardWithImage-Therapy']").click()
    # Select Therapy + Medication
    # driver.find_element_by_xpath("//figure[@data-testid='cardWithImage-Therapy + Medication']").click()
    # Select I'm not sure
    # driver.find_element_by_xpath("//figure[@data-testid='cardWithImage-I’m not sure']").click()

selectPsychTreatment()

# https://www.forhers.com/consultation/mental-health/your-experience
driver.find_element_by_xpath("//figure[@data-testid='cardWithIcon-Somewhat familiar']").click()

# https://www.forhers.com/consultation/mental-health/in-the-right-place
driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

# https://www.forhers.com/consultation/mental-health/account
driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("password").send_keys("rt%^352MQNDS")
# rt%^352MQNDS         asdf96&&PB
# asdf96@@PB

# driver.find_element_by_xpath("//div[@data_testid='legalAgreementCheckbox']").click()

# intakeLegalAgreementCheckbox = driver.find_element_by_xpath("//label[contains (text(), 'I agree to the')]")
# driver.execute_script("arguments[0].click()", intakeLegalAgreementCheckbox)

# driver.find_element_by_xpath("//label[contains (text(), 'I agree to the')]").click()
driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()
time.sleep(2)

# //Click Continue ***  /c/mh/deeper-look
driver.find_element_by_xpath("//*[@data-testid='footerButton']").click()
time.sleep(2)
		
# //Click CTA		*** /c/mh/how-it-works
driver.find_element_by_xpath("//*[@data-testid='footerButton']").click()
time.sleep(2)


psychNewIntake.psychNewIntakeMain()

time.sleep(2)

def ShippingAddressPageCrossSell():

    driver.find_element_by_id("firstName").send_keys(FirstName)
    driver.find_element_by_id("lastName").send_keys(LastName)
    driver.find_element_by_id("line1").send_keys(AddressLine1)
    driver.find_element_by_id("line2").send_keys(AddressLine2)
    driver.find_element_by_id("city").send_keys(City)
    # //Selecting Dropdawn State
    dropState = Select (driver.find_element_by_name("state"))
    dropState.select_by_visible_text("California")
    # dropState.select_by_visible_text("Arizona")
    # dropState.select_by_visible_text("West Virgina")
    
    driver.find_element_by_id("zip").send_keys(Zip)
    driver.find_element_by_id("phone").send_keys(Phonenumber)
    driver.find_element_by_xpath("//button[@data-testid='ConsultationSaveAddressButton']").click()

    # //Shippo suggested
    driver.find_element_by_xpath("//*[@data-testid='address-choice-suggested']").click()
    
    driver.find_element_by_xpath("//*[@data-testid='ConsultationShippingSelectAddressButton']").click()

ShippingAddressPageCrossSell()

def PhotoUpload(): 
    
    UploadPhotoID = driver.find_element_by_xpath("//input[@type='file']")
    # driver.execute_script("arguments[0].click()", UploadPhotoID)

    filePathID = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/pencilimageforuploadID.png"

    UploadPhotoID.send_keys(filePathID)
    
    # //photo-upload-1 C
    edIDButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edIDButton)
    
    time.sleep(2.5)
    
    # //UPlOAD SELFIE
    UploadPhotoSELFIE = driver.find_element_by_xpath("//input[@type='file']")
    filePathSELFIE = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/UploadSELFIE.jpg"

    UploadPhotoSELFIE.send_keys(filePathSELFIE)
    
    # //photo-upload-2 
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']")).click()
    edSelfieButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edSelfieButton)
    
    time.sleep(2.5)

PhotoUpload()

def paymentCC():
	driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@name, '__privateStripeFrame')]"))
	time.sleep(2)
	inputCC = driver.find_element_by_name("cardnumber")
	time.sleep(2)
	inputCC.send_keys(CC)

	time.sleep(2)
	driver.find_element_by_name("exp-date").send_keys(ExpDate)
	time.sleep(2)
	driver.find_element_by_name("cvc").send_keys(CVC)

	driver.switch_to.default_content()
	driver.find_element_by_xpath("//*[@data-testid='paymentButton']").click()

paymentCC()



