import pandas as pd  # подключаем библиотеку для работы с таблицами

class data_processor:  # создаем класс
    def __init__(self, file_path):  # создаем объукт и читаем файл
        self.df = pd.read_csv(file_path)  # сохраняем таблицу в переменную df

    def __neg__(self):  # перегрузка унарного минуса 
        # посчитаем, сколько строк было, сколько стало после удаления дубликатов
        dup_count = self.df.duplicated().sum()  # сразу узнаем количество дубликатов
        self.df = self.df.drop_duplicates(keep='first')  # удаляем дубликаты
        print(f"Удалено дубликатов: {dup_count}")  # выводим результат
        return self  # возвращаем объект

    def split_and_save(self):  # метод для разделения
        -self  # ставим минус, чтобы сработал метод __neg__  т.е. удаление дубликатов

        # просто возьмем нужные столбцы и сохраним в два файла
        # сохраняем только списание средств
        spisanie = self.df[self.df['Тип операции'] == 'списание средств']
        spisanie.to_csv('spisanie.csv', index=False, encoding='utf-8-sig')
        print("Сохранен файл spisanie.csv")

        # сохраняем только получение средств
        poluchenie = self.df[self.df['Тип операции'] == 'получение средств']
        poluchenie.to_csv('poluchenie.csv', index=False, encoding='utf-8-sig')
        print("Сохранен файл poluchenie.csv")