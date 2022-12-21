class SuperHero:
    people = 'people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name=name
        self.health_points=health_points
        self.nickname=nickname
        self.superpower=superpower
        self.catchphrase=catchphrase
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


