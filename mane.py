import random


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
        # target.got_damage(self.damage)
        damage = self.damage

        target.unprotected_part = random.choice(['h', 'b', 'l'])

        if self.selected_body_part == target.unprotected_part:
            damage *= 1.25
        else:
            damage *= 0.75

        damage = target.got_damage()

        print(f'{self.name} attacks {target.name} with {self.damage} damage')
        print(f"The damage, taking into account the opponent's defense, was {damage}")
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
        super().attack(target)
        if self.is_alive():
            self.hp += self.regeneration
            print(f'{self.name} restored {self.regeneration} HP')

    def __str__(self):
        return f'{self.name} | HP: {self.hp}, damage: {self.damage}, protection: {self.protection}, regeneration: {self.regeneration}'


#
#
# class Dragon(Person):
#     def __init__(self, name, hp, damage, protection, fire_damage, burning_time):
#         super().__init__(name, hp, damage, protection)
#         self.fire_damage = fire_damage
#         self.burning_time = burning_time
#
#     def attack(self, target):
#         super().attack(target)
#         target.hp
#
#
# def fight(person_1, person_2):
#     while person_1.is_alive() and person_2.is_alive():
#         person_1.attack(person_2)
#         if person_2.is_alive():
#             person_2.attack(person_1)


def fight(person_1, person_2):
    print(f'>>> Fight: {person_1.name} vs {person_2.name} <<<')
    print(person_1)
    print(person_2)
    print(f'{person_2.name} будет защищать две части тела из трех. чтобы нанести максимальный урон, '
          'вам нужно предугадать часть тела, которую он не будет защищать')
    print('Введите часть тела, в которую будете атаковать')

    while person_1.is_alive and person_2.is_alive:
        selected_body_part = input("'h': Head, 'b': Body, 'l': Legs >>> ")

        print(f'{person_2.name} не защитил {person_2.unprotected_part}')
        person_1.selected_body_part = selected_body_part

        person_1.attack(person_2)

        print(person_1)
        print(person_2)

        print('>>>>>>>>>>>>>>------------<<<<<<<<<<<<<<<<<')

slime = Person('slime', 100, 10, 5)
knight = Knight('knight', 250, 20, 5, 1)

fight(knight, slime)


# лес замок
