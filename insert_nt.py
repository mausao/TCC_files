import io
import os

#Caminho do .fasta
path_fasta = r"C:\Users\mmjam\Área de Trabalho\TCC_files\TCC_files\consensus.fasta"

with open(path_fasta, "r") as arq:
    linhas = arq.readlines()

if not linhas:
    print("Arquivo vazio ou erro ao abrir o arquivo.")
    exit()

#Criação de um dicionário para armazenar as posições e os nucleotídeos
try:
    posicoes = input("Digite as posições que deseja inserir os nucleotídeos separadas por hífen (ex. 707-708) e caso sejam mais do que uma, separe-as por espaços simples (ex. 707-708 38450-38451)\n")
    nucleotideos = input("Digite os nucleotídeos que deseja inserir nas posições separados por espaços simples (ex. A T) e caso sejam mais do que um, mantenha-os juntos (ex. AA GGG)\n").upper()
except Exception as e:
    print("Erro ao inserir os valores:", e)
    exit()

posicoes_separadas = posicoes.split()
nucleotideos_separados = nucleotideos.split()

if len(posicoes_separadas) != len(nucleotideos_separados):
    print("Erro: quantidade de posições e nucleotídeos diferentes. Tente novamente.")
    exit()

pos_nt = {} #dicionário de posições e nucleotídeos

for i in range(len(posicoes_separadas)):
    try:
        inicio, fim = map(int, posicoes_separadas[i].split("-"))
        nucleotideo = nucleotideos_separados[i]
        if not all (base in 'ATGC' for base in nucleotideo):
            print(f"Erro: nucleotídeos inválidos: {nucleotideo}. Use apenas A T C G.")
            exit()
        pos_nt[f"{inicio}-{fim}"] = nucleotideo	
    except ValueError:
        print(f"Erro: posição inválida: {posicoes_separadas[i]}. Use apenas números separados por hífen.")
        exit()
    
print("Teste. Dicionario de posicoes e nucleotideos:")
for posicao, nucleotideo in pos_nt.items():
    print(f"{posicao}: {nucleotideo}")
