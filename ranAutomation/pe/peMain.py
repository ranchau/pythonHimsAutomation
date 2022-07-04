import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from random import randint
from numpy import random

FirstName = "TestHims"
LastName = "TestHers"
AddressLine1 = "3121 Diablo Ave"
AddressLine2 = " "
City = "Hayward"
Zip = "94545"
Phonenumber = "888" + "555" + str(random.rand()*1000)
username = ("ranjit+cronofy+0301+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")

CC = "4085380151154156"
ExpDate = "0622"
CVC = "908"

# randint(0, 9)
# Phonenumber = "888" + "555" + Phonenumber1.substring(Phonenumber1.length() - 4, Phonenumber1.length())
#  &experiment.edFrequencyNewProducts=control
# System.setProperty("webdriver.chrome.driver", "/Users/rchaudhary/eclipse-workspace/chromedriver")
# driver = webdriver.Chrome()
# driver.get("https://www.forhims.com")
# assert "Python" in driver.title  premature-ejaculation
# url = "https://www.forhims.com/consultation/premature-ejaculation?edMBG=on&experiment.edMBGBanners=treatment&coupon=startfor5upto40sild&experiment.edDrugRecommendation=control&experiment.hersAcnePicasso=treatment&hairLossDrFirst=off&experiment.hairLossDrFirst=treatment&experiment.hairLossCheckoutFirst=treatment&experiment.smsRetargetingED=control&experiment.smsRetargetingHairLoss=treatment&hairLossFMF=off&split.hairLossSingleScreenCrossSell=on&experiment.hairLossPatientConversationShift=control&experiment.edOtcCrossSellBlock=treatment&experiment.hairLossOtcCrossSellBlock=treatment&experiment.displayUpgradeButtonHairLoss=treatment&experiment.displayUpgradeButtonED=treatment&experiment.edEducationAnimationRevamp=treatment&experiment.edMonthlySkuUnAvailable=treatment&experiment.hairLossDiagnosticPhotosReorder=treatment&experiment.hairLossSelfiePhotoReorder=treatment&experiment.acneMinor=treatment&experiment.hersAcneStreamlined=treatment&experiment.himsAgingStreamlined=treatment&experiment.himsAgingFreeOTC=treatment&experiment.hairLossTopicalFinasMinox=treatment&experiment.hairLossRenewalDefaultShipping=treatment&experiment.newSchedulingApi=control&experiment.edRenewalAdjust=treatment"

url = "https://6298-prod.dev.forhims.com/consultation/premature-ejaculation?edSkipIntro=off&experiment.edDrugRecommendation=control&edMBG=on&experiment.edMBGBanners=treatment&experiment.psychPicasso=treatment&coupon=startfor5upto40sild&experiment.psychMonthlyBilling=treatment&hairLossDrFirst=off&experiment.hairLossCheckoutFirst=treatment&experiment.edRenewalRefresh=treatment&experiment.edMonthlySkuUnavailable=treatment&experiment.hairLossDrFirst=treatment&cadence=kit12&experiment.hersAcneStreamlined=treatment&community=freetrial2020&experiment.smsRetargetingED=control&experiment.smsRetargetingHairLoss=treatment&hairLossFMF=off&split.hairLossSingleScreenCrossSell=on&experiment.hairLossPatientConversationShift=treatment&experiment.edOtcCrossSellBlock=treatment&experiment.hairLossOtcCrossSellBlock=treatment&experiment.displayUpgradeButtonHairLoss=treatment&experiment.displayUpgradeButtonED=treatment&experiment.edPhotoStageTransition=treatment&experiment.hairLossCHKAnnualSKU=treatment&experiment.edRenewalRefresh=treatment&experiment.edEducationAnimationRevamp=treatment&experiment.registrationStreamlined=treatment&experiment.acneMinor=treatment&experiment.edProviderMessage=treatment&experiment.himsAgingFreeOTC=treatment&experiment.hairLossRenewalDefaultShipping=treatment&experiment.skinRenewalRefresh=treatment&experiment.newSchedulingApi=treatment&experiment.hersAcnePicasso=control&experiment.hersAcnePicassoTOF=treatment&experiment.hersAcnePicassoRoutine=treatment&experiment.hersAcnePicassoPhotos=treatment&experiment.hersAcnePicassoConfirm=treatment&experiment.edRenewalAdjust=treatment&experiment.edResumeStage=treatment"

# http://0-1049-0-prod.dev.forhims.com/  experiment.enableSchedulingForFlows=control
# https://www.forhers.com/?experiments.edOtcCrossSellBlock=treatment&split.edEducationAnimation=variant1&split.consultationEdShippingBeforePhotos=on&split.consultationEdUsagePage=off&community=freetrial2020&split.hersAcneTry29=on&experiments.hairLossOtcCrossSellBlock=treatment

# [SX-15192] Select a different Sertraline SKU #6298

driver = webdriver.Chrome("/Users/rchaudhary/eclipse-workspace/chromedriver")
    
driver.maximize_window()
driver.implicitly_wait(20)

def getURL():
    # [SX-12522] Top of funnel and OTC flow for Premature Ejaculation #5464
    # [SX-12524][SX-13052] PE Drug recommendation rules and Logic cleanup #5591

    driver.get(url)
getURL()
time.sleep(1.5)

