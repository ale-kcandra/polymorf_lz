import data_processor as dp  # подключаем наш файл с классом 

def main():  # создаем главную функцию
    processor = dp.DataProcessor('var2.csv') # создаем объект класса из файла data_processor
    processor.split_and_save() # вызываем метод для разделения и сохранения

if __name__ == "__main__":  # проверяем, что файл запущен 
    main()  # запускаем главную функцию