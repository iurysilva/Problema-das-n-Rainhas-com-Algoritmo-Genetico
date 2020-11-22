from objetos.cromossomo import Cromossomo
import numpy as np
import bitstring
import copy as cp

class Populacao:
    def __init__(self, numero_cromossomos, parametros):
        self.numero_cromossomos = numero_cromossomos
        self.parametros = parametros
        self.cromossomos = self.cria_cromossomos()

    def cria_cromossomos(self):
        cromossomos = np.array([])
        for cromossomo in range(0, self.numero_cromossomos):
            colunas_possiveis = np.array([0, 1, 2, 3, 4, 5, 6, 7])
            cromossomo = Cromossomo()
            cromossomo.bits = bitstring.BitArray(bin='')
            for linha_rainha in range(0, 8):
                coluna_rainha = colunas_possiveis[np.random.randint(0, len(colunas_possiveis))]
                bits = format(coluna_rainha, "#005b")
                cromossomo.bits.insert(bits, 3*linha_rainha)
                colunas_possiveis = np.delete(colunas_possiveis, np.where(colunas_possiveis == coluna_rainha))
                cromossomo.tabuleiro[linha_rainha, coluna_rainha] = 1
            cromossomo.calcular_fitness()
            cromossomos = np.append(cromossomos, cromossomo)
        return cromossomos

    def seleciona_cromossomos(self):
        nova_populacao = Populacao(self.numero_cromossomos, self.parametros)
        for i in range(nova_populacao.numero_cromossomos):
            chance_escolha = np.random.uniform(0, 1)
            cromossomo_1 = np.random.choice(self.cromossomos)
            cromossomo_2 = np.random.choice(self.cromossomos)
            while (cromossomo_2.bits == cromossomo_1.bits):
                cromossomo_2 = np.random.choice(self.cromossomos)
            if (cromossomo_1.fitness <= cromossomo_2.fitness):
                cromossomo_melhor = cromossomo_1
                cromossomo_pior = cromossomo_2
            else:
                cromossomo_melhor = cromossomo_2
                cromossomo_pior = cromossomo_1

            if(chance_escolha <= 0.80):
                nova_populacao.cromossomos[i] = cp.copy(cromossomo_melhor)
            else:
                nova_populacao.cromossomos[i] = cp.copy(cromossomo_pior)
        return nova_populacao
