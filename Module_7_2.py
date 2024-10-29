from idlelib.iomenu import encoding

def custom_write (file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for line_number, string in enumerate(strings):
        byte_position = file.tell()  # Получаем текущую позицию в байтах
        file.write(str(string) + '\n')  # Записываем строку с переводом строки
        strings_positions[f'{(line_number+1)}, {byte_position}'] = str(string)
    return strings_positions
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)