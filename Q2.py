"""Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter
um método aumenta_salario. Crie duas subclasses da classe funcionário,
programador e analista, implementando o método nas duas subclasses. Para
o programador some ao atributo salário mais 20 e ao analista some ao salário
mais 30, mostrando na tela o valor. Depois disso, crie uma classe de testes
instanciando os objetos programador e analista e chame o método
aumenta_salario de cada um."""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.increase = 0

    def increase_salary(self):
        self.salary = self.salary + self.increase

class Analyst(Employee):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age, salary)
        self.increase = 30

class Programmer(Employee):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, age, salary)
        self.increase = 20



p1 = Programmer("Arthur", 21, 1700)
print(p1.name)
print("R$: ",p1.salary)
p1.increase_salary()
print("Salário com aumento R$: ",p1.salary)

a1 = Analyst("Leandro", 30, 4500)
print("\n",a1.name)
print("R$: ",a1.salary)
a1.increase_salary()
print("Salário com aumento R$: ",a1.salary)
