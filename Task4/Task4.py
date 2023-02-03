# Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст)  своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

N = int(input("Введите количество друзей: "))
friends = []
new_friend = {}
for el in range(0, N):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    new_friend['name'] = name
    new_friend['age'] = age
    friends.append(new_friend)
    new_friend = {}
print('Список Ваших друзей: ', friends)

aver_age = 0
long_name = friends[0]['name']
for el in friends:
    aver_age = aver_age + el['age']
    if len(el['name']) > len(long_name):
        long_name = el['name']
aver_age = aver_age/N
print('Средний возраст друзей:', round(aver_age, 1))
print('Самое длинное имя друга:', long_name)