import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# from random import randint
from numpy import random
import Base as edMainDriver
import edNewIntake
import ed_Utils

FirstName = "Testhims"
LastName = "Testhers"
AddressLine1 = "3121 Diablo Ave"
AddressLine2 = " "
City = "Hayward"
Zip = "94545"
Phonenumber = "888" + "555" + str(random.rand()*1000)
username = ("Ranjit+cronofy+0720+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
# username = ("ranjit+vouched+0301+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")

# username = ("rio+test++vouched+0301+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")


# confidence1
CC = "4085380151154156"
ExpDate = "0622"
CVC = "908"

# CC = "4030150337076888"
# ExpDate = "0628"
# CVC = "667"

# randint(0, 9)
# Phonenumber = "888" + "555" + Phonenumber1.substring(Phonenumber1.length() - 4, Phonenumber1.length())
#  &experiment.edFrequencyNewProducts=control
# System.setProperty("webdriver.chrome.driver", "/Users/rchaudhary/eclipse-workspace/chromedriver")
# driver = webdriver.Chrome()
# driver.get("https://www.forhims.com")
# assert "Python" in driver.title  premature-ejaculation

# url = "https://www.forhims.com/c/e/?utm_medium=pla&productId=CYtlAn4ZXlI&experiment.isPricingService=treatment&experiment.edOnboardingNewCopy=treatment&edMBG=off&experiment.edMBGBanners=treatment&experiment.displayUpgradeButtonED=treatment&experiment.edEducationAnimationRevamp=treatment&experiment.edMonthlySkuUnAvailable=treatment&experiment.hairLossTopicalFinasMinox=treatment&experiment.hairLossRenewalDefaultShipping=treatment&experiment.edRenewalAdjust=treatment&experiment.googleShoppingSub=treatment&experiment.edNewCheckout=control&experiment.edOnboardingNewUI=control&experiment.edSildenafilTransition=treatment&experiment.googleShoppingCadence=control&experiment.edNewCheckout6mo=control&experiment.edViagraCialisModals=treatment&experiment.peNewCheckout=treatment&experiment.edCheckoutNewUI=treatment&experiment.intakeV2ED=treatment"

# edResumeStage
url = "https://8719.dev.forhims.com/c/e/?utm_medium=pla&experiment.isPricingService=treatment&experiment.contactRouting=treatment&experiment.himsHairConsultationTransitionV1=treatment&experiment.edOnboardingNewCopy=treatment&edMBG=off&experiment.edMBGBanners=treatment&experiment.displayUpgradeButtonED=treatment&experiment.edEducationAnimationRevamp=treatment&experiment.edMonthlySkuUnAvailable=treatment&experiment.hairLossTopicalFinasMinox=treatment&experiment.hairLossRenewalDefaultShipping=treatment&experiment.edRenewalAdjust=treatment&experiment.googleShoppingSub=treatment&experiment.edNewCheckout=control&experiment.edOnboardingNewUI=control&experiment.edSildenafilTransition=treatment&experiment.googleShoppingCadence=control&experiment.edNewCheckout6mo=control&experiment.edViagraCialisModals=treatment&experiment.peNewCheckout=treatment&experiment.edCheckoutNewUI=treatment&experiment.googleShoppingSubHair=treatment&experiment.confirmationAppSync=treatment&experiment.intakeV2ED=treatment"
# url = "https://0-3402-0-prod.dev.forhims.com/c/e?"  ?productId=CYtlAn4ZXlI     p= hDbOen6hbA

#  *** [STOR-1044] CA Cancel Flow #8759

#  ?loginRedirect=t         &experiment.confirmationApp=treatment&experiment.confirmationAppSync=treatment
#  ******** [SX-21577, SX-13578] fix(web): remove the skipping of the treatment preferences stage if "complete" #8445

#  ****** https://8719.dev.forhims.com?experiment.intakeV2ED=treatment    - new intake 


#  *** https://8215-prod.dev.forhims.com/?experiment.isPricingService=treatment

#  **** /consultation/google-shopping/premature-ejaculation?productId=STbNncSAX1U&utm_medium=pla

#    experiment.edGenericViagraRecommendation=treatment&experiment.edViagraCialisModals=treatment.

# CYtlAn4ZXlI

# https://www.forhims.com/erectile-dysfunction/sildenafil?env=master&experiment.sildenafilPDPHero=treatment

driver = edMainDriver.driver
    
driver.maximize_window()
driver.implicitly_wait(20)
# driver.get("https://www.forhims.com/consultation/ed/?split.edEducationAnimation=variant1&split.consultationEdShippingBeforePhotos=on&split.consultationEdUsagePage=off")
#  &experiment.enableSchedulingForFlows=treatment &experiment.edEducationAnimationRevamp=treatment
def getURL():

# https://github.com/Clubroom/hers/pull/6203
    # [SX-12425] ED DOB confirmation step #5898 confirmAgeName

    driver.get(url)
getURL()
time.sleep(1.5)

# driver.find_element_by_xpath("//*[@data-testid='start-consultation-flow']").click()

def edTOF():
    # // intro-transition-step
    time.sleep(5)
        # //pop-up dialog Checkbox
    # driver.find_element_by_xpath("//*[@data-testid='discount-cta']").click()

    # // ed/ed-questionnaire-frequency-step  How often are you suffering from ED?
    driver.find_element_by_xpath("//label[@for='questionnaire-frequency-step-halfTime']").click()
    # // ed/ed-questionnaire-frequency-transition-step
    time.sleep(5)

    # // ed/ed-questionnaire-results-step What sort of results are you looking for?
    driver.find_element_by_xpath("//label[@for='questionnaire-results-step-all']").click()
    # // /ed/ed-questionnaire-results-transition-step
    time.sleep(1.5)

edTOF()

# States = "California"
# States = "Delaware"
# //First Page - Select State
# selectState = Select(driver.find_element_by_name("state"))
# selectState.select_by_visible_text(States)

ed_Utils.SelectState()
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
username = ("ranjit+cronofy+0820+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
# username = ("rio+hers+e2e+new") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
# brian+75confidence1warningAgewarningName@forhims.com   84confidence1warningAgewarningName
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys("asdf96&&PB")
# prt%^352MQNDS
# 824PBasdf96&&
# //Click Register CTA
driver.find_element_by_xpath("//*[@data-testid='ConsultationRegisterAccountButton']").click()
# breakpoint()
time.sleep(3)

# // ******************************* **********************************// 

#  The below only for GOOGLE Shopping V3 & V4
# ed_Utils.edGoogleShoppingV3()
# ed_Utils.ShippingAddressPageCrossSell()
# ed_Utils.edPhotoUpload()
# ed_Utils.paymentCC()


# time.sleep(1.5)
# # # //questionnaire-landing-step
# driver.find_element_by_xpath("//*[@data-testid='ExplanationPageContinue']").click()
# time.sleep(1.5)

# edNewIntake.edNewIntakeMain()

# # # 2 WAY message
# driver.find_element_by_name("patientConversation").send_keys("hi, thank you for reviewing my info")

# # # // PatientConversationFormSubmitButton
# driver.find_element_by_xpath("//*[@data-testid='PatientConversationFormSubmitButton']").click()
# time.sleep(2)

# // ******************************* // 

# //questionnaire-landing-step
driver.find_element_by_xpath("//*[@data-testid='ExplanationPageContinue']").click()
time.sleep(1.5)

# sms retargeting pop up modal skip  experiment.smsRetargetingED=treatment
# driver.find_element_by_xpath("//button[contains (text(), 'Skip')]").click()

time.sleep(1.5)
edNewIntake.edNewIntakeMain()

# 2 WAY message
if (ed_Utils.States=="California"):
    driver.find_element_by_name("patientConversation").send_keys("No questions")

# # // PatientConversationFormSubmitButton
    driver.find_element_by_xpath("//*[@data-testid='PatientConversationFormSubmitButton']").click()
    time.sleep(2)
else:
    pass

# //Treatment Preference
# driver.find_element_by_xpath("//*[@data-testid='Sildenafil-brand-tile-cta']").click()
time.sleep(2)

#  trying to reload/refresh the page on the treatment page
# driver.refresh()
# #switch to popup
# driver.switch_to.alert.accept()

time.sleep(5)
driver.find_element_by_xpath("//*[@data-testid='Generic Viagra-brand-tile-cta']").click()

time.sleep(2)
#  Generic Viagra-brand-tile-cta
# //ed-education-animation-step
# driver.find_element_by_xpath("//button[@data-testid='EducationAnimationContinue']").click()
edAnimationButton = driver.find_element_by_xpath("//button[@data-testid='EducationAnimationContinue']")
driver.execute_script("arguments[0].click()", edAnimationButton)
# EducationAnimationContinueRevamped
time.sleep(2)
# // Stage Use 6 times per month
driver.find_element_by_xpath("//img[@src='/forhims/image/upload/q_auto,f_auto,fl_lossy,c_limit/03-TreatmentPreference-Packets-6-2x']").click()

# //*** Shipment Frequency
# driver.find_element_by_id("freq-select-2").click()

# // ed/packaging-selection-step
# driver.find_element_by_id("packaging-option-0").click()

# When PHOTO upload is after shipping
# //Visit Summary V2
# driver.find_element_by_xpath("//p[contains (text(), 'Visit Summary')]").is_displayed()

# driver.find_element_by_xpath("//h1[contains (text(), 'Almost done!')]").is_displayed()

# edSummaryButton = driver.find_element_by_xpath("//*[@data-testid='VisitSummary-Continue']")
# driver.execute_script("arguments[0].click()", edSummaryButton)


ed_Utils.ShippingAddressPageCrossSell()

ed_Utils.edPhotoUpload()

ed_Utils.paymentCC()
