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
        damage = round(damage * (100 / (100 + self.protection)))

        if damage == 0:
            damage = 1

        self.hp -= damage

        return damage

    def attack(self, target):
        damage = self.damage

        target.unprotected_part = random.choice(['h', 'b', 'l'])

        if self.selected_body_part == target.unprotected_part:
            damage *= 1.25
        else:
            damage *= 0.75

        damage = target.got_damage(damage)

        print(f'{self.name} attacks {target.name} with {self.damage} damage')
        print(f"The damage, taking into account the opponent's defense and critical damage, was {damage}")
        if target.is_alive():
            print(f'{target.name} HP: {target.hp}')
        else:
            print(f'{target.name} died')

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f'{self.name} | HP: {self.hp}, damage: {self.damage}, protection: {self.protection}'


class Knight(Person):
    def __init__(self, name, hp, damage, protection, regeneration, selected_body_part='h', unprotected_part='h'):
        super().__init__(name, hp, damage, protection, selected_body_part, unprotected_part)
        self.regeneration = regeneration

    def attack(self, target):
        damage = self.damage

        target.unprotected_part = random.choice(['h', 'b', 'l'])

        if self.selected_body_part == target.unprotected_part:
            damage *= 1.25
        else:
            damage *= 0.75

        damage = target.got_damage(damage)

        print(f'{self.name} attacks {target.name} with {self.damage} damage')
        print(f"The damage, taking into account the opponent's defense and critical damage, was {damage}")

        if self.is_alive() and random.random() <= 0.3:
            self.hp += self.regeneration
            print(f'{self.name} restored {self.regeneration} HP')

        if target.is_alive():
            print(f'{target.name} HP: {target.hp}')
        else:
            print(f'{target.name} died')

    def __str__(self):
        return f'{self.name} | HP: {self.hp}, damage: {self.damage}, protection: {self.protection}, regeneration: {self.regeneration}'


class Dragon(Person):
    def __init__(self, name, hp, damage, protection, fire_damage):
        super().__init__(name, hp, damage, protection)
        self.fire_damage = fire_damage

    def attack(self, target):
        damage = self.damage

        if random.random() <= 0.3:
            damage += self.fire_damage
            'Дракон поджигает ваше тело'

        target.unprotected_part = random.choice(['h', 'b', 'l'])

        if self.selected_body_part == target.unprotected_part:
            damage *= 1.25
        else:
            damage *= 0.75

        damage = target.got_damage(damage)

        print(f'{self.name} attacks {target.name} with {self.damage} damage')
        print(f"The damage, taking into account the opponent's defense and critical damage, was {damage}")
        if target.is_alive():
            print(f'{target.name} HP: {target.hp}')
        else:
            print(f'{target.name} died')

    def __str__(self):
        return f'{self.name} | HP: {self.hp}, damage: {self.damage}, protection: {self.protection}, fire damage: {self.fire_damage}'


def fight(person_1, person_2):
    print(f'>>> Fight: {person_1.name} vs {person_2.name} <<<')
    print('-'*40)
    print(person_1)
    print(person_2)
    print('-'*40)
    print(f'{person_2.name} будет защищать две части тела из трех. чтобы нанести максимальный урон, '
          'вам нужно предугадать часть тела, которую он не будет защищать')

    while person_1.is_alive and person_2.is_alive:
        print('Введите часть тела, в которую будете АТАКОВАТЬ')
        selected_body_part = input("'h': Head, 'b': Body, 'l': Legs >>> ")

        print(f'{person_2.name} не защитил {person_2.unprotected_part}')
        person_1.selected_body_part = selected_body_part

        person_1.attack(person_2)

        time.sleep(1)
        print(f'{person_2.name} атакует {person_1.name}')
        print('Выберите часть тела которую НЕ будете ЗАЩИЩАТЬ')
        unprotected_part = input("'h': Head, 'b': Body, 'l': Legs >>> ")
        person_1.unprotected_part = unprotected_part

        person_2.selected_body_part = random.choice(['h', 'b', 'l'])

        print(f'{person_2.name} атакует {person_1.name} в часть тела {person_2.selected_body_part}')
        person_2.attack(person_1)

        print('-' * 40)
        print(person_1)
        print(person_2)
        print('-' * 40)

        print('>>>>>>>>>>>>>>------------<<<<<<<<<<<<<<<<<')

slime = Person('slime', 100, 10, 5)

dragon = Dragon('dragon', 400, 15, 3, 30)
knight = Knight('knight', 250, 20, 5, 35)

fight(knight, dragon)
