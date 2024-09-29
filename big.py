import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# คำสั่ง /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name  # ดึงชื่อผู้ใช้
    await update.message.reply_text(f"สวัสดี {user_name} /help เพื่อดูคำสั่งทั้งหมด")

# คำสั่ง /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"สวัสดี {user_name} ฟังก์ชั่นเรามีดังนี้:\n"
                                    f"/sms ยิงเบอร์\n"
                                    f"/checkip เช็ค IP")

# คำสั่ง /sms
async def sms_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # ดึงข้อมูลเบอร์และจำนวนจากคำสั่ง
        if len(context.args) != 2:
            await update.message.reply_text("กรุณาใช้คำสั่งในรูปแบบ /sms เบอร์10หลัก จำนวน")
            return

        phone_number = context.args[0]
        amount = context.args[1]

        # ตรวจสอบว่าเบอร์เป็นตัวเลข 10 หลัก
        if len(phone_number) != 10 or not phone_number.isdigit():
            await update.message.reply_text("กรุณากรอกเบอร์ที่ถูกต้อง (10 หลัก)")
            return

        # สร้าง URL ที่จะเรียกใช้งาน API
        api_url = f"https://api.cyber-safe.cloud/api/spamsms/ebea760a90/{phone_number}/1"
        print(f"API URL: {api_url}")  # พิมพ์ URL เพื่อตรวจสอบความถูกต้อง

        # เรียกใช้งาน API
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            # ตรวจสอบสถานะของ API
            if data.get("status") == "succeed":
                await update.message.reply_text(f"ยิงสำเร็จ ไปที่เบอร์ {phone_number} จำนวน {amount} 🚀🚀")
            else:
                await update.message.reply_text(f"ยิงไม่สำเร็จกรุณาทักหาแอดมิน")
        else:
            await update.message.reply_text(f"การเชื่อมต่อ API ล้มเหลว (HTTP {response.status_code})")

    except Exception as e:
        await update.message.reply_text(f"เกิดข้อผิดพลาด: {str(e)}")

# คำสั่ง /checkip
async def checkip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/checkip IP")

# ฟังก์ชั่นหลัก
if __name__ == '__main__':
    # ใส่ Token ที่คุณได้จาก BotFather
    application = ApplicationBuilder().token('7291952960:AAF0s9gBMN7pfmha7cRoBsVF1ekgwq_7wHY').build()

    # จัดการคำสั่งต่าง ๆ
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('sms', sms_command))
    application.add_handler(CommandHandler('checkip', checkip_command))

    # เริ่มรันบอท
    application.run_polling()

