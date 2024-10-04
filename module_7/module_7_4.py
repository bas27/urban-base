class Team:

    def __init__(self, team_name, team_num):
        self.team_name = team_name
        self.team_num = team_num
        self.__str__()

    def __str__(self):
        print("В команде %s участников: %s !" % (self.team_name, self.team_num))


class Makes:

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.__str__()

    def __str__(self):
        print("Итого сегодня в командах участников: %d и %d!" % (self.team1.team_num, self.team2.team_num))


# Использование %:
t1 = Team("Студенты", 1)
t2 = Team("Менеджеры", 2)

m1 = Makes(t1, t2)

# Далее вручную
team_name1 = "Мастера кода"
team_name2 = "Волшебники данных"
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование format():
print("Команда {} решила задач: {} !".format(team_name2, score_2))
print("{} решили задачи за {} с !".format(team_name2, team2_time))

# Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: победа команды {team_name1}!")
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем "
      f"по {(team1_time + team2_time) / tasks_total:.2f} секунды на задачу!.")
