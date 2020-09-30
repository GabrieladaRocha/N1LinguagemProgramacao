""" Darth Vader achou que seu exército de stormtrooper estava prendendo poucos
rebeldes, então lhe contratou para desenvolver um programa que leia um conjunto
indeterminado de número de reféns presos por mês. Ao final da listagem informe o
menor e o maior número de capturados, a média e o valor mais próximo a média (não
utilize funções prontas do python)."""


class Number:
    def read_numbers(self):
        counter = 1
        new_list = []
        option = 1
        while True:
            new_list.append(
                int(input("Digite o %d° conjunto de presos " % counter)))
            option = int(input("Deseja continuar? \n1 = Sim \n0 = Não \n"))
            counter += 1
            if(option == 0 or option != 1):
                break
        return new_list

    def find_bigger(self, new_list):
        bigger = new_list[0]
        for find_bigger in new_list:
            if find_bigger > bigger:
                bigger = find_bigger
        return bigger

    def find_little(self, new_list):
        smaller = new_list[0]
        for find_little in new_list:
            if find_little < smaller:
                smaller = find_little
        return smaller

    def sum_values(self, new_list):
        total_sum = 0.0
        for value in new_list:
            total_sum += value
        return total_sum

    def calculate_average(self, mySum, new_list):
        average_number = mySum / len(new_list)
        return average_number

    def find_approximate(self, average, new_list):
        approximate = {value: abs(value - average) for value in new_list}
        return min(approximate, key=approximate.get)


number = Number()
numbers_new_list = number.read_numbers()

bigger = number.find_bigger(numbers_new_list)
print("Maior conjunto de presos : %d" % bigger)

smaller = number.find_little(numbers_new_list)
print("Menor conjunto de presos: %d" % smaller)

mySum = number.sum_values(numbers_new_list)
print("Soma do conjunto de presos: %d" % mySum)

average = number.calculate_average(mySum, numbers_new_list)
print("Média do conjunto de presos: %.2f" % average)

approximate = number.find_approximate(average, numbers_new_list)
print("Valor do conjunto de presos aproximado da média : %.2f" % approximate)
