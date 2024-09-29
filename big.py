import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command
async def start(update: Update, context) -> None:
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f"สวัสดี {user_first_name} /help เพื่อดูคำสั่งทั้งหมด")

# Help command
async def help_command(update: Update, context) -> None:
    user_first_name = update.message.from_user.first_name
    help_message = (
        f"สวัสดี {user_first_name} ฟังก์ชั่นเรามีดังนี้:\n"
        "/qr สร้างคิวอาร์โค้ด\n"
        "/check ตรวจสอบที่อยู่จาก IP (ไม่แน่นอน 100%)\n"
        "/ngl สแปม NGL\n"
        "ADMIN @BIG554"
    )
    await update.message.reply_text(help_message)

# QR Code generation command
async def qr_command(update: Update, context) -> None:
    if context.args:
        qr_text = " ".join(context.args)
    else:
        await update.message.reply_text("กรุณาระบุข้อความสำหรับสร้างคิวอาร์โค้ด เช่น /qr ข้อความของคุณ")
        return

    api_url = f"https://api.hamx.xyz/qrcode.php?qrcode={qr_text}"
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            qr_image_path = 'qr_code.png'
            with open(qr_image_path, 'wb') as f:
                f.write(response.content)

            await update.message.reply_photo(photo=open(qr_image_path, 'rb'))
            os.remove(qr_image_path)  # Remove the file after sending
        else:
            await update.message.reply_text("ไม่สามารถสร้างคิวอาร์โค้ดได้ในขณะนี้ กรุณาลองใหม่อีกครั้ง")
    except requests.RequestException as e:
        logger.error(f"Error generating QR Code: {e}")
        await update.message.reply_text("เกิดข้อผิดพลาดในการสร้างคิวอาร์โค้ด กรุณาลองใหม่")

# IP Check command
async def check_command(update: Update, context) -> None:
    if not context.args:
        await update.message.reply_text("/check IP ที่จะเช็ค")
        return

    ip_address = context.args[0]
    await update.message.reply_text("รอสักครู่กำลังเช็ค IP...")

    api_url = f"https://ipinfo.io/{ip_address}/json?token=YOUR_TOKEN_HERE"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            ip_info = response.json()
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
    except requests.RequestException as e:
        logger.error(f"Error checking IP: {e}")
        await update.message.reply_text("เกิดข้อผิดพลาดในการเช็คข้อมูล IP กรุณาลองใหม่")

# NGL command for spamming messages
async def ngl_command(update: Update, context) -> None:
    if len(context.args) < 3:
        await update.message.reply_text("กรุณาระบุข้อมูลให้ครบ: /ngl ชื่อผู้ใช้ ข้อความ จำนวน")
        return

    username = context.args[0]
    message = context.args[1]
    try:
        count = int(context.args[2])
    except ValueError:
        await update.message.reply_text("กรุณาระบุจำนวนเป็นตัวเลข")
        return

    if count > 50:
        await update.message.reply_text("คุณไม่สามารถส่งข้อความเกิน 50 ครั้ง")
        return

    await update.message.reply_text(f"กำลังส่งข้อความไปที่ {username} จำนวน {count * 2} ครั้ง...")

    for i in range(count * 2):  # ส่งข้อความเป็น 2 เท่าของจำนวนที่ผู้ใช้ระบุ
        data = {
            "username": username,
            "question": message,
            "deviceId": "random-device-id",  # ปกติ NGL ใช้ deviceId, อาจจำเป็นต้องใส่ค่านี้
        }

        try:
            response = requests.post("https://ngl.link/api/submit", json=data)
            if response.status_code != 200:
                logger.error(f"Error sending NGL message: {response.status_code}")
                await update.message.reply_text(f"เกิดข้อผิดพลาดในการส่งข้อความครั้งที่ {i + 1}")
                break
        except requests.RequestException as e:
            logger.error(f"Error sending NGL message: {e}")
            await update.message.reply_text("เกิดข้อผิดพลาดในการเชื่อมต่อกับ NGL API")
            break

    await update.message.reply_text(f"การส่งข้อความไปยัง {username} เสร็จสิ้นแล้ว")

# Main function
def main() -> None:
    # Load token from environment variable
    token = os.getenv("7291952960:AAF0s9gBMN7pfmha7cRoBsVF1ekgwq_7wHY")
    if not token:
        logger.error("Bot token not found!")
        return

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("qr", qr_command))
    application.add_handler(CommandHandler("check", check_command))
    application.add_handler(CommandHandler("ngl", ngl_command))

    # Start bot polling
    application.run_polling()

if __name__ == '__main__':
    main()

