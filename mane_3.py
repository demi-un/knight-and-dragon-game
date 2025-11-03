import random
import time


class Person:
    def __init__(self, name, hp, damage, protection, selected_body_part='h', unprotected_part='h'):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection
        self.selected_body_part = selected_body_part
        self.unprotected_part = unprotected_part

    def got_damage(self, damage):
        real_damage = round(damage * (100 / (100 + self.protection)))
        if real_damage < 1:
            real_damage = 1
        self.hp -= real_damage
        return real_damage

    def attack(self, target):
        # Выбор незащищённой части тела противника
        target.unprotected_part = random.choice(['h', 'b', 'l'])

        # Проверка попадания в незащищённое место
        if self.selected_body_part == target.unprotected_part:
            damage = self.damage * 1.25  # крит
        else:
            damage = self.damage * 0.75  # противник защитился

        damage = target.got_damage(damage)

        print(f'{self.name} атакует {target.name} с уроном {self.damage}')
        print(f"урон с учётом защиты и крита: {damage}")
        if target.is_alive():
            print(f'{target.name} HP: {target.hp}\n')
        else:
            print(f'{target.name} погиб\n')

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f'{self.name} | HP: {self.hp}, Урон: {self.damage}, Защита: {self.protection}'


class Knight(Person):
    def __init__(self, name, hp, damage, protection, regeneration, selected_body_part='h', unprotected_part='h'):
        super().__init__(name, hp, damage, protection, selected_body_part, unprotected_part)
        self.regeneration = regeneration

    def attack(self, target):
        target.unprotected_part = random.choice(['h', 'b', 'l'])

        if self.selected_body_part == target.unprotected_part:
            damage = self.damage * 1.25
        else:
            damage = self.damage * 0.75

        damage = target.got_damage(damage)

        print(f'{self.name} атакует {target.name} с уроном {self.damage}')
        print(f"урон с учётом защиты и крита: {damage}")

        # 30% шанс восстановить здоровье
        if self.is_alive() and random.random() <= 0.3:
            self.hp += self.regeneration
            print(f'{self.name} восстановил {self.regeneration} HP')

        if target.is_alive():
            print(f'{target.name} HP: {target.hp}\n')
        else:
            print(f'{target.name} погиб\n')

    def __str__(self):
        return f'{self.name} | HP: {self.hp}, Урон: {self.damage}, Защита: {self.protection}, Регенерация: {self.regeneration}'


class Dragon(Person):
    def __init__(self, name, hp, damage, protection, fire_damage):
        super().__init__(name, hp, damage, protection)
        self.fire_damage = fire_damage

    def attack(self, target):
        damage = self.damage

        # 30% шанс добавить огненный урон
        if random.random() <= 0.3:
            damage += self.fire_damage
            print('Дракон поджигает противника!')

        target.unprotected_part = random.choice(['h', 'b', 'l'])

        if self.selected_body_part == target.unprotected_part:
            damage *= 1.25
        else:
            damage *= 0.75

        damage = target.got_damage(damage)

        print(f'{self.name} атакует {target.name} с уроном {self.damage}')
        print(f"урон с учётом защиты и крита: {damage}")
        if target.is_alive():
            print(f'{target.name} HP: {target.hp}\n')
        else:
            print(f'{target.name} погиб\n')

    def __str__(self):
        return f'{self.name} | HP: {self.hp}, Урон: {self.damage}, Защита: {self.protection}, Огненный урон: {self.fire_damage}'


def fight(person_1, person_2):
    print(f'>>> Бой: {person_1.name} vs {person_2.name} <<<')
    print('-' * 40)
    print(person_1)
    print(person_2)
    print('-' * 40)
    print('Дракон будет защищать 2 части тела из 3')

    while person_1.is_alive() and person_2.is_alive():
        print('\nВыберите часть тела, в которую будете АТАКОВАТЬ:')
        selected_body_part = input("'h': Голова, 'b': Тело, 'l': Ноги >>> ").strip().lower()

        if selected_body_part not in ['h', 'b', 'l']:
            print('Неверный ввод')
            continue

        person_1.selected_body_part = selected_body_part
        person_1.attack(person_2)

        if not person_2.is_alive():
            print(f'\n{person_2.name} пал в бою! Победил {person_1.name}!')
            break

        time.sleep(1)

        print(f'{person_2.name} готовит атаку...')
        print('Выберите часть тела, которую НЕ будете защищать:')
        unprotected_part = input("'h': Голова, 'b': Тело, 'l': Ноги >>> ").strip().lower()

        if unprotected_part not in ['h', 'b', 'l']:
            print('Неверный ввод')
            continue

        person_1.unprotected_part = unprotected_part
        person_2.selected_body_part = random.choice(['h', 'b', 'l'])
        print(f'{person_2.name} атакует в {person_2.selected_body_part}')
        person_2.attack(person_1)

        if not person_1.is_alive():
            print(f'\n{person_1.name} пал в бою! Победил {person_2.name}!')
            break

        print('-' * 40)
        print(person_1)
        print(person_2)
        print('-' * 40)


dragon = Dragon('Дракон', 120, 15, 3, 20)
knight = Knight('Рыцарь', 80, 18, 4, 10)

fight(knight, dragon)

Betty_Botter_bought_some_butter___Betty_Botter_bought_some_better_butter = random.randint(1, 2)
if knight.is_alive():
    print('Рыцарь защитил королевство')
else:
    if Betty_Botter_bought_some_butter___Betty_Botter_bought_some_better_butter == 1:
        print('Дракон сжег королевство')
    else:
        print('Дракон пощадил жителей королевства и улетел')