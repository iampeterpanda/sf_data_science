import requests    
import random


if __name__ == '__main__':
    while True:
        # выполняем POST-запрос на сервер по эндпоинту add с параметром json
        # lng = float(input('Введите долготу: '))
        # lat = float(input('Введите широту: '))
        # sqft = float(input('Введите sqft: '))
        # year_build = int(input('Введите год постройки: '))
        # stories = int(input('Введите этаж дома: '))
        # beds = int(input('Введите количество комнат: '))
        # baths = int(input('Введите количество ванных комнат: '))
        # density = float(input('Введите плотность населения: '))
        # population = float(input('Введите количество жителей в населенном пункте: '))
        # mean_rating = float(input('Введите срединий рейтинг школ: '))
        # mean_distance = float(input('Средняя дистанция до школ: '))
        # condo = int(input('Совместное владение (да - 1, нет - 0): '))
        lng = random.randint(-123, -67)
        lat = random.randint(5, 48)
        sqft = random.randint(50, 10000)
        year_build = random.randint(1800, 2023)
        stories = random.randint(0, 50)
        beds = random.randint(0, 20)
        baths = random.randint(0, 20)
        population = random.randint(0, 150000)
        density = random.randint(1, 15000)
        mean_rating = round((random.randint(0, 10)+random.randint(0, 10)+random.randint(0, 10))/3, 2)
        mean_distance = round((random.randint(0, 45)+random.randint(0, 45)+random.randint(0, 45))/3, 2)
        condo = random.randint(0, 1)
        
        r = requests.post('http://localhost:5000/predict', json=[sqft, 
                                                                lng, 
                                                                density, 
                                                                lat, 
                                                                mean_rating, 
                                                                year_build, 
                                                                population, 
                                                                baths, 
                                                                condo, 
                                                                stories, 
                                                                mean_distance, 
                                                                beds])
        # выводим статус запроса
        print('Status code: {}'.format(r.status_code))
        # реализуем обработку результата
        if r.status_code == 200:
            # если запрос выполнен успешно (код обработки=200),
            # выводим результат на экран
            print('Prediction: {}'.format(r.json()['prediction']))
        else:
                # если запрос завершён с кодом, отличным от 200,
                # выводим содержимое ответа
                print(r.text)