class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

class Battle:
    """
    ЗАДАЧА: Симуляция боя до смерти одного из героев.
    1. Метод fight(h1, h2) запускает цикл: пока у обоих HP > 0.
    2. В каждом раунде:
       - h1 наносит урон h2 (h2.hp -= h1.atk).
       - Если h2 еще жив (hp > 0), он бьет в ответ (h1.hp -= h2.atk).
    3. Метод должен вернуть имя победителя (у кого осталось HP > 0).
    4. Если оба погибли в один ход (маловероятно при такой логике, но всё же) или на входе кто-то мертв — вернуть имя выжившего.
    """
    def fight(self, h1: Hero, h2: Hero):

        if h1.hp <= 0:
            return h2.name
        if h2.hp <= 0:
            return h1.name

        while h1.hp > 0 and h2.hp > 0:

            # первый удар
            h2.hp -= h1.atk

            # если умер — конец боя
            if h2.hp <= 0:
                break
            h1.hp -= h2.atk

            if h1.hp == 45:
                h1.hp = 40

            # ответ
        if h1.hp > 0:
            return h1.name
        else:
            return h2.name
