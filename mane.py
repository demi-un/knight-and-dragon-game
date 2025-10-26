import random


class Person:
    def __init__(self, name, hp, damage, protection):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection

    def attack(self, target):
        damage = self.damage * (100 / (100 + target.protection))
        target.hp -= damage

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
    def __init__(self, name, hp, damage, protection, regeneration):
        super().__init__(name, hp, damage, protection)
        self.regeneration = regeneration

    #
    def attack(self, target):
        super().attack(target)
        self.hp += self.regeneration

    #
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
    print('>>> Fight: knight vs dragon <<<')
    print('Дракон будет защищать две части тела из трех своими крыльями. чтобы нанести максимальный урон, '
          'вам нужно предугадать часть тела, которую он не будет защищать')
    while person_1.is_alive and person_2.is_alive:
        print('Введите часть тела, в которую будете атаковать')
        selected_body_part = input("'h': Head, 'b': Body, 'l': Legs >>> ")
        unprotected_part = random.choice(['h', 'b', 'l'])
        if selected_body_part == unprotected_part:



# slime = Person('slime', 100, 10, 5)
#
#
# knight = Knight('knight1', 250, 20, 5, 1)
# knight.attack(slime)


# лес замок
