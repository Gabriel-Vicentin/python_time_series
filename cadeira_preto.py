#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Criador: Gabriel Vicentin Bonfim   
# Data de criação: 25/08/2025 
# Versão ='1.3'
# Descrição: Funções básicas para analisar valores
# ---------------------------------------------------------------------------

"""Docstring: Docstrings são maneiras de comentar durante o código. É Possível acessar as Docstrings durante o período de funcionamento do código, possibilitando a criação de funções extras para prestar ajuda em relação a documentação."""

#Cabeçalho: O cabeçalho é utilizado para dar um contexto geral do código e informações básicas sobre seu autor.



def maximo(nums):
	"""
	Calcula o maior número digitado em uma lista 
	"""
	lista = []
	for i in range(nums):
		lista.append(int(input(f"Digite o número {i + 1} da lista: ")))
	maior = lista[0]
	for i in range(len(lista)):
		if maior < lista[i]:
			maior = lista[i]
	print("Maior numero digitado: ", maior)
	return maior

maximo(5)

def e_par(n: int) -> bool:
	"""
	Recebe um Numéro N e Informa se este número é par ou impar.
	"""
	if n % 2 == 0:
		print("É par")
		return True
	else:
		print("É impar")
		return False
	# Ternario: print ("É par" if n % 2 == 0 else "É impar")

e_par(2)

def fatorial(n: int) -> int:
	"""
	Recebe um Número N e informa o resultado do fatorial do mesmo
	"""
	fat = 1
	for i in range(1, n + 1):
		fat *= i
	print(f"Resultado final: {fat}")
	return fat

fatorial(5)


help(maximo)
help(e_par)
help(fatorial)