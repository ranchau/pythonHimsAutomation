
import unittest, time
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from numpy import random

# System.setProperty("webdriver.chrome.driver", "/Users/rchaudhary/eclipse-workspace/chromedriver")
# driver = webdriver.Chrome()
# driver.get("https://www.forhims.com")
# assert "Python" in driver.title
# url = "https://www.forhers.com/consultation/anti-aging/?aaKit=off&productId=8A74yVMeFl4&experiment.googleShoppingSubAging=treatment&experiment.acneMinor=treatment&split.himsAgingPrepaid=on&experiment.displayUpgradeButtonAcne=treatment&experiment.himsAgingStreamlined=treatment&experiment.hersAcnePicasso=control&experiment.hersAcnePicassoTOF=treatment&experiment.hersAcnePicassoRoutine=control&experiment.hersAcnePicassoPhotos=control&experiment.hersAcnePicassoConfirm=treatment&experiment.hersAcnePicasso2Way=treatment&experiment.himsAgingDuo=treatment&experiment.hersAcneTwentyOff=control&experiment.hersAcneOTCBundle=treatment&experiment.hersAcneStreamlined=treatment"
# url = "https://www.forhers.com/consultation/anti-aging/"

url = "https://8719-prod.dev.forhims.com/consultation/anti-aging/?experiment.intakeV2AntiAging=treatment"

# url = "https://6499.dev.forhers.com/consultation/primary-care?free-visit=active"
#  ******* https://8358.dev.forhers.com/?experiment.intakeV2AntiAging=treatment

#  https://github.com/Clubroom/hers/pull/8719


# &experiment.himsAgingDuo=treatment
# &experiment.himsAgingFreeOTC=treatment   utm_varaint=FreeOTC himsAgingDuo
# ?experiment.hersAcnePicasso=treatment&experiment.hersAcneStreamlined=treatment&experiment.hersAcneTry19=treatment
#  cadence=kit2&coupon=active&experiment.hersAcneStreamlined=treatment
# https://www.forhers.com/consultation/acne
# [SX-14969] hers acne 20% off discount #6295 -- experiment.hersAcneTwentyOff=treatment
# https://github.com/Clubroom/hers/pull/6391
# [SX-12425] age and name confirmation steps #5898 -- confirmAgeName

driver = webdriver.Chrome("/Users/rchaudhary/eclipse-workspace/chromedriver")
driver.maximize_window()
driver.implicitly_wait(20)
# driver.get("https://www.forhers.com/acne/?split.hersAcneTry29=on&split.edEducationAnimation=variant1&split.consultationEdShippingBeforePhotos=on&split.consultationEdUsagePage=off")
# https://www.forhers.com/consultation/acne/?experiment.enableSchedulingForFlows=treatment&split.hersAcneBlockPrepaidCards=off


def getURL():
	    driver.get(url)

		# ****** PR with the updated copy for the 1mo AA cream: https://github.com/Clubroom/hers/pull/7020

        #   *** 1mo anti-aging cream: 
    # https://6755-prod.dev.forhims.com/consultation/google-shopping/anti-aging?productId=gEfF0YNq&experiment.googleShoppingSubAging=treatment
    #    *** 2mo anti-aging duo: 
    # https://6755-prod.dev.forhims.com/consultation/google-shopping/anti-aging?productId=8A74yVMeFl4&experiment.googleShoppingSubAging=treatment
		

# 		"skin_first_month_promo";
# "skin_first_month_try_for_29";
#  "skin_first_month_try_for_19";
#  "skin_community_promo";
#  "freetrial2020",
#  "vipx89",

getURL()
# [SX-10948] skin renewals on submit fixed #5492

# [SX-10948] Anti-aging Renewals to new base #5412
#  https://5272-prod.dev.forhims.com?utm_variant=FreeOTC
#  [SX-10948][WIP] Skin renewals refresh #5136  skinRenewalRefresh
#  ?experiment.hersAcneStreamlined=treatment&experiment.hersAcnePicasso=treatment&experiment.himsAgingStreamlined=treatment&experiment.edDrugRecommendation=treatment

