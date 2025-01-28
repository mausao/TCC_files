import os

# Caminho do .fasta
path_fasta = r"C:\Users\mmjam\Área de Trabalho\TCC_files\teste.fasta"

# Caminho para o arquivo com inserções
novo_path_fasta = r"C:\Users\mmjam\Área de Trabalho\TCC_files\teste_modificado.fasta"

# Ler o arquivo .fasta
with open(path_fasta, "r") as arq:
    linhas = arq.readlines()

if not linhas:
    print("Arquivo vazio ou erro ao abrir o arquivo.")
    exit()

# Extrair a sequência de DNA (ignorando a linha do cabeçalho)
sequencia = ''.join(linha.strip() for linha in linhas[1:])

# Solicitar posições e nucleotídeos ao usuário
try:
    posicoes = input("Digite as posições que deseja inserir os nucleotídeos separadas por hífen (ex. 4-5) e caso sejam mais do que uma, separe-as por espaços simples (ex. 4-5 8-9)\n")
    nucleotideos = input("Digite os nucleotídeos que deseja inserir nas posições separados por espaços simples (ex. GGG AA) e caso sejam mais do que um, mantenha-os juntos (ex. GGG AA)\n").upper()
except Exception as e:
    print("Erro ao inserir os valores:", e)
    exit()

# Separar posições e nucleotídeos
posicoes_separadas = posicoes.split()
nucleotideos_separados = nucleotideos.split()

# Verificar se o número de posições e nucleotídeos é o mesmo
if len(posicoes_separadas) != len(nucleotideos_separados):
    print("Erro: quantidade de posições e nucleotídeos diferentes. Tente novamente.")
    exit()

# Função para inserir nucleotídeos na sequência
def inserir_nt(sequencia, posicoes, nucleotideos):
    # Ordenar as inserções pelas posições (para evitar problemas com deslocamentos)
    #zip junta as duas listas (posicoes e nucleotideos) em uma lista de tuplas, onde cada tupla contém uma posição e um nucleotídeo, sorted ordena a lista de acordo com a posição
    #key em sorted é um parametro, e = lambda significa que é um parametro com uma função anônima, que recebe x e retorna x[0].split('-')[0], que é a posição inicial da inserção (em 4-5, retorna o 4 p. ex.)
    insercoes = sorted(zip(posicoes, nucleotideos), key=lambda x: int(x[0].split('-')[0]))
    
    for i in range(len(insercoes)):
        posicao, nucleotideo = insercoes[i]
        inicio, fim = map(int, posicao.split('-'))
        
        # Inserir os nucleotídeos ENTRE as posições (sem substituir)
        sequencia = sequencia[:inicio] + nucleotideo + sequencia[inicio:]
        
        # Ajustar as posições subsequentes
        for j in range(i + 1, len(insercoes)):
            novo_inicio, novo_fim = map(int, insercoes[j][0].split('-'))
            if novo_inicio > inicio:
                deslocamento = len(nucleotideo)
                novo_inicio += deslocamento
                novo_fim += deslocamento
                insercoes[j] = (f"{novo_inicio}-{novo_fim}", insercoes[j][1])
    return sequencia

# Aplicar as inserções
sequencia_modificada = inserir_nt(sequencia, posicoes_separadas, nucleotideos_separados)

# Escrever a sequência modificada em um novo arquivo .fasta
with open(novo_path_fasta, "w") as novo_arq:
    novo_arq.write(linhas[0])  # Manter o cabeçalho original
    novo_arq.write(sequencia_modificada)  # Escrever a sequência modificada

print(f"Sequência modificada salva em: {novo_path_fasta}")