import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# ฟังก์ชันที่จะแสดงผลเมื่อพิมพ์ /start
def start(update: Update, context: CallbackContext) -> None:
    user_first_name = update.message.from_user.first_name
    update.message.reply_text(f"สวัสดี {user_first_name} /help เพื่อดูคำสั่งทั้งหมด")

# ฟังก์ชันที่จะแสดงผลเมื่อพิมพ์ /help
def help_command(update: Update, context: CallbackContext) -> None:
    user_first_name = update.message.from_user.first_name
    update.message.reply_text(f"สวัสดี {user_first_name} ฟังก์ชั่นเรามีดังนี้:\n /qr สร้างคิวอาร์โค้ด")

# ฟังก์ชันสำหรับการสร้าง QR Code
def qr_command(update: Update, context: CallbackContext) -> None:
    # รับข้อความที่ผู้ใช้ต้องการสร้าง QR Code
    if context.args:
        qr_text = " ".join(context.args)
    else:
        update.message.reply_text("กรุณาระบุข้อความสำหรับสร้างคิวอาร์โค้ด เช่น /qr ข้อความของคุณ")
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
        update.message.reply_photo(photo=open(qr_image_path, 'rb'))

    else:
        update.message.reply_text("ไม่สามารถสร้างคิวอาร์โค้ดได้ในขณะนี้ กรุณาลองใหม่อีกครั้ง")

def main() -> None:
    # ใส่โทเค็นบอทของคุณที่ได้จาก @BotFather
    updater = Updater("YOUR_TELEGRAM_BOT_API_TOKEN")

    # รับการอัปเดตจากบอท
    dispatcher = updater.dispatcher

    # กำหนด handler สำหรับคำสั่งต่างๆ
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("qr", qr_command))

    # เริ่มต้นบอท
    updater.start_polling()

    # ทำงานค้างไว้จนกว่าจะมีการหยุด
    updater.idle()

if __name__ == '__main__':
    main()
    
