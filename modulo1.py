'''
#Exercicio1

valor1 = 10
valor2 = 5

print("Soma dos valores:", valor1 + valor2)


#Example 4 - Using loops


for produto in range(1, 6):
    print("Número", produto)



contador = 3
while contador > 0:
    print(contador)
    contador -= 1     
print("Fim")    


#Example 5 - Using lists

frutaria = ["banana", "maçã"]
frutaria.append("uva")
print(frutaria)

#tupla
cores = ["vermelho", "azul", "verde"]
print(cores[0])

#dicionario
aluno = {"nome": "João", "idade": 20}
print(aluno["nome"])



#Exercicios
#De repetição até função curta

for i in range(5):
    print("Python é divertido!")


    
#funções   
    
def nome_da_funcao(parametro):
    return "resultado"

def somar(a, b):    
    return a + b        

resultado = somar(10, 5)
print(" O resultado da soma é:", resultado)
    


def ciclo_de_frutas():
    frutas = ["banana", "maçã", "uva"]
    for fruta in frutas:
        print("A fruta é", fruta)
    return fruta
        
ciclo_de_frutas()


def repetir_frase(frase, vezes):
    for _ in range(vezes):
        print(frase)
repetir_frase("Python é divertido!", 5)


# Uso do if, elif e else
idade = 15
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
    
    
    
# Ciclo while para validação
contagem = 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
    contagem += 1
    numero = int(input("Digite outro número (0 para sair): "))
print("Números digitados antes do 0:", contagem)
    
    
# Listas e For integrados
nomes = ["Ana", "Pedro", "Maria", "João", "Clara"]
for nome in nomes:
    print("Olá,", nome)
    
    
# Dicionários simples
amigo = {"nome": "Lucas", "idade": 20, "cidade": "Lisboa"}
print(f"{amigo['nome']} tem {amigo['idade']} anos e mora em {amigo['cidade']}.")    

    
# Conjuntos para remover duplicados
numeros = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(numeros)
print(conjunto)


#Tuplas imutáveis
estacoes = ("Primavera", "Verão", "Outono", "Inverno")
for estacao in estacoes:
    print(estacao)
    
    
# Função com argumento padrão
def quadrado(n=2):
    return n ** 2
print(quadrado())
print(quadrado(5))


# Recursividade simples
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)
print(fatorial(5))

'''


# listas

listaCores = ["vermelho", "azul", "verde"]
print(listaCores[1])


# dicionários

carro = {'marca': 'Renault', 'ano': 2020, 'cor': 'azul'}
print(carro['ano'])


# if, elif e else

def verificar_idade(idade):
    """Verifica a idade e retorna uma descrição."""
    if idade < 13:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    else:
        return "Adulto"


print(verificar_idade(15))


# methods

curso = "   python programming"
print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.strip())
print(curso.find("pro"))
print(curso.replace("p", "x"))
print(curso.split())
print("pro" in curso)
print("swift" not in curso)
