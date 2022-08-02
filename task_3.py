from statistics import mean
import csv


def read_all():
    with open('films.csv') as f:
        films = csv.reader(f)
        for film_name, note, rating in films:
            print(f'Назва: {film_name} Опис: {note} Оцінка: {rating}')


def add_film():
    with open('films.csv', 'a') as f:
        writer = csv.writer(f)
        film_name = input('Введіть назву стрічки: ')
        note = input('Опис стрічки: ')
        try:
            rating = int(input('Рейтинг фільму від 1 до 5: '))
        except ValueError:
            print('Введіть ЧИСЛО від 1 до 5')

        if 1 <= rating <= 5:
            new_film = [film_name, note, rating]
            writer.writerow(new_film)
            print(f'{film_name} додано')
        else:
            print('ERROR: Рейтинг повинен бути від 1 до 5')


def remove_film(film_name):
    new_films_list = []
    with open('films.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != film_name:
                new_films_list.append(row)
            else:
                print(film_name, 'найден и будет удален')

    with open('films.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(new_films_list)


def from_high_to_low_rating():
    with open('films.csv') as f:
        films = csv.reader(f)
        films = sorted(films, key=lambda x: x[2], reverse=True)
        for film in films:
            print(' '.join(film))


def from_low_to_high_rating():
    with open('films.csv') as f:
        films = csv.reader(f)
        films = sorted(films, key=lambda x: x[2])
        for film in films:
            print(' '.join(film))


def top_rated():
    with open('films.csv') as f:
        films = csv.reader(f)
        for film in films:
            if film[2] == '5':  # rating 5 only, or we can do sort and then slice print(films[:5]) - top5 films
                print(' '.join(film))


def average_rating():
    rating_list = []
    with open('films.csv') as f:
        films = csv.reader(f)
        for film in films:
            rating_list.append(int(film[2]))
    average = mean(rating_list)  # or sum(rating_list) / len(rating_list)
    return average


read_all()
print('----')
#add_film()
#remove_film('Test2')
print(f'average rating among all films: {average_rating()}')
print('----')
from_high_to_low_rating()