time.sleep(3)
# //First Page - Select State
selectState = Select(driver.find_element_by_name("state"))
selectState.select_by_visible_text("California")
# selectState.select_by_visible_text("Delaware")

# selectState.select_by_visible_text("New Jersey")
# selectState.select_by_visible_text("Arizona")
# selectState.select_by_visible_text("District of Columbia")

# //Select Checkbox
driver.find_element_by_xpath("//*[@data-testid='ConsultationConsent']").click()
		
# //Click CTA		
driver.find_element_by_xpath("//*[@data-testid='SelectStateFormSubmitButton']").click()
		
# Second Page - Enter DOB
driver.find_element_by_id("dob").send_keys("04252000")
		
# //Submit DOB
driver.find_element_by_xpath("//button[@data-testid='DateOfBirthFormSubmitButton']").click()

# //Third Page - Register Page
username = ("ranjit+cronofy+0701") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
# username = ("santa+vouched+0612+20") + "+" + str(math.floor(random.rand()*1000)) + ("one@forhims.com")
# 82confidence1warningAgewarningName

driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys("asdf96@@PB")
time.sleep(300)
# //Click Register CTA
driver.find_element_by_xpath("//*[@data-testid='ConsultationRegisterAccountButton']").click()



# //questionnaire-landing-step
driver.find_element_by_xpath("//*[@data-testid='ExplanationPageContinue']").click()


# JavascriptExecutor executor = (JavascriptExecutor)driver


# //(Visit questionnaire 1/19)
# //Do you ever have a problem getting or maintaining an erection that is rigid enough for sex?
# //Selecting I never have a problem getting or maintaining an erection for as long as I want
driver.find_element_by_xpath("//*[@for='Question-16201-06843032-2b05-4eca-b551-17df0483f5f6']").click()  

# //Six page (Visit questionnaire 2/19)
# //How did your erectile dysfunction begin? Select the one that best describes your ED.
# //Selecting I do not recall how it began
driver.find_element_by_xpath("//*[@for='Question-16208-ba2c27e1-8eb4-41bd-acdb-00fcfd520941']").click()


# //Seven page (Visit questionnaire 3/19)
# //Do you get erections...
# //Selecting Neither
# driver.find_element_by_xpath("//*[@for='Question-16589-177fe078-9570-4744-8026-04700433320f']").click()
# driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake3 = driver.find_element_by_xpath("//*[@for='Question-16589-177fe078-9570-4744-8026-04700433320f']")
driver.execute_script("arguments[0].click()", intake3)

intake3Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
# driver.execute_script("arguments[0].click()", intake3Button)
driver.execute_script("arguments[0].click()", intake3Button)


# //Eight page (Visit questionnaire 4/19)
# //Which of the following best describes your sex drive or desire to have sex (libido)?
# //Selecting Unchanged
driver.find_element_by_xpath("//*[@for='Question-16233-0c70798f-e8f8-4850-b8b7-3b68359b7336']").click()


# //Nine page (Visit questionnaire 5/19)
# //Have you ever been formally treated for ED or tried any medicines, vitamins, or supplements to treat it?
# //Selecting No
driver.find_element_by_xpath("//*[@for='Question-16198-33e79356-9a00-453c-8827-9b5046249594']").click()


# //Ten page (Visit questionnaire 6/19)
# //Have you had a physical exam with a healthcare provider in the past 3 years?
# //Selecting No
driver.find_element_by_xpath("//*[@for='Question-16597-1b9fa11e-c2fe-4619-bb5c-d77c2f70a578']").click()


