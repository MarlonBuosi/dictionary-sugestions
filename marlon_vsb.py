# Nome: Marlon Vinicius Souza Buosi
# RA: 12461539
# Disciplina: Projeto de Software II
# Data: 25/09/2021

def n_gramas(palavras, n):
  sequencias = [palavras[i:] for i in range(n)]
  ngramas = zip(sequencias[0], sequencias[1], sequencias[2])
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
      # <INSIRA SEU CÓDIGO AQUI>
      placeholder4 = 0
  except IOError:
      print("Erro ao abrir o arquivo {arquivo}")

def carrega_dicionario(arquivo_dicionario):
  # <INSIRA SEU CÓDIGO AQUI>
  placeholder=6 = 0

def conta_mais_frequente(colecao):
  placeholder7 = 0
  # <INSIRA SEU CÓDIGO AQUI>
    
def gera_lista_unica(palavras):
  # <INSIRA SEU CÓDIGO AQUI>
  placeholder7 = 0

def busca_palavras_oov(palavras, vocabulario):
  # <INSIRA SEU CÓDIGO AQUI>
  placeholder8 = 0

def busca_sugestoes_correcao(palavras_oov, vocabulario):
  placeholder9 = 0
  # <INSIRA SEU CÓDIGO AQUI>

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
  info_frequencia = f"Unigrama mais frequente: {uni_mais_frequente[0]} Total: {uni_mais_frequente[1]}\n"
  info_frequencia += f"Bigrama mais frequente: {bi_mais_frequente[0]} Total: {bi_mais_frequente[1]}\n"
  info_frequencia += f"Trigrama mais frequente: {tri_mais_frequente[0]} Total: {tri_mais_frequente[1]}\n"
  
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
