from functools import total_ordering


class Animal:
    """Класс животного"""
    def __init__(self, species: str, food_per_day: float):
        self.species = species
        self.food_per_day = food_per_day

class ZooInventory:
    """
    ЗАДАЧА: Учет животных и их пропитания.
    1. calculate_monthly_food(): возвращает суммарное количество еды
       для всех животных в списке self.animals на 30 дней.
    2. count_species(species): возвращает количество животных конкретного вида.
    """
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def calculate_monthly_food(self):
        # ТВОЙ КОД: сумма (food_per_day каждого животного) * 30
        sum_food_per_day = 0
        for animal in self.animals:
            sum_food_per_day += animal.food_per_day
        return sum_food_per_day*30

    def count_species(self, species: str):
        # ТВОЙ КОД: подсчет количества объектов с такой породой
        total = 0
        for animal in self.animals:
            if species == animal.species:
                total += 1
        return total