# //Eleven page (Visit questionnaire 7/19)
# //Have you had your blood pressure measured in the past 6 months?
# //Selecting Continue, I know my blood pressure
driver.find_element_by_xpath("//*[@for='Question-16281-a040992e-63eb-41c8-92f9-eb65febe7a9e']").click()


# //Twelve page (Visit questionnaire 8/19)
# //What was your blood pressure (BP) at your last reading measured within the last 6 months?
# //Note:   BP is read as 2 numbers - the top number is always higher than the bottom number. Example: "115/72" 115 (systolic) 72 (diastolic)	

# // now the BP question is in text area
driver.find_element_by_id("systolic").send_keys("122")

driver.find_element_by_id("diastolic").send_keys("82")
# driver.find_element_by_xpath("//*[@data-testid='QuestionCard-BloodPressure-Continue']").click()
intakeBPButton = driver.find_element_by_xpath("//*[@data-testid='QuestionCard-BloodPressure-Continue']")
driver.execute_script("arguments[0].click()", intakeBPButton)



# //Thirteen page (Visit questionnaire 9/20)
# //Do you take any medications, vitamins, or supplements regularly?
# //Selecting No
driver.find_element_by_xpath("//*[@for='Question-16269-72551763-a820-439e-8692-037e19d1be90']").click()


# //Fourteen page (Visit questionnaire 10/20)
# //Do you take any of the following medicines? Select all that apply.
# //Selecting None Apply
# driver.find_element_by_xpath("//*[@for='Question-16267-7678494c-aefe-4c0c-8711-27196d4435a8']").click()
# driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake10 = driver.find_element_by_xpath("//*[@for='Question-16267-7678494c-aefe-4c0c-8711-27196d4435a8']")
driver.execute_script("arguments[0].click()", intake10)

intake10Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake10Button)


# //Fifteen page (Visit questionnaire 11/20)
# //Do you have any allergies?
# //Selecting No
driver.find_element_by_xpath("//*[@for='Question-16271-a581d6be-b65b-467c-ae8c-83bea090b294']").click()


# //Sixteen page (Visit questionnaire 12/20)
# //Do you have any medical conditions or history of prior surgeries?
# //Selecting No
# driver.find_element_by_xpath("//*[@for='Question-16599-e55dde5d-2a3f-4dc5-9399-f36b8bba233e']").click()


# //Seventeen page (Visit questionnaire 13/20)
# //Do any of the following cardiovascular risk factors apply to you?
# //Selecting None apply to me
# driver.find_element_by_xpath("//*[@for='Question-16226-7bc2729e-791d-4f49-8fa4-7cd24f854742']").click()
# driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake13 = driver.find_element_by_xpath("//*[@for='Question-16226-7bc2729e-791d-4f49-8fa4-7cd24f854742']")
driver.execute_script("arguments[0].click()", intake13)

intake13Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake13Button)

# //Eighteen page (Visit questionnaire 14/20)
# //Do you experience any of the following cardiovascular symptoms?
# //Selecting None of these apply to me
# // driver.find_element_by_xpath("//*[@for='Question-16278-b129f833-dd3d-4ec7-8d07-4fa83e01b6dd']").click()
# // driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake14 = driver.find_element_by_xpath("//*[@for='Question-16278-b129f833-dd3d-4ec7-8d07-4fa83e01b6dd']")
driver.execute_script("arguments[0].click()", intake14)

intake14Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake14Button)


# //Nineteen page (Visit questionnaire 15/20)
# //Do you have or have you previously been diagnosed with any of the following? Select all that apply.
# //Selecting None of these apply to me
# // driver.find_element_by_xpath("//*[@for='Question-16235-2f05ed5f-a6f5-4866-916d-7a755db3ace4']").click()
# // driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake15 = driver.find_element_by_xpath("//*[@for='Question-16235-2f05ed5f-a6f5-4866-916d-7a755db3ace4']")
driver.execute_script("arguments[0].click()", intake15)

intake15Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake15Button)


