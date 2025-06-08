from cryptography.fernet import Fernet

# Генериране на ключ (при стартиране)
key = Fernet.generate_key()
f = Fernet(key)

print('🔐 Simple Encryptor')
print('Текущият ключ (само за тази сесия):')
print(key.decode())

while True:
    action = input('\n(e) Шифрирай | (d) Дешифрирай | (q) Изход: ').lower()

    if action == 'e':
        text = input('Въведи текст за шифриране: ')
        encrypted = f.encrypt(text.encode())
        print('🔒 Шифриран текст:', encrypted.decode())

    elif action == 'd':
        token = input('Въведи шифрирания текст: ')
        try:
            decrypted = f.decrypt(token.encode())
            print('🔓 Дешифриран текст:', decrypted.decode())
        except Exception as e:
            print('❌ Невалиден текст или ключ.')

    elif action == 'q':
        print('👋 Изход.')
        break

    else:
        print('⚠️ Невалидна команда.')