def peTOF():
    # // /premature-ejaculation/intro-transition-step
    time.sleep(3)
        # //premature-ejaculation/pej-frequency-question-step
    driver.find_element_by_xpath("//label[@for='undefined-halfTime']").click()

    # transition page   
    time.sleep(1.5)

    # // premature-ejaculation/pej-results-question-step
    driver.find_element_by_xpath("//label[@for='undefined-hard']").click()
    # // transition-step
    time.sleep(1.5)

    # // premature-ejaculation/prescription-preference-step
    driver.find_element_by_xpath("//label[@for='prescription-preference-question-MODIFIED_PRESCRIPTION']").click()
    # // -transition-step
    time.sleep(1.5)
    # premature-ejaculation/pej-treatment-faq-step
    driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

peTOF()
# //First Page - Select State
selectState = Select(driver.find_element_by_name("state"))
selectState.select_by_visible_text("California")
# selectState.select_by_visible_text("West Virginia")
# selectState.select_by_visible_text("Arizona")
# selectState.select_by_visible_text("Delaware")
# selectState.select_by_visible_text("District of Columbia")


# //Select Checkbox
driver.find_element_by_xpath("//*[@data-testid='ConsultationConsent']").click()
		
# //Click CTA		
driver.find_element_by_xpath("//*[@data-testid='SelectStateFormSubmitButton']").click()
		
# Second Page - Enter DOB
driver.find_element_by_id("dob").send_keys("10101990")
# ("05051971")
		
# //Submit DOB
driver.find_element_by_xpath("//button[@data-testid='DateOfBirthFormSubmitButton']").click()

# //Third Page - Register Page
username = ("ranjit+cronofy+0302+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys("asdf96@@PB")
# //Click Register CTA
driver.find_element_by_xpath("//*[@data-testid='ConsultationRegisterAccountButton']").click()

# //questionnaire-landing-step
driver.find_element_by_xpath("//*[@data-testid='ExplanationPageContinue']").click()
time.sleep(1.5)

# sms retargeting pop up modal skip  experiment.smsRetargetingED=treatment
# driver.find_element_by_xpath("//button[contains (text(), 'Skip')]").click()
breakpoint() 

time.sleep(1.5)
# edNewIntake.edNewIntakeMain()

# 2 WAY message
driver.find_element_by_name("patientConversation").send_keys("hi, thank you for reviewing my info")
# ("test's order ed's stage new visit 01-15-2021 ! plz give me the med's doc! doc u r the awesome doc! plz plz help me doc, i really need the med!!")

# // PatientConversationFormSubmitButton
driver.find_element_by_xpath("//*[@data-testid='PatientConversationFormSubmitButton']").click()
time.sleep(2)

# //Treatment Preference
driver.find_element_by_xpath("//*[@data-testid='TreatmentDrugSelectContinue']").click()

time.sleep(2)

# //ed-education-animation-step
# driver.find_element_by_xpath("//button[@data-testid='EducationAnimationContinue']").click()
edAnimationButton = driver.find_element_by_xpath("//button[@data-testid='EducationAnimationContinue']")
driver.execute_script("arguments[0].click()", edAnimationButton)
# EducationAnimationContinueRevamped
time.sleep(2)
# // Stage Use 6 times per month
driver.find_element_by_xpath("//img[@src='/forhims/image/upload/q_auto,f_auto,fl_lossy,c_limit/03-TreatmentPreference-Packets-6-2x']").click()
# https://res.cloudinary.com/forhims/image/upload/q_auto,f_auto,fl_lossy/03-TreatmentPreference-Packets-6-2x
# drugUsageButton = driver.find_element_by_id("drug-usage-a8aukYKX-qty-6").click()
# driver.execute_script("arguments[0].click()", drugUsageButton)

# //*** Shipment Frequency
driver.find_element_by_id("freq-select-0").click()

# // ed/packaging-selection-step
driver.find_element_by_id("packaging-option-0").click()

# When PHOTO upload is after shipping
# //Visit Summary V2
driver.find_element_by_xpath("//p[contains (text(), 'Visit Summary')]").is_displayed()

driver.find_element_by_xpath("//h1[contains (text(), 'Almost done!')]").is_displayed()

# driver.find_element_by_xpath("//*[@data-testid='VisitSummary-Continue']").click()
edSummaryButton = driver.find_element_by_xpath("//*[@data-testid='VisitSummary-Continue']")
driver.execute_script("arguments[0].click()", edSummaryButton)

def ShippingAddressPageCrossSell():

    driver.find_element_by_id("firstName").send_keys(FirstName)
    driver.find_element_by_id("lastName").send_keys(LastName)
    driver.find_element_by_id("line1").send_keys(AddressLine1)
    driver.find_element_by_id("line2").send_keys(AddressLine2)
    driver.find_element_by_id("city").send_keys(City)
    # //Selecting Dropdawn State
    dropState = Select (driver.find_element_by_name("state"))
    dropState.select_by_visible_text("Arizona")
    # dropState.select_by_visible_text("California")
    
    
    driver.find_element_by_id("zip").send_keys(Zip)
    driver.find_element_by_id("phone").send_keys(Phonenumber)
    driver.find_element_by_xpath("//button[@data-testid='ConsultationSaveAddressButton']").click()

    # //Shippo suggested

    # for AZ 
    driver.find_element_by_xpath("//*[@data-testid='address-choice-original']").click()

    #  for CA 
    # driver.find_element_by_xpath("//*[@data-testid='address-choice-suggested']").click()
    
    driver.find_element_by_xpath("//*[@data-testid='ConsultationShippingSelectAddressButton']").click()

ShippingAddressPageCrossSell()

def edPhotoUpload(): 

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

edPhotoUpload()

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
	driver.find_element_by_xpath("//*[@data-testid='ConsultationPaymentSubmitButton']").click()

paymentCC()