# //Twenty page (Visit questionnaire 16/20)
# //In the last 2 weeks, have you been troubled by any of the following?
# //Selecting No, I have not felt down, anxious, nervous, etc. in the last 2 weeks.
# // driver.find_element_by_xpath("//*[@for='Question-16603-584552c9-9119-4a0c-a771-7d854e6c60ba']").click()
# // driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake16 = driver.find_element_by_xpath("//*[@for='Question-16603-584552c9-9119-4a0c-a771-7d854e6c60ba']")
driver.execute_script("arguments[0].click()", intake16)

intake16Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake16Button)


# //TwentyOne page (Visit questionnaire 17/20)
# //Do you use any of the following recreational drugs?
# //Selecting No I don't use any of these
# // driver.find_element_by_xpath("//*[@for='Question-16273-c8d92f3a-cdf2-47bb-817c-6dfb539e7466']").click()
# // driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake17 = driver.find_element_by_xpath("//*[@for='Question-16273-c8d92f3a-cdf2-47bb-817c-6dfb539e7466']")
driver.execute_script("arguments[0].click()", intake17)

intake17Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake17Button)


# //TwentyTwo page (Visit questionnaire 18/20)
# //Do you have any of the following conditions? Select all that apply.
# //Selecting None of these apply to me
# // driver.find_element_by_xpath("//*[@for='Question-16207-922351b4-149b-4b6a-9868-2dd1b89804b4']").click()
# // driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake18 = driver.find_element_by_xpath("//*[@for='Question-16213-3402dda4-e718-4999-a902-faae6c684418']")
driver.execute_script("arguments[0].click()", intake18)

intake18Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake18Button)

# //TwentyThree page (Visit questionnaire 19/20)
# //Do you have, or have you ever had any of the following conditions?
# //Selecting None apply to me
# // driver.find_element_by_xpath("//*[@for='Question-16213-3402dda4-e718-4999-a902-faae6c684418']").click()
# // driver.find_element_by_xpath("//*[@data-testid='QuestionCard-Checkbox-Continue']").click()

intake19 = driver.find_element_by_xpath("//*[@for='Question-16207-922351b4-149b-4b6a-9868-2dd1b89804b4']")
driver.execute_script("arguments[0].click()", intake19)

intake19Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Checkbox-Continue']")
driver.execute_script("arguments[0].click()", intake19Button)

# 19 of 19
# Do you have any other medical conditions or history of prior surgeries?
intake20 = driver.find_element_by_xpath("//*[@for='Question-16599-e55dde5d-2a3f-4dc5-9399-f36b8bba233e']")
driver.execute_script("arguments[0].click()", intake20)

intake20Button = driver.find_element_by_xpath("//button[@data-testid='QuestionCard-Radio-Continue']")
driver.execute_script("arguments[0].click()", intake20Button)

# 2 WAY message
driver.find_element_by_name("patientConversation").send_keys("test order ed stage new visit 7-15-2020 ! plz give me the med doc! doc u r the awesome doc! plz plz help me doc, i really need the med!!")

# // PatientConversationFormSubmitButton
driver.find_element_by_xpath("//*[@data-testid='PatientConversationFormSubmitButton']").click()

# //Treatment Preference
driver.find_element_by_xpath("//*[@data-testid='TreatmentDrugSelectContinue']").click()

time.sleep(3)

# //ed-education-animation-step
# driver.find_element_by_xpath("//button[@data-testid='EducationAnimationContinue']").click()
edAnimationButton = driver.find_element_by_xpath("//button[@data-testid='EducationAnimationContinue']")
driver.execute_script("arguments[0].click()", edAnimationButton)

time.sleep(1.5)
# // Stage Use 6 times per month
driver.find_element_by_xpath("//img[@src='https://res.cloudinary.com/forhims/image/upload/q_auto,f_auto,fl_lossy/03-TreatmentPreference-Packets-6-2x']").click()
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
