"""
Наверняка многие из вас имеют опыт прохождения компьютерных игр. Возникало ли у вас в процессе игры желание изменить
что-нибудь и сделать так, чтобы персонажи или игровой мир больше соответствовали вашему представлению о хорошей игре?
Скорее всего да. В этой миссии (и в нескольких последующих, связанных с ней) вам предоставится возможность "посидеть в
кресле разработчика" и создать логику простой игры о сражениях. Давайте начнем с малого - сражения 1х1. В этой миссии
вам необходимо будет создать класс Warrior, у экземпляров которого будет 2 параметра - здоровье (равное 50) и атака
(равная 5), а также свойство is_alive, которое может быть True (если здоровье воина > 0) или False (в ином случае).

Кроме этого вам необходимо создать класс для второго типа солдат - Knight, который будет наследником Warrior,
но с увеличенной атакой - 7.
Также вам необходимо будет создать функцию fight(), которая будет проводить дуэли между 2
воинами и определять сильнейшего из них.
Бои происходят по следующему принципу: каждый ход первый воин наносит второму
урон в размере своей атаки, в следствие чего здоровье второго воина уменьшается, после чего аналогично поступает и
второй воин по отношению к первому.
Если в конце очередного хода у первого воина здоровье > 0, а у другого - нет,
выживший объявляется победителем и функция возвращает True, или False в ином случае.

Входные данные: воины.

Выходные данные: результат поединка (True или False).

Предусловие: 2 типа солдат
"""


class Warrior:

    health: int = 50
    attack: int = 5
    is_alive: bool = True

    def check_health(self):
        self.is_alive = self.health > 0
        return self.is_alive


class Knight(Warrior):
    attack: int = 7


def calc_fight(unit_1: Warrior, unit_2: Warrior):
    unit_2.health = unit_2.health - unit_1.attack


def fight(unit_1: Warrior, unit_2: Warrior):
    while all((unit_1.is_alive, unit_2.is_alive)):
        calc_fight(unit_1, unit_2)
        if unit_1.check_health() and not unit_2.check_health():
            return True
        calc_fight(unit_2, unit_1)
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
