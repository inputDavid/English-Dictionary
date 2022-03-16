import random
import pyttsx3  # Библиотека для преобразования текста в речь
from Dictionary_Adjectives import My_Dictionary_For_Adjectives
from Dictionary_Adverbs import My_Dictionary_For_Adverbs
from Dictionary_Animals import My_Dictionary_For_Animals
from Dictionary_City import My_Dictionary_For_City_Life
from Dictionary_Colors import My_Dictionary_For_Colors
from Dictionary_Drinks import My_Dictionary_For_Drinks
from Dictionary_Family import My_Dictionary_For_Family
from Dictionary_Food import My_Dictionary_For_Food
from Dictionary_Human import My_Dictionary_For_Human_Structure
from Dictionary_Job import My_Dictionary_For_Job
from Dictionary_Linking import My_Dictionary_For_Linking_Words
from Dictionary_Nature import My_Dictionary_For_Nature
from Dictionary_Nouns import My_Dictionary_For_Nouns
from Dictionary_Pronouns import My_Dictionary_For_Pronouns
from Dictionary_Science import My_Dictionary_For_Science
from Dictionary_Syntax import My_Dictionary_For_Syntax
from Dictionary_Time import My_Dictionary_For_Time
from Dictionary_Verbs import My_Dictionary_For_Verbs

All_Dictionaries = [
    [My_Dictionary_For_Adjectives, 'My_Dictionary_For_Adjectives'],
    [My_Dictionary_For_Adverbs, 'My_Dictionary_For_Adverbs'],
    [My_Dictionary_For_Animals, 'My_Dictionary_For_Animals'],
    [My_Dictionary_For_City_Life, 'My_Dictionary_For_City_Life'],
    [My_Dictionary_For_Colors, 'My_Dictionary_For_Colors'],
    [My_Dictionary_For_Drinks, 'My_Dictionary_For_Drinks'],
    [My_Dictionary_For_Family, 'My_Dictionary_For_Family'],
    [My_Dictionary_For_Food, 'My_Dictionary_For_Food'],
    [My_Dictionary_For_Human_Structure, 'My_Dictionary_For_Human_Structure'],
    [My_Dictionary_For_Job, 'My_Dictionary_For_Job'],
    [My_Dictionary_For_Linking_Words, 'My_Dictionary_For_Linking_Words'],
    [My_Dictionary_For_Nature, 'My_Dictionary_For_Nature'],
    [My_Dictionary_For_Nouns, 'My_Dictionary_For_Nouns'],
    [My_Dictionary_For_Pronouns, 'My_Dictionary_For_Pronouns'],
    [My_Dictionary_For_Science, 'My_Dictionary_For_Science'],
    [My_Dictionary_For_Syntax, 'My_Dictionary_For_Syntax'],
    [My_Dictionary_For_Time, 'My_Dictionary_For_Time'],
    [My_Dictionary_For_Verbs, 'My_Dictionary_For_Verbs']
]


# Функция №1 - Считает общее количество слов в базе
def all_words():
    count_words = 0
    for dictionary in All_Dictionaries:
        count_words += len(dictionary[0])
    return count_words


# Функция №2 - Выводит на экран общую информацию по словарному запасу
def show_my_vocabulary():
    print(f'Всего словарей: {len(All_Dictionaries)}')
    print(f'Средний размер словаря: {int(all_words() / len(All_Dictionaries))}')
    print(f'Всего слов: {all_words()}')


# Функция №3 - Вытаскивает одно рандомное слово из всех доступных слов
def take_random_word():
    # 1 - Вытаскиваем рандомный индекс для словаря
    random_index_of_dictionary = random.randrange(0, len(All_Dictionaries), 1)  # Последняя цифра не берётся
    # 2 - Вытаскиваем рандомный словарь по индексу
    random_dictionary = All_Dictionaries[random_index_of_dictionary]
    # 3 - Вытаскиваем слова списком из этого словаря
    words_of_random_dictionary = list(random_dictionary[0].items())
    # 4 - Вытаскиваем рандомное слово из этого списка в кортеже вида (eng, rus)
    random_word = random.choice(words_of_random_dictionary)
    # 5 - Делаем кортеж (eng, rus) результатом работы функции
    return random_word


# Функция №4 - Озвучивает переданный текст
# Более подробно о библиотеке pyttsx3 по ссылке ниже
# https://learn4kid-python.firebaseapp.com/python_data_structure/python_speech_synthesis
def computer_says(some_text):
    engine = pyttsx3.init()  # Инициализация движка
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('rate', 125)  # Скорость речи в %
    engine.setProperty('volume', 1)  # Громкость (от 0 до 1)
    engine.setProperty('voice', en_voice_id)  # Выбор голоса
    engine.say(some_text)  # Запись слова(фразы) в очередь
    engine.runAndWait()  # Очистка очереди и воспроизведение текста


# Функция №5 - Запуск тренировки слов на основе функций №1, №3 и №4
def lets_start_training():
    for i in range(0, all_words()):
        our_word = take_random_word()
        print(our_word[0])
        computer_says(our_word[0])
        our_desire = input('Хотите послушать повторно? Если да, то введите «1» ')
        while our_desire == '1':
            computer_says(our_word[0])
            our_desire = input('Хотите послушать повторно? Если да, то введите «1» ')
        else:
            print(our_word[1])


# Функция №6 - Проверяет содержится ли в базе переданное слово
def check_your_word(any_word):
    check_word = 0
    for i in All_Dictionaries:
        for j in list(i[0].items()):
            if j[0] == any_word or j[1] == any_word:
                print(f'Слово уже есть в словаре «{i[1]}»')
                check_word += 1
    if check_word == 0:
        print('Такого слова ещё нет')


# Функция №7 - Проверяет нет ли дублей в словарях
def check_duplicate_words():
    check_dictionaries = []
    for i in All_Dictionaries:
        for j in list(i[0].items()):
            if j[0] in check_dictionaries:
                print(f'Есть дубликат слова {j[0]}')
            else:
                check_dictionaries.append(j[0])
    if not check_dictionaries:
        print('Нет повторяющихся слов')


# show_my_vocabulary()
# lets_start_training()
# check_your_word('drink')
# check_duplicate_words()
