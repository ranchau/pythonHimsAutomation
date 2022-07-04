import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from numpy import random
import hl_Base as hlMainDriver
import hl_Utils

FirstName = "TestHims"
LastName = "TestHers"
AddressLine1 = "3121 Diablo Ave"
AddressLine2 = " "
City = "Hayward"
Zip = "94545"
Phonenumber = "888" + "555" + str(random.rand()*1000)
username = ("ranjit+cronofy+0113+21") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")

CC = "4085380196652032"
ExpDate = "0122"
CVC = "072"

driver = hlMainDriver.driver

# System.setProperty("webdriver.chrome.driver", "/Users/rchaudhary/eclipse-workspace/chromedriver")
# driver = webdriver.Chrome()
# driver.get("https://www.forhims.com")
# assert "Python" in driver.title


# driver = webdriver.Chrome("/Users/rchaudhary/eclipse-workspace/chromedriver")
driver.maximize_window()
driver.implicitly_wait(20)

# experimentshairLossPatientConversationShift   ranjitchau0011@gmail.com
finasOnlyGoogleShoppingLP = "https://www.forhims.com/shop/hair-finasteride"
#  hairLossDrFirst=on
def getURL():
    # driver.get("https://www.forhims.com/c/gs/hl/?utm_medium=pla&productId=dSOIr3P3hNE")
    # driver.get(finasOnlyGoogleShoppingLP)
    # driver.find_element_by_xpath("//button[contains (text(), 'Add to cart')]").click()

    # driver.get("https://www.forhims.com/c/hl/?utm_medium=pla&productId=APSnOWod&experiment.himsHairConsultationTransitionV1=treatment&experiment.isPricingService=treatment&experiment.hairLossTopicalFinasMinox=control&experiment.hairLossDiagnosticPhotosReorder=treatment&experiment.hairLossOtcCrossSellBlock=control&experiment.hairSkinConfirmCrossSell=aacreampromo&experiment.himsHairTopFinRecco=treatment")
    
    driver.get("https://8738-prod.dev.forhims.com/c/hl/?utm_medium=pla&productId=APSnOWod&experiment.himsHairConsultationTransitionV1=treatment&experiment.isPricingService=treatment&experiment.hairLossTopicalFinasMinox=control&experiment.hairLossDiagnosticPhotosReorder=treatment&experiment.hairLossOtcCrossSellBlock=control&experiment.hairSkinConfirmCrossSell=aacreampromo&experiment.himsHairTopFinRecco=treatment")

    # driver.get("https://master-staging.dev.forhims.com/consultation/hair-loss/")

#  ***** [SX-21145] hims redesign treatment results screen v1 #8691
#  *** [SX-21437] - Hims registration screen redesign #8738

#  ******** ?loginRedirect=t
# ****** Hims Prod: https://8535-prod.dev.forhims.com
#  ***** [SX-21421] clean up experiment hairLossReducedChoice to control #8508 ?experimemt.hairLossReducedChoice=treatment
#  https://8358.dev.forhers.com/?experiment.intakeV2AntiAging=treatment

# ***** [SX-13487] clean up experiment hairLossTopicalFinasMinox to total treatment #8535


# **** [SX-17715] clean up experiment hairLossDrFirst to control #8058


#  ***** [SX-21146] set up himsHairConsultationTransitionV1 to control intro-transition #8389
#   ?experiment.messageChannels=treatment

#  **** [SX-21318] convert hair-loss treatment-drug-select container to a functional component #8391

# experiment.hairLossDrFirst=treatment    &hairLossFMF=on&hairLoss33=on  &experiment.googleShoppingSubHair=treatment
# &experiment.himsHairTopFinRecco=treatment
#    ?productId=APSnOWod
#  **** [SX-19876] hims hair enable 6mo shipping cadence for topical finasteride #8300
#  *** [SX-18274] [ED] edOnboardingNewCopy experiment #7572 -- ?experiment.edOnboardingNewCopy=treatment

# **** [SX-19947] hims hair oral finasteride attestations for patients with history of sexual dysfunction or mental health condition #8206

#  *** Hims Staging: https://7547.dev.forhims.com
#  *** [SX-18030] filter out spiro from hims hair #7431
#  *** [SX-18069] fix(web): disable brand 176 for hims hair loss flow #7446
# *** [SXM-18069] fix(web): support addition of hair loss brand 186 & 187 #7478
#    hairLossCheckoutFirst
#    hairLossDrFirst
   
    # **** [SX-17227] hims hair topical finasteride #7173 experiment.hairLossTopicalFinasMinox=treatment&experiment.himsHairTopFinRecco=treatment

# [SX-16222] Google Shopping v5 - Hair #6653     &experiment.googleShoppingSubHair=treatment  # &productId=XHKHRqc1

getURL()

# ?hairLossDrFirst=on&experiment.hairLossFinasMinox=treatment&experiment.hairLossPatientConversationShift=treatment&experiment.hairLossOtcCrossSellBlock=treatment&experiment.hairLossDiagnosticPhotosReorder=treatment

# MEDUSA TOF
# // /hair-loss/hair-loss-questionnaire-describe-step **** what best describes your hair?
# // selecting ***** overall hair loss/thinning   //hair-loss-questionnaire-describe-step-overallLoss
driver.find_element_by_xpath("//*[@for='questionnaire-describe-step-overallLoss']").click()
# // Transition step **** hair-loss-questionnaire-describe-step-overallLoss
time.sleep(1.5)
# ///consultation/hair-loss/hair-loss-questionnaire-care-step
# // what sort of results are you looking for? **** Selecting both regrowth and loss prevention
driver.find_element_by_xpath("//label[@for='questionnaire-describe-step-regrowthAndPrevention']").click()
# //Transition Step *** we've got you early action is the best action
# // consultation/hair-loss/hair-loss-ugc-before-registration-step
# // **** the results speak for themselves Where you're going - There's nothing but great hair
# driver.find_element_by_xpath("//*[@data-testid='RadioQuestionNextBtn']").click()
time.sleep(2)


#  *********  FOR GOOGLE SHOPPING NEED to Comment below two TOF 

# Would you consider using FDA-approved prescription products?
# Maybe — I would have some questions
driver.find_element_by_xpath("//*[@for='treatment-routine-preference-question-MODIFIED_PRESCRIPTION']").click()
time.sleep(2)

# First, let's learn a bit about you
# hair-loss/hair-loss-treatment-faq-step
driver.find_element_by_xpath("//button[contains (text(), 'Continue')]").click()

# //Second Page - Enter DOB
# //Janus DOB		
# Second Page - Enter DOB
driver.find_element_by_id("dob").send_keys("01011990")

# // T&C PP
driver.find_element_by_xpath("//*[@data-testid='ConsultationConsent']").click()
		
# //Submit DOB
driver.find_element_by_xpath("//button[@data-testid='DateOfBirthFormSubmitButton']").click()

time.sleep(1.5)

# //Third Page - Register Page
username = ("ranjit+cronofy+0801+02") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
# brian+75confidence1warningAgewarningName@forhims.com
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys("asdf96&&PB")
# //Click Register CTA
driver.find_element_by_xpath("//*[@data-testid='ConsultationRegisterAccountButton']").click()


# Google Shopping V5
# hl_Utils.ShippingAddressPageCrossSell()
# hl_Utils.hairLossPhotoUpload()
# hl_Utils.paymentCC()

# //questionnaire-landing-step
driver.find_element_by_xpath("//*[@data-testid='ExplanationPageContinue']").click()

# MEDUSA INTAKE

# 1 of 16  What was your sex assigned at birth?
# For example, on your original birth certificate
intake2new = driver.find_element_by_xpath("//*[@for='Question-19939-a070f11a-b83c-4b20-94d0-d324ad6b617b']")
driver.execute_script("arguments[0].click()", intake2new)

# 2 of 16  What is your gender?
# We ask this question of all of our patients to ensure that we provide you with safe and effective care. We are inclusive of all people.
intake1new = driver.find_element_by_xpath("//*[@for='Question-21313-35bdc8d1-cf0d-41f5-86ad-1c17e6d5a5f6']")
driver.execute_script("arguments[0].click()", intake1new)	



