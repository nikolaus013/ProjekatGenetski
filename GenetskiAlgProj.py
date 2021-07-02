import random
import numpy as np

solution_found = False
popN = 100  # n number of chromos per population
genesPerCh = 75
max_iterations = 1000
target = 1111.0
crossover_rate = 0.7
mutation_rate = 0.2

U = np.random.uniform


def generatePop():
    chromos, chromo = [], []
    for eachChromo in range(popN):
        chromo = []
        for bit in range(genesPerCh * 4):
            chromo.append(random.randint(0, 1))
        chromos.append(chromo)
    return chromos


def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')


def reverse_sublist(lst, start, end):
    lst[start:end] = lst[start:end][::-1]
    return lst


def mutiraj(chromosomes, mutation_rate):
    for row in chromosomes:
        if U(0, 1) < mutation_rate:

            v1 = np.random.randint(len(row))
            v2 = np.random.randint(len(row))
            while v1 == v2:
                v2 = np.random.randint(len(row))
            # row[v1], row[v2] = row[v2], row[v1]
            reverse_sublist(chromosomes, v1, v2)
    return chromosomes


def dekoduj_bin(hromozom):
    l = []
    d = hromozom.encode()
    for i in range(len(d)):
        for mask in [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]:
            if mask & d[i] > 0:
                l.append(1)
            else:
                l.append(0)
    return l


def trosak(hromozom, resenje):
    n = 0
    for i in range(len(hromozom)):
        if hromozom[i] != resenje[i]:
            n += 1
    return n


#    Input, integer M, the number of variables.
#
#    Input, real X(M), the argument of the function.
#
#    Output, real F, the value of the function at X.
#

def beale( x):
    f1 = 1.5 - x[0] * (1.0 - x[1])
    f2 = 2.25 - x[0] * (1.0 - x[1] ** 2)
    f3 = 2.625 - x[0] * (1.0 - x[1] ** 3)

    f = f1 ** 2 + f2 ** 2 + f3 ** 2

    return f


def bejl(position):
    x, y = position
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2




def genetski():
    npop_vel = 10


    dekod = dekoduj_bin(popN)




    def _random_n(N, chromosomes):

        shuffle = np.arange(len(chromosomes))
        np.random.shuffle(shuffle)
        return shuffle[:N]

    def jednoTackastoCrossover(ind1, ind2):
        size = min(len(ind1), len(ind2))
        cxpoint = random.randint(1, size - 1)
        ind1[cxpoint:], ind2[cxpoint:] = ind2[cxpoint:], ind1[cxpoint:]

        return ind1, ind2

    for k in range(5):
        print("Pokretanje Algortima")
        best = None
        best_f = None
        t = 0

        populacija = generatePop()
        print(populacija)
        while best_f != 0 and t < max_iterations:
            n_pop = populacija[:]

            while len(n_pop) < popN + npop_vel:
                h1 = _random_n(2, populacija)
                h2 = _random_n(2, populacija)
                h3, h4 = jednoTackastoCrossover(h1, h2)

                mutiraj(h3, mutation_rate)
                mutiraj(h4, mutation_rate)
                n_pop.append(h3)
                n_pop.append(h4)
#Sortirati po trosku populaciju i skrati na popN velicinu, ispis i racunanje proseka
#



########################################################

genetski()