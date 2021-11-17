import telebot
import config

client = telebot.TeleBot(config.conf['token'])


@client.message_handler(content_types = ['text'])
def get_text(message):
  ball = 0 
  if message.text.lower() == 'привіт' or message.text.lower() == 'хай':
    client.send_message(message.chat.id, 'Привіт! Почнемо роботу?')
  elif message.text.lower() == 'що ти можеш?':
    client.send_message(message.chat.id, 'Я можу: відповідати на запитання ')
  elif message.text.lower() == 'як тебе звати?':
    client.send_message(message.chat.id, 'Мене звати testpyVbot')
  elif message.text.lower() == 'розпочнемо тест':
     client.send_message(message.chat.id, 'добре')
     client.send_message(message.chat.id, 'Старт тесту (напишіть т1 і подальші цифри для показу запитань)')
  elif message.text.lower() == 'т1':
    client.send_message(message.chat.id, '1. У громадському транспорті почалась суперечка. Ваша реакція?')
    client.send_message(message.chat.id, '1) не приймаю участі;')
    client.send_message(message.chat.id, '2) коротко висловлююся на захист сторони, яку вважаю правою;')
    client.send_message(message.chat.id, '3) активно втручаюся.')
    client.send_message(message.chat.id, 'Що ви виберите?:  ')
    if message.text.lower() == '1':
      ball = ball + 4
      client.send_message(message.chat.id, ball)
    elif message.text.lower() == '2':
      ball = ball + 2
      client.send_message(message.chat.id, ball)
    elif message.text.lower() == '3':
      ball = ball + 0
      client.send_message(message.chat.id, ball)
    #else: 
        #client.send_message(message.chat.id, 'EROR')
 
    

    
  if message.text.lower() == 'т2':
    client.send_message(message.chat.id, '2. Чи виступаєте на зборах із критикою?')
    client.send_message(message.chat.id, '1)  ні;')
    client.send_message(message.chat.id, '2) тільки якщо маю для цього вагомі підстави;')
    client.send_message(message.chat.id, '3) критикую з будь-якого приводу.')
    client.send_message(message.chat.id, 'Що ви виберете?:  ')
    if message.text.lower() == '1':
      ball = ball + 4
      client.send_message(message.chat.id, ball) 
    elif message.text.lower() == '2':
      ball = ball + 2
      client.send_message(message.chat.id, ball)
    elif message.text.lower() == '3':
      ball = ball + 0
      client.send_message(message.chat.id, ball)
    #else:
      #іclient.send_message(message.chat.id, 'EROR')





client.polling(non_stop = True, interval = 0)
