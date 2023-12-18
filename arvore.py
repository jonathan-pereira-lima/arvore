# 2 VA
# HELDON JOSE OLIVEIRA ALBUQUERQUE
# aluno: JOSÉ JONATHAN PEREIRA LIMA
# •
# 100 pontos
# Data de entrega: 04 de out.
#1 - VOcês tetarem fazer o balancear.
#2 - Grava um video de no máximo 20 min explicando o balancear
    # - O - que é uma arvore balaceada
    # - 1 - Fator de balacemaneto
    # - 3 - Rotação para balancear.
    # - Rotação diretira - Rotação esquerda  (Rotação dupla)
    #3 - Caso não consiga a parte 1, gravar o video explicando o funcionamento de um balaceamento


import sys
from typing import AnyStr


class _No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = None

    def __str__(self):
        return f'{self.valor}'

    def is_folha(self):
        return self.direita is None and self.esquerda is None


class ArvoreBinaria:
    def __init__(self, tipo=None):
        self.raiz = None
        self.total = 0

    def _add(self, no_raiz, no):
        if not no_raiz:
            return no
        elif no.valor < no_raiz.valor:
            no_raiz.esquerda = self._add(no_raiz.esquerda, no)
        else:
            no_raiz.direita = self._add(no_raiz.direita, no)
        return no_raiz

    def add(self, valor):
        no = _No(valor)
        self.raiz = self._add(self.raiz, no)
        self.total += 1

    def get(self, valor):
        perc, anterior = self._get_perc(self.raiz, valor)
        return perc

    def _get_perc(self, perc, valor, anterior=None):
        if not perc:
            return
        elif perc.valor == valor:
            return perc, anterior
        elif valor > perc.valor:
            return self._get_perc(perc.direita, valor, perc)
        else:
            return self._get_perc(perc.esquerda, valor, perc)

    def minimo(self):
        return self._minimo(self.raiz)

    def maximo(self):
        return self._maximo(self.raiz)

    def _minimo(self, no_raiz):
        while no_raiz and no_raiz.esquerda:
            no_raiz = no_raiz.esquerda
        return no_raiz

    def _maximo(self, no_raiz):
        while no_raiz and no_raiz.direita:
            no_raiz = no_raiz.direita
        return no_raiz

    def __str__(self):
        self.ordem(self.raiz)
        return ''

    def ordem(self, raiz, tipo = 'in'):
        if not raiz:
            return
        if tipo == 'pre':
            print(raiz)
        self.ordem(raiz.esquerda, tipo)
        if tipo == 'in':
            print(raiz)
        self.ordem(raiz.direita, tipo)
        if tipo == 'post':
            print(raiz)

    def _get_sucessor(self, perc):
        perc = self._minimo(perc.direita)
        return perc

    def _get_predececessor(self, perc):
        perc = self._maximo(perc.esquerda)
        return perc

    def remover(self, valor):
        perc, anterior = self._get_perc(self.raiz, valor)
        if not perc:
            raise Exception('não existe esse item para remover')

        if perc.is_folha():
            if perc.valor > anterior.valor:
                anterior.direita = None
            else:
                anterior.esquerda = None
        else:
            sucessor = self._get_sucessor(perc)
            predecessor = self._get_predececessor(perc)
            if sucessor:
                anterior.direita = perc.direita
                sucessor.esquerda = perc.esquerda
                perc.direita = None
                perc.esquerda = None
            if not sucessor and predecessor:
                pass
        # print(perc.is_folha())
        # print(perc, anterior)
        # print("oba vamos remover")


    def get_lista(self):
        pass

    def create_arvore_to_lista(self, lista):
        pass

    def print(self):
        self.printHelper(self.raiz, '', True)




    def balancear(self):
        pass

    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.valor)
            self.printHelper(currPtr.esquerda, indent, False)
            self.printHelper(currPtr.direita, indent, True)


arvore = ArvoreBinaria()
arvore.add(60)
arvore.add(45)
arvore.add(80)
arvore.add(120)
arvore.add(50)
arvore.add(70)

# print(arvore.total)
print(arvore)
# print(arvore.minimo())
# print(arvore.maximo())
# arvore.remover(80)
print("**********")

# print(arvore.minimo())
print(arvore.print())