# 1 of 15
# When did you first notice any signs of hair loss?
intake1newre = driver.find_element_by_xpath("//*[@for='Question-20833-ae852747-f338-4a5e-a417-a603dc4cfe03']")
driver.execute_script("arguments[0].click()", intake1newre)	


# 3 of 15
# Are you currently experiencing any of the following?
# Different patterns of symptoms can suggest different possible causes.
intake3newre = driver.find_element_by_xpath("//*[@for='Question-15974-6823fb48-68a1-4b1a-a88a-1c8bae7be1e8']")
driver.execute_script("arguments[0].click()", intake3newre)	
intake3newreButton = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake3newreButton)

# 4 of 15
# What treatments have you already tried?
# We want to know what has and hasn't worked in the past.
intake4newre = driver.find_element_by_xpath("//*[@for='Question-15980-2d3494dd-cf9d-4746-8ddf-5d9783862e39']")
driver.execute_script("arguments[0].click()", intake4newre)	
intake4newreButton = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake4newreButton)


# intake1newButton = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
# driver.execute_script("arguments[0].click()", intake1newButton)

# 2 of 16  What was your sex assigned at birth?
# For example, on your original birth certificate
intake2new = driver.find_element_by_xpath("//*[@for='Question-19939-a070f11a-b83c-4b20-94d0-d324ad6b617b']")
driver.execute_script("arguments[0].click()", intake2new)


# 8 of 15
# Do any of the following currently apply to you?
# Certain conditions can complicate diagnosis, increase risks, or change the recommended treatments so it critical we know everything going on with your health.
intake8newre = driver.find_element_by_xpath("//*[@for='Question-16008-462d69e7-d126-4b21-8e6f-1963f59586c3']")
driver.execute_script("arguments[0].click()", intake8newre)	
intake8newreButton = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake8newreButton)

# 9 of 15
# Do you experience any symptoms of sexual dysfunction?
intake9newre = driver.find_element_by_xpath("//*[@for='Question-15989-8924b702-43be-4c0f-882e-9f697b75b026']")
driver.execute_script("arguments[0].click()", intake9newre)	

# 10 of 15
# Do you have or have you had any medical conditions?
# Even if they are in the past certain conditions can complicate diagnosis, increase risks, or change the recommended treatments so it critical we know your full history.
intake10newre = driver.find_element_by_xpath("//*[@for='Question-20164-5d253d4e-1f57-436b-adfa-774fae40de2e']")
driver.execute_script("arguments[0].click()", intake10newre)

# 10 of 14
# Do you have or have you had any mental health conditions?

driver.find_element_by_xpath("//*[@for='Question-20678-409c8e0d-59e7-4c40-acff-f7bc21b3420c']").click()

# 8 of 14
# In the last two weeks, have you been troubled by any of the following?
intake8new = driver.find_element_by_xpath("//*[@for='Question-19698-fe364368-c53e-4863-91f1-81089ccf10a9']")
driver.execute_script("arguments[0].click()", intake8new)
driver.execute_script
intake8NewButton = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake8NewButton)

# 5 of 15
# Do other people in your family have hair loss?
# Hair loss can run in families.
# intake5newre = driver.find_element_by_xpath("//*[@for='Question-15986-085083e7-eb6d-4572-92c8-b19c7bb37847']")
# driver.execute_script("arguments[0].click()", intake5newre)	
									
# 			//Visit questionnaire 13/16
# //			Have you ever had any surgeries or hospitalizations?
# 			// Selecting No, never had surgery or been hospitalized
driver.find_element_by_xpath("//*[@for='Question-15995-106c9a7e-76b7-4e75-b75e-03045f8e3056']").click()
			
# 			//Visit questionnaire 14/16
# //				Do you currently take any medicines, herbals, or supplements?
# 			// Please include any medicines you finished recently, including topical medicines, and any injections, vitamins, herbal remedies, or any other products you use.
driver.find_element_by_xpath("//*[@for='Question-15997-73c8f214-1965-45c4-93b4-0edbedf70ce6']").click()
driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']").click()
			
# 			//Visit questionnaire 15/16
# //				Do you have any allergies or medication reactions?
# 			//Selecting No, dont have any allergies or medication reactions
driver.find_element_by_xpath("//*[@for='Question-15999-b0ab2baf-300c-41f6-9b72-fc96f2e56395']").click()
			

