import telegram


bot = telegram.Bot(token='7516140299:AAGlBSDDZ8AtRBU-jbLK4V0D9Paj9kKlg40')
bot.send_document(chat_id="@cosmicpicture1", document=open('pictures/nasa1.jpg', 'rb'))