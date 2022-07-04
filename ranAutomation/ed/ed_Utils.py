import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from numpy import random
import Base as newUtils
import edNewIntake

FirstName = "Testhims"
LastName = "Testhers"
AddressLine1 = "3121 Diablo Ave"
AddressLine2 = " "
City = "Hayward"
Zip = "94545"
Phonenumber = "888" + "555" + str(random.rand()*1000)
# username = ("ranjit+cronofy+ed+0301+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
username = ("njaensch+cronfy+0301+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")

# confidence1
CC = "4085380151154156"
ExpDate = "0622"
CVC = "908"

States = "California"
# States = "Delaware"
# States = "West Virginia"


def SelectState():
    driver = newUtils.driver

    # //First Page - Select State
    selectState = Select(driver.find_element_by_name("state"))
    selectState.select_by_visible_text(States)
    # selectState.select_by_visible_text("Oregon")
    # selectState.select_by_visible_text("North Dakota")
    # selectState.select_by_visible_text("Texas")

    # selectState.select_by_visible_text("West Virginia")
    # selectState.select_by_visible_text("Arizona")
    # alreadySelectedState = selectState.select_by_visible_text("Delaware")
    # selectState.select_by_visible_text("District of Columbia")

def ShippingAddressPageCrossSell():
    
    driver = newUtils.driver

    driver.find_element_by_id("firstName").send_keys(FirstName)
    driver.find_element_by_id("lastName").send_keys(LastName)
    driver.find_element_by_id("line1").send_keys(AddressLine1)
    driver.find_element_by_id("line2").send_keys(AddressLine2)
    driver.find_element_by_id("city").send_keys(City)
    # //Selecting Dropdawn State

    # selectState = Select(driver.find_element_by_name("state"))
    # selectState.select_by_visible_text(States)
    SelectState()

    # dropState = Select (driver.find_element_by_name("state"))
    # dropState.select_by_visible_text("Delaware")
    # dropState.select_by_visible_text("California")
    # dropState.select_by_visible_text("Arizona")
    # dropState.select_by_visible_text(" North Dakota")

    driver.find_element_by_id("zip").send_keys(Zip)
    driver.find_element_by_id("phone").send_keys(Phonenumber)
    driver.find_element_by_xpath("//button[@data-testid='ConsultationSaveAddressButton']").click()
    time.sleep(4)

    # //Shippo suggested
    if (States=="California"):
        #  for CA 
        driver.find_element_by_xpath("//*[@data-testid='address-choice-suggested']").click()
    else:
        # for DE
        driver.find_element_by_xpath("//*[@data-testid='address-choice-original']").click()
    
    driver.find_element_by_xpath("//*[@data-testid='ConsultationShippingSelectAddressButton']").click()

def edPhotoUpload(): 

    driver = newUtils.driver

	# //ED Photo Upload
    # JavascriptExecutor executor = (JavascriptExecutor)driver

    # //photo-upload-1		
    # //below photo upload code works only when input type is file
    
    UploadPhotoID = driver.find_element_by_xpath("//input[@type='file']")
    # driver.execute_script("arguments[0].click()", UploadPhotoID)

    filePathID = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/pencilimageforuploadID.png"
    # "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/pencilimageforuploadID.png"
    # "/Photos/pencilimageforuploadID.png"
    # ranAutomation/Photos/pencilimageforuploadID.png

    UploadPhotoID.send_keys(filePathID)
    
    # //photo-upload-1 Confirmation page for NO TREATMENT
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']").click()
    edIDButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edIDButton)
    
    time.sleep(2.5)
    # //ID RETAKE
    driver.find_element_by_xpath("//button[contains (text(), 'Retake ID Photo')]").click()
    time.sleep(2.5)
    
    # //TRY to Upload ID Aagain
    UploadPhotoIDRE = driver.find_element_by_xpath("//input[@type='file']")
    filePathIDRE = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/pencilimageforuploadID.png"

    UploadPhotoIDRE.send_keys(filePathIDRE)
    
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']")).click()
    edIDAgainButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edIDAgainButton)
    time.sleep(2.5)

    # //ID Proceed Anyway
    driver.find_element_by_xpath("//button[contains (text(), 'Proceed Anyway')]").click()
    time.sleep(2.5)
    
    # //UPlOAD SELFIE
    UploadPhotoSELFIE = driver.find_element_by_xpath("//input[@type='file']")
    filePathSELFIE = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/UploadSELFIE.jpg"

    UploadPhotoSELFIE.send_keys(filePathSELFIE)
    
    # //photo-upload-2 Confirmation page for NO TREATMENT
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']")).click()
    edSelfieButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edSelfieButton)
    
    time.sleep(2.5)
    
    # //FACE RETAKE
    driver.find_element_by_xpath("//button[contains (text(), 'Retake Face Photo')]").click()
    time.sleep(2.5)
    
    # //TRY to Upload FACE AGAIN
    UploadPhotoSELFIERE = driver.find_element_by_xpath("//input[@type='file']")
    filePathSELFIERE = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/UploadSELFIE.jpg"

    UploadPhotoSELFIERE.send_keys(filePathSELFIERE)
    
    # //Confirmation for FACE RETAKE
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']")).click()
    edSelfieAgainButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edSelfieAgainButton)
    time.sleep(2.5)

    # //SELFIE Proceed Anyway
    driver.find_element_by_xpath("//button[contains (text(), 'Proceed Anyway')]").click()
    time.sleep(2.5)


def paymentCC():

    driver = newUtils.driver
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
    driver.find_element_by_xpath("//*[@data-testid='ConsultationPaymentSubmitButton']").click()

    #  The below only for GOOGLE Shopping V3

def edGoogleShoppingV3():
    ShippingAddressPageCrossSell()
    edPhotoUpload()
    paymentCC()
    driver = newUtils.driver

    # time.sleep(1.5)
    # # //questionnaire-landing-step
    driver.find_element_by_xpath("//*[@data-testid='ExplanationPageContinue']").click()
    time.sleep(1.5)

    edNewIntake.edNewIntakeMain()

    # # 2 WAY message
    driver.find_element_by_name("patientConversation").send_keys("hi, thank you for reviewing my info")

    # # // PatientConversationFormSubmitButton
    driver.find_element_by_xpath("//*[@data-testid='PatientConversationFormSubmitButton']").click()
    time.sleep(2)