# intake16 = driver.find_element_by_xpath("//*[@for='Question-16345-d40324f9-cd5d-4ad9-92ac-993309dfdf0d']")
# driver.execute_script("arguments[0].click()", intake16)

# driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Radio-Continue']").click()
# driver.execute_script("arguments[0].click()", intake16Button)
time.sleep(2)

# Calling Hair Loss Diagnostic Photo ReOrder
def hairDiagnosticPhotoReorder():
    # Upload HairFront & HairBack
    # // UPlOAD Front Of Your Head

    time.sleep(2)
    UploadPhotoHeadFront = driver.find_element_by_xpath("//input[@type='file']")
    UploadPhotoHeadFront.send_keys("/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/forehead.png")

    # "../ranAutomation/Photos/forehead.png"
    driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']").click()

    # UploadPhotoHairBack
    time.sleep(4)
    UploadPhotoHairBack = driver.find_element_by_xpath("//input[@type='file']")
    UploadPhotoHairBack.send_keys("/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/backhead.png")

    # // photo-upload-hair-front Confirmation page
    driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']").click()

    time.sleep(2)

hairDiagnosticPhotoReorder()

# What type of prescription product would you prefer?
#  select Spray
driver.find_element_by_xpath("//*[@for='side-effects-questionnaire-SPRAY']").click()

# /consultation/hair-loss/treatment-routine-preference-step
# What matters more to you in a hair treatment regimen?
# driver.find_element_by_xpath("//*[@for='treatment-routine-preference-question-effectiveness']").click()

# consultation/hair-loss/treatment-routine-preference-step
# What best describes the way you try new things?
# driver.find_element_by_xpath("//*[@for='treatment-routine-preference-question-recommended']").click()

# consultation/hair-loss/treatment-drug-select-step -- ANIMATION
driver.find_element_by_xpath("//*[@data-testid='education-cta']").click()

# consultation/hair-loss/treatment-drug-select-step
# Routine for loss prevention, regrowth, and healthy hair

#  if selection CHK
# drugSelectButton = driver.find_element_by_xpath("//button[contains (text(), 'Starting at $60/mo')]").click()

# if selection finas + minox kit
# drugSelectButton = driver.find_element_by_xpath("//button[contains (text(), 'Starting at $32/mo')]")

# if selection TOPICAL finas + minox kit
drugSelectButton = driver.find_element_by_xpath("//button[contains (text(), 'Starting at $50/mo')]")

driver.execute_script("arguments[0].click()", drugSelectButton)

time.sleep(1.5)

# disclaimer /hair-loss/disclaimer
driver.find_element_by_xpath("//button[contains (text(), 'I understand, continue')]")

def hairLoss2WayMessage():
    # 2 WAY message
    driver.find_element_by_name("patientConversation").send_keys("test's order ed's stage new visit's 01-15-2021 ! plz give me the med doc! doc u r the awesome doc! plz plz help me doc, i really need the med!!")

    # // PatientConversationFormSubmitButton
    driver.find_element_by_xpath("//*[@data-testid='PatientConversationFormSubmitButton']").click()

hairLoss2WayMessage()

# //consultation/hair-loss/timeline-transition-step
driver.find_element_by_xpath("//*[@data-testid='TreatmentDrugSelectContinue']").click()

# consultation/hair-loss/shipment-frequency-step # Choose your shipping & billing frequency
# Commenting when selecting TOPICAL & Dr First
# driver.find_element_by_id("freq-select-0").click()

# //Visit Summary V2
hairLossSummaryPage()

#  Calling Shipping Address Method
ShippingAddressPageCrossSell()

