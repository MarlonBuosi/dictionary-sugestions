# Nome: Marlon Vinicius Souza Buosi
# RA: 12461539
# Disciplina: Projeto de Software II
# Data: 25/09/2021

def n_gramas(palavras, n):
  sequencias = [palavras[i:] for i in range(n)]
  ngramas = zip(*sequencias)
  return [" ".join(ngrama) for ngrama in ngramas]

def limpa_texto(texto):
  translation = texto.maketrans('', '', '.,%]["$&:0123456789')
  texto_limpo = texto.translate(translation)
  texto_limpo.replace('\n', '  ')
  return " ".join(texto_limpo.split())

def le_linhas_arquivo(arquivo):
  
  linhas = []
  try:
    with open(arquivo, 'r', encoding='utf-8') as f:
      linhas = f.readlines()

  except IOError:
    print("Erro ao abrir o arquivo {arquivo}")

  return linhas

def carrega_arquivo():
  placeholder3 = 0

def grava_em_arquivo(linhas, arquivo, modo='w'):
  try:
    with open(arquivo, modo) as f:
      f.writelines(linhas)

  except IOError:
    print("Erro ao abrir o arquivo {arquivo}")

def carrega_dicionario(arquivo_dicionario):
    
  linhas = []
  try:
    with open(arquivo_dicionario, 'r', encoding='utf-8') as f:
      linhas = f.readlines()

    dicionario = [palavras.split() for palavras in linhas]
    for numeros_palavras in dicionario:
      numeros_palavras[1] = int(numeros_palavras[1])

  except IOError:
    print("Erro ao abrir o arquivo {arquivo}")
  
  return dicionario

def conta_mais_frequente(colecao):
  vezes_que_repete = {}
  for gramas in colecao:
    vezes_que_repete[colecao.count(gramas)] = gramas
  frequencia = vezes_que_repete.items()
  
  return max(frequencia)
    
def gera_lista_unica(palavras):
  lista_unica = sorted(set(palavras))
  return lista_unica

def busca_palavras_oov(palavras, vocabulario): 
  for palavras_em_palavras in palavras:
    for palavras_em_vocabulario in vocabulario:
      if palavras_em_palavras == palavras_em_vocabulario:
        palavras.remove(palavras_em_vocabulario)
  palavras = [palavra.lower() for palavra in palavras]

  return palavras

def busca_sugestoes_correcao(palavras_oov, vocabulario):
  contador = 0
  sugestoes = []

  for palavras in palavras_oov:
    for palavras_vocabulario in vocabulario:
      if len(palavras) == len(palavras_vocabulario):
        caracteres = [char for char in palavras]
        caracteres_vocabulario = [char_vocabulario for char_vocabulario in palavras_vocabulario]
        for i in range(len(caracteres)):
          if caracteres[i] == caracteres_vocabulario[i]:
            contador += 1
        comparacoes = palavras, palavras_vocabulario, contador
        sugestoes.append(comparacoes)
        contador = 0
  sugestoes.sort(reverse=True, key=lambda tuplas: tuplas[2])

  return sugestoes

def main():
  # Abra o arquivo de texto e carregue o seu conteudo
  exemplo_texto = "".join(le_linhas_arquivo("exemplo_texto.txt"))
  
  # Gera a lista de palavras do texto
  texto_limpo = limpa_texto(exemplo_texto)

  # Gera lista de palavras do texto
  palavras_texto = texto_limpo.split()

  # Gera os bigramas e trigramas
  bigramas = n_gramas(palavras_texto, 2)
  trigramas = n_gramas(palavras_texto, 3)

  # Conta os n-gramas mais frequentes
  uni_mais_frequente = conta_mais_frequente(palavras_texto)
  bi_mais_frequente = conta_mais_frequente(bigramas)
  tri_mais_frequente = conta_mais_frequente(trigramas)

  # Monta as linhas com as informações de frequencia
  info_frequencia = f"Unigrama mais frequente: '{uni_mais_frequente[1]}' Total: {uni_mais_frequente[0]}\n"
  info_frequencia += f"Bigrama mais frequente: '{bi_mais_frequente[1]}' Total: {bi_mais_frequente[0]}\n"
  info_frequencia += f"Trigrama mais frequente: '{tri_mais_frequente[1]}' Total: {tri_mais_frequente[0]}\n"
  
  # Grava as frequencias em um arquivo
  grava_em_arquivo(info_frequencia, "contagens.txt")
  
  # Carrega as palavras do dicionario
  linhas_dicionario = carrega_dicionario("vocabulario.txt")
  vocabulario = [x[0] for x in linhas_dicionario]

  # Gera lista de palavras unicas
  palavras_unicas = gera_lista_unica(palavras_texto)

  # Busca palavras fora do vocabulário
  palavras_oov = busca_palavras_oov(palavras_unicas, vocabulario)
  
  # Busca sugestoes de correcao
  sugestoes_correcao = busca_sugestoes_correcao(palavras_oov, vocabulario)
  
  # Grava as sugestões em arquivo
  linhas_sugestoes = []
  for sugestao in sugestoes_correcao:        
    linha = f"Palavra OOV: {sugestao[0]} Sugestão: {sugestao[1]}\n"
    linhas_sugestoes.append(linha)
  
  grava_em_arquivo(linhas_sugestoes, "palavras_alienigenas.txt")

if __name__ == __name__=='__main__':
    main()
