
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import pyperclip
display = '''   ██████                                               ██████████                    ██           ██                                            ██  ██
  ██░░░░██                                             ░░░░░██░░░                    ░██          ░██       ██   ██                             ░░  ░██
 ██    ░░   ██████    █████   ██████  ██████   ██████      ░██      ██████   ██████  ░██  ██████  ░██      ░░██ ██     ██████ ███████   ██████   ██ ░██
░██        ░░░░░░██  ██░░░██ ██░░░░  ░░░░░░██ ░░██░░█      ░██     ██░░░░██ ██░░░░██ ░██ ██░░░░   ░██████   ░░███     ██░░░░ ░░██░░░██ ░░░░░░██ ░██ ░██
░██         ███████ ░███████░░█████   ███████  ░██ ░       ░██    ░██   ░██░██   ░██ ░██░░█████   ░██░░░██   ░██     ░░█████  ░██  ░██  ███████ ░██ ░██
░░██    ██ ██░░░░██ ░██░░░░  ░░░░░██ ██░░░░██  ░██         ░██    ░██   ░██░██   ░██ ░██ ░░░░░██  ░██  ░██   ██       ░░░░░██ ░██  ░██ ██░░░░██ ░██ ░██
 ░░██████ ░░████████░░██████ ██████ ░░████████░███         ░██    ░░██████ ░░██████  ███ ██████   ░██████   ██        ██████  ███  ░██░░████████░██ ███
  ░░░░░░   ░░░░░░░░  ░░░░░░ ░░░░░░   ░░░░░░░░ ░░░          ░░      ░░░░░░   ░░░░░░  ░░░ ░░░░░░    ░░░░░    ░░        ░░░░░░  ░░░   ░░  ░░░░░░░░ ░░ ░░░ 
'''
def menu(): # 打印菜单
    print('欢迎使用snail凯撒加解密工具箱！')
    print('请输入你需要进行的操作')
    print('1.encrypt(加密)')
    print('2.decrypt(解密)')


def chose():  # 选择加密类型
    mode = input('')
    if mode == 'encrypt':
        encrypt()
    elif mode == 'decrypt':
        decrypt()
    else:
        print('输入错误 请重新输入！')


def encrypt(): # 加密函数
    text = input('请输入你需要加密的明文')
    key = int(input('请输入偏移量(必须为整数)'))
    # mode = 'encrypt'
    translated = ''
    text = text.upper()

    for symbol in text:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num += key

            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            translated += LETTERS[num]
        else:
            translated = translated + symbol
    pyperclip.copy(translated)
    print(f"加密完成，密文为{translated}")

def decrypt(): # 解密函数
    text = input('请输入你需要加密的明文')
    key = int(input('请输入偏移量(必须为整数)'))
    translated = ''
    for key in range(len(LETTERS)):
        for symbol in text:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated += LETTERS[num]
            else:
                translated += symbol
    print(f'解密成功，偏移量为：{key}，解密后的明文为：{translated}')

if __name__ == '__main__':
    print('*'*80)
    print(display)
    while True:  # 一直循环执行
        menu()
        chose()