def hairLossSelfieAndIDUpload():
    # //UPlOAD SELFIE
    UploadPhotoSELFIE = driver.find_element_by_xpath("//input[@type='file']")
    filePathSELFIE = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/UploadSELFIE.jpg"

    UploadPhotoSELFIE.send_keys(filePathSELFIE)

    # //photo-upload-2 Confirmation page for NO TREATMENT
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']")).click()
    edSelfieButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edSelfieButton)

    time.sleep(4)

    # //FACE RETAKE
    driver.find_element_by_xpath("//button[contains (text(), 'Retake Face Photo')]").click()
    time.sleep(4)

    # //TRY to Upload FACE AGAIN
    UploadPhotoSELFIERE = driver.find_element_by_xpath("//input[@type='file']")
    filePathSELFIERE = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/UploadSELFIE.jpg"

    UploadPhotoSELFIERE.send_keys(filePathSELFIERE)

    # //Confirmation for FACE RETAKE
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']")).click()
    edSelfieAgainButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edSelfieAgainButton)
    time.sleep(2)

    # //SELFIE Proceed Anyway
    driver.find_element_by_xpath("//button[contains (text(), 'Proceed Anyway')]").click()
    time.sleep(2)

    time.sleep(2)

    # //photo-upload-1		
    # //below photo upload code works only when input type is file

    UploadPhotoID = driver.find_element_by_xpath("//input[@type='file']")
    # driver.execute_script("arguments[0].click()", UploadPhotoID)

    filePathID = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/pencilimageforuploadID.png"
    UploadPhotoID.send_keys(filePathID)

    # //photo-upload-1 Confirmation page for NO TREATMENT
    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']").click()
    edIDButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edIDButton)

    time.sleep(2)
    # //ID RETAKE
    driver.find_element_by_xpath("//button[contains (text(), 'Retake ID Photo')]").click()
    time.sleep(2)

    # //TRY to Upload ID Aagain
    UploadPhotoIDRE = driver.find_element_by_xpath("//input[@type='file']")
    filePathIDRE = "/Users/rchaudhary/projects/pythonProjects/ranAutomation/Photos/pencilimageforuploadID.png"

    UploadPhotoIDRE.send_keys(filePathIDRE)

    # // driver.find_element_by_xpath("//*[@data-testid='Camera-Confirm']")).click()
    edIDAgainButton = driver.find_element_by_xpath("//button[@data-testid='Camera-Confirm']")
    driver.execute_script("arguments[0].click()", edIDAgainButton)
    time.sleep(2)

    # //ID Proceed Anyway
    driver.find_element_by_xpath("//button[contains (text(), 'Proceed Anyway')]").click()
    time.sleep(2)

hairLossSelfieAndIDUpload()

# //Visit Summary V2
def hairLossSummaryPage():
    driver.find_element_by_xpath("//h1[contains (text(), 'Your visit summary')]").is_displayed()

    driver.find_element_by_xpath("//p[contains (text(), 'Almost done! Here’s an overview of your order.')]").is_displayed()

    # driver.find_element_by_xpath("//*[@data-testid='VisitSummary-Continue']").click()
    hlSummaryButton = driver.find_element_by_xpath("//*[@data-testid='VisitSummary-Continue']")
    driver.execute_script("arguments[0].click()", hlSummaryButton)

def ShippingAddressPageCrossSell():
    
    driver.find_element_by_id("firstName").send_keys(FirstName)
    driver.find_element_by_id("lastName").send_keys(LastName)
    driver.find_element_by_id("line1").send_keys(AddressLine1)
    driver.find_element_by_id("line2").send_keys(AddressLine2)
    driver.find_element_by_id("city").send_keys(City)
    # //Selecting Dropdawn State
    dropState = Select (driver.find_element_by_name("state"))
    dropState.select_by_visible_text("Delaware")
    # dropState.select_by_visible_text("California")
    # dropState.select_by_visible_text("Texas")
    # dropState.select_by_visible_text(" North Dakota")

    
    
    driver.find_element_by_id("zip").send_keys(Zip)
    driver.find_element_by_id("phone").send_keys(Phonenumber)
    driver.find_element_by_xpath("//button[@data-testid='ConsultationSaveAddressButton']").click()

    # //Shippo suggested

    # for DE
    driver.find_element_by_xpath("//*[@data-testid='address-choice-original']").click()

    #  for CA 
    # driver.find_element_by_xpath("//*[@data-testid='address-choice-suggested']").click()
    
    driver.find_element_by_xpath("//*[@data-testid='ConsultationShippingSelectAddressButton']").click()


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