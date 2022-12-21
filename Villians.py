class SuperHero:
    people = 'people'
    sir = 'sir'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def imia(self):
        return (f'{self.name}')

    def health(self):
        self.health_points *= 2

    def __str__(self):
        return f' nickname is {self.nickname}\n' \
               f' superpower is {self.superpower}\n' \
               f' HP {self.health_points}\n' \
               f' Catchphrase {self.catchphrase}'

    def __len__(self):
        return len(self.catchphrase)


a = SuperHero('Luffi', 'Mugiwara', 'stretching', 100, 'I Will Be The King Of The pirates')
c = a.catchphrase
a.imia()
a.health()
print(a)
print(len(c))


class SuperHero2(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, )
        self.fly = fly
        self.damage = damage

    def health(self):
        self.health_points **= 2

    def fly(self):
        self.fly=True
    def __str__(self):
        return f'Fly in The True_phrase'


superhero2 = SuperHero2('Zoro', 'King of Hell', 'Asura: Blades Drawn Dead Mans Game', 150,
                        'theres no point in just standing there and whining, it wont change a thing', )
superhero2.health()
print(superhero2.fly)


class SuperHero3(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, )
        self.fly = fly
        self.damage = damage
    def health(self):
        self.health_points **= 2

    def Ibicf(self):
        self.fly = True

    def true(self):
        print('fly in the True_phrase')


superhero3 = SuperHero3('Sanji', 'Black Foot', 'Fire Foots', 100, 'NAMI SAAAAAAAAAAAN, ROBIN TYAAAAAAAAAN')
superhero3.health()
print(superhero3)
print(f'Damage is: {superhero3.damage}')
superhero3.Ibicf()
print(f'Fly is: {superhero3.fly}')
superhero3.true()


class Villians(SuperHero3):
    Monster = 'Monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)


    def gen_x(self):
        pass

    def crit(self):
        print(f'Crit is: {self ** 2}')


villians = Villians('Kaido', 'Dragon', 'TRANSformation', 1000, 'I will kill you!!!')
print(villians)
villians.gen_x()
Villians.crit(superhero3.damage)
