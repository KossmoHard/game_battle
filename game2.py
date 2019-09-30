import random


class Player:
    """Класс Player отвечает за инициализацию игроков."""
    def __init__(self, name):   # Конструктор класса.
        self.name = name
        self.hp = 100
        self.skills = {
            'punch': (18, 25),
            'kick': (15, 35),
            'healing': (18, 25)
        }

    def choice_skill(self):
        """Возращает рандомный ключ из словаря."""
        name = random.choice(list(self.skills.keys()))
        return name

    def healing_skill(self, damage):
        """Восстанавливает здоровья игрока в диапазоне от 18 до 25."""
        self.hp = self.hp + damage
        if self.hp > 100:
            self.hp = 100

    def attack(self, target):
        """Принимает объект которому будет нанесен урон. Возращает информацию о нанесенном уроне."""
        skill_name = self.choice_skill()
        damage = random.randint(*self.skills.get(skill_name))   # Рандомный выбор значения по переданному ключу.

        if skill_name == 'healing':     # Если рандомное умение равно "healing" вызывается метод healing_skill.
            self.healing_skill(damage)

            return "Player {} used the '{}', healing {} hp".format(self.name, skill_name, damage)

        target.hp = target.hp - damage  # Нанесение урона объекту переданному в метод attack.
        if target.hp < 0:
            target.hp = 0

        return "Player {} used the '{}', damage {} hp".format(self.name, skill_name, damage)


class Computer(Player):
    """Класс Computer наследует класс Player с возможностью расширения выбора умения."""
    def choice_skill(self):
        if self.hp <= 35:
            name_dict = random.choices(list(self.skills.keys()), [0.1, 0.1, 0.8])   # Рандомный выбор ключа с заданной вероятностью.
            name = name_dict[0]

            return name

        name = random.choice(list(self.skills.keys()))
        return name


class Battle:
    """Класс Battle отвечает за основной игровой процесс."""
    def __init__(self, player, computer):   # В конструктор передаются объекты класса Player.
        self.obj_player = player
        self.obj_computer = computer

    def battle_start(self):
        """Выполняет цикл по условию до тех пор пока один из игроков не будет убит."""
        while self.obj_player.hp > 0 and self.obj_computer.hp > 0:
            random_choice = random.choice((self.obj_player, self.obj_computer))    # Рандомный выбор игрока.

            if random_choice == self.obj_player:
                print(random_choice.attack(self.obj_computer))    # Вызов метода attack объекта класса Player.
            else:
                print(random_choice.attack(self.obj_player))

            print("------------------")
            print("{} Health: {} hp".format(self.obj_player.name, self.obj_player.hp))
            print("{} Health: {} hp".format(self.obj_computer.name, self.obj_computer.hp))
            print("------------------")

        return "Game Over"

    def game_over(self):
        """Возращает информацию о победителе и проигравшем после окончания боя."""
        if self.obj_player.hp == 0:    # Условия проверки кол-ва здоровья одного из объектов
            return "{} - WIN! {} - LOSE! ".format(self.obj_computer.name, self.obj_player.name)
        else:
            return "{} - WIN! {} - LOSE! ".format(self.obj_player.name, self.obj_computer.name)


class Game:
    """Инициализация объектов."""
    input("Press Enter:")
    player = Player('Jon')
    computer = Computer('Alex')

    battle = Battle(player, computer)
    print(battle.battle_start())
    print(battle.game_over())


Game()
