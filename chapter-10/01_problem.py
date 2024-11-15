class Programmers:
    company = 'Microsoft'
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position;

abu_bokor = Programmers('Abu Bokor', 18000, 'Frontend engineer');

print(abu_bokor.company, abu_bokor.name, abu_bokor.position, abu_bokor.salary)