class Tomato:
    # стадии созревания (статическое свойство)
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зелёный', 3: 'красный'}

    def __init__(self, index: int):
        # _index — номер томата (приватное)
        # _state — стадия созревания (приватное)
        self._index = index
        self._state = 0  # первая стадия

    def grow(self):
        # перевод томата на следующую стадию
        if self._state < max(Tomato.states.keys()):
            self._state += 1
        print(f"Томат {self._index} теперь {Tomato.states[self._state]}")

    def is_ripe(self):
        # проверка, что томат созрел
        return self._state == max(Tomato.states.keys())


class TomatoBush:
    def __init__(self, count: int):
        # список томатов
        self.tomatoes = [Tomato(i) for i in range(1, count + 1)]

    def grow_all(self):
        print("\nКуст растёт")
        for t in self.tomatoes:
            t.grow()

    def all_are_ripe(self):
        # проверка, что все томаты спелые
        return all(t.is_ripe() for t in self.tomatoes) if self.tomatoes else False

    def give_away_all(self):
        # сбор урожая
        self.tomatoes.clear()
        print("Урожай собран, куст пуст")


class Gardener:
    def __init__(self, name: str, plant: TomatoBush):
        # name — имя садовника (публичное)
        # _plant — куст (приватное)
        self.name = name
        self._plant = plant

    def work(self):
        print(f"\n{self.name} ухаживает за растением")
        self._plant.grow_all()
        print(f"{self.name} закончил уход")

    def harvest(self):
        print(f"\n{self.name} проверяет урожай")
        if not self._plant.tomatoes:
            print("На кусте нет томатов")
            return
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собрал урожай")
        else:
            print("Не все томаты созрели, собирать рано")

    @staticmethod
    def knowledge_base():
        print("""Справка по садоводству:
1. Томат проходит стадии: отсутствует -> цветение -> зелёный -> красный
2. Чтобы собрать урожай, нужно ухаживать за кустом до полной зрелости
3. После созревания плоды можно собрать""")


if __name__ == "__main__":
    Gardener.knowledge_base()

    bush = TomatoBush(3)
    gardener = Gardener("Влад", bush)

    gardener.work()
    gardener.harvest()

    gardener.work()
    gardener.harvest()

    gardener.work()
    gardener.harvest()