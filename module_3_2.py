def send_email(message, recipient, *, sender="university.help@gmail.com"):
    check_mail = [".com", ".ru", ".net"]
    flag_sender = True
    flag_recipient = True
    for element in check_mail:
        if element in sender:
            flag_sender = False
        if element in recipient:
            flag_recipient = False

    if "@" not in sender or "@" not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif flag_sender or flag_recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient.lower() == sender.lower():
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

