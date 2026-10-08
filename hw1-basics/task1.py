"""
Задание 1. Расшифровка.

ИИ-ассистент выгрузил маркетинговый отчёт зашифрованным шифром Цезаря -
теперь его нужно расшифровать вручную.
"""


def decode_caesar_cipher(text: str, shift: int) -> str:
    """
    Расшифровать text, зашифрованный шифром Цезаря со сдвигом shift.

    Каждая латинская буква в исходном (незашифрованном) тексте была сдвинута
    вперёд по алфавиту на shift позиций (с переходом с 'z' на 'a' и с 'Z' на 'A').
    Регистр буквы должен сохраняться. Все остальные символы - цифры, пробелы,
    знаки препинания - в тексте не менялись при шифровании и должны остаться
    как есть при расшифровке.

    Пример: decode_caesar_cipher("Khoor!", 3) -> "Hello!"
    """
    result = ''
    alphabet_s = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_b = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(0, len(text)):
        if text[i] in alphabet_s:
            a = (alphabet_s.index(text[i]) - shift) % 26
            result += alphabet_s[a]
        elif text[i] in alphabet_b:
            a = (alphabet_b.index(text[i]) - shift) % 26
            result += alphabet_b[a]
        else:
            result += text[i]
    return result


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/task1_encoded.txt", encoding="utf-8") as f:
        encoded_text = f.read().strip()

    shift = 7
    print(decode_caesar_cipher(encoded_text, shift))
