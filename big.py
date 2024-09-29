import requests
from telegram import Update
from telegram.ext import Application, CommandHandler

# ฟังก์ชันที่จะแสดงผลเมื่อพิมพ์ /start
async def start(update: Update, context) -> None:
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f"สวัสดี {user_first_name} /help เพื่อดูคำสั่งทั้งหมด")

# ฟังก์ชันที่จะแสดงผลเมื่อพิมพ์ /help
async def help_command(update: Update, context) -> None:
    user_first_name = update.message.from_user.first_name
    help_message = (
        f"สวัสดี {user_first_name} ฟังก์ชั่นเรามีดังนี้:\n"
        "/qr สร้างคิวอาร์โค้ด\n"
        "/check ตรวจสอบที่อยู่จาก IP (ไม่แน่นอน 100%)\n"
        "ADMIN @BIG554"
    )
    await update.message.reply_text(help_message)

# ฟังก์ชันสำหรับการสร้าง QR Code
async def qr_command(update: Update, context) -> None:
    # รับข้อความที่ผู้ใช้ต้องการสร้าง QR Code
    if context.args:
        qr_text = " ".join(context.args)
    else:
        await update.message.reply_text("กรุณาระบุข้อความสำหรับสร้างคิวอาร์โค้ด เช่น /qr ข้อความของคุณ")
        return

    # เรียก API เพื่อสร้าง QR Code
    api_url = f"https://api.hamx.xyz/qrcode.php?qrcode={qr_text}"
    response = requests.get(api_url)

    if response.status_code == 200:
        # บันทึกภาพ QR Code ชั่วคราว
        qr_image_path = 'qr_code.png'
        with open(qr_image_path, 'wb') as f:
            f.write(response.content)

        # ส่งรูปภาพกลับให้ผู้ใช้
        await update.message.reply_photo(photo=open(qr_image_path, 'rb'))

    else:
        await update.message.reply_text("ไม่สามารถสร้างคิวอาร์โค้ดได้ในขณะนี้ กรุณาลองใหม่อีกครั้ง")

# ฟังก์ชันตรวจสอบ IP
async def check_command(update: Update, context) -> None:
    if not context.args:
        await update.message.reply_text("/check IP ที่จะเช็ค")
        return

    ip_address = context.args[0]
    await update.message.reply_text("รอสักครู่กำลังเช็ค IP...")

    # เรียก API เพื่อเช็ค IP
    api_url = f"https://ipinfo.io/{ip_address}/json?token=16dd0fbb0567d6"
    response = requests.get(api_url)

    if response.status_code == 200:
        ip_info = response.json()
        # ส่งข้อมูลที่ได้จาก API กลับให้ผู้ใช้
        location_info = (
            f"IP: {ip_info.get('ip')}\n"
            f"ประเทศ: {ip_info.get('country')}\n"
            f"เมือง: {ip_info.get('city')}\n"
            f"องค์กร: {ip_info.get('org')}\n"
            f"ตำแหน่ง: {ip_info.get('loc')}\n"
        )
        await update.message.reply_text(location_info)
    else:
        await update.message.reply_text("ไม่สามารถเช็คข้อมูลได้ในขณะนี้ กรุณาลองใหม่อีกครั้ง")

def main() -> None:
    # ใส่โทเค็นบอทของคุณที่ได้จาก @BotFather
    application = Application.builder().token("7291952960:AAF0s9gBMN7pfmha7cRoBsVF1ekgwq_7wHY").build()

    # กำหนด handler สำหรับคำสั่งต่างๆ
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("qr", qr_command))
    application.add_handler(CommandHandler("check", check_command))

    # เริ่มต้นบอท
    application.run_polling()

if __name__ == '__main__':
    main()
    
