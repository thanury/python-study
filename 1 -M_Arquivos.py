import os

# Obter o nome do sistema operacional
print(os.name)

# Listar os arquivos e diretórios no diretório atual
print(os.listdir())

# Obter o diretório de trabalho atual
print(os.getcwd())

# Obter o separador de diretórios do sistema
print(os.sep)

# Criar um caminho para um arquivo usando o separador de diretórios
caminho = os.path.join(os.getcwd() + os.sep + '1.1_M_Arquivos.txt')
print(caminho)

# Obter o nome do diretório do caminho
print(os.path.dirname(os.path.join(os.getcwd()+ os.sep + '1.1_M_Arquivos.txt')))

# Obter o nome do arquivo do caminho
print(os.path.basename(caminho))

# Obter o nome do diretório do caminho usando split
print(os.path.split(caminho))

# Obter o nome do diretório do caminho usando split e indexação
print(os.path.split(caminho)[1])

# Como navegar até o diretório pai(nível acima)
caminho_atual = os.getcwd() + os.sep
print(caminho_atual)
print(os.path.abspath(os.path.join(caminho_atual, os.pardir)))