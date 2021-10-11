# Nome: Marlon Vinicius Souza Buosi
# RA: 12461539
# Disciplina: Projeto de Software II
# Data: 25/09/2021

def n_grams(words, n):

  try:
    sequencies = [words[i:] for i in range(n)]
    ngrams = zip(*sequencies)
  
  except IOError:
    print("Erro ao criar ngramas")
    return 0

  return [" ".join(ngram) for ngram in ngrams]

def clean_text(text, characters):
  translation = text.maketrans('', '', characters)
  text_clean = text.translate(translation)
  text_clean.replace('\n', '  ')

  return " ".join(text_clean.split())

def read_lines(file, encode):
  
  lines = []
  try:
    with open(file, 'r', encoding=encode) as f:
      lines = f.readlines()

  except IOError:
    print("Erro ao abrir o arquivo {arquivo}")

  return lines

def write_file(lines, file, encode, mode='w'):
  try:
    with open(file, mode, encoding=encode) as f:
      f.writelines(lines)

  except IOError:
    print("Erro ao abrir o arquivo {arquivo}")

def load_dictionary(dictionary_file, encode):
  
  lines = []
  try:
    with open(dictionary_file, 'r', encoding=encode) as f:
      lines = f.readlines()

    lexicon = [words.split() for words in lines]
    [int(numbers_words[1]) for numbers_words in lexicon]

  except IOError:
    print("Erro ao abrir o arquivo {arquivo_dicionario}")
  
  return lexicon

def count_frequency(colection):

  frequency = (dict(zip([colection.count(grams) for grams in colection], colection))).items()

  return max(frequency)
    
def unique_list(words):
  return sorted(set(words))

def busca_palavras_oov(words, vocabulary): 
  oov_words = []
  words = [word.lower() for word in words]
  oov_words = list(set(words).difference(vocabulary))

  return oov_words

def find_sugestions(oov_words, vocabulary):
  sugestions = []

  for words in oov_words:
    list = []
    for vocabulary_words in vocabulary:
      count = 0
      if len(words) == len(vocabulary_words): count = sum(1 for character_a, character_b in zip(words, vocabulary_words) if character_a == character_b)
      list.append((words, vocabulary_words, count))
    sugestions.append((max(list, key=lambda x: x[2])))

  sugestions.sort(reverse=True, key=lambda tuples: tuples[2])
  return sugestions

def main():
  # Parâmetros
  characters = '.,%]["$&:0123456789'
  # Abra o arquivo de texto e carregue o seu conteudo
  text_example = "".join(read_lines("exemplo_texto.txt", 'utf-8'))
  
  # Gera a lista de palavras do texto
  text_clean = clean_text(text_example, characters)

  # Gera lista de palavras do texto
  text_words = text_clean.split()

  # Gera os bigramas e trigramas
  bigrams = n_grams(text_words, 2)
  trigrams = n_grams(text_words, 3)

  # Conta os n-gramas mais frequentes
  frequent_unigram = count_frequency(text_words)
  frequent_bigram = count_frequency(bigrams)
  frequent_trigram = count_frequency(trigrams)

  # Monta as linhas com as informações de frequencia
  frequency_info = f"Unigrama mais frequente: '{frequent_unigram[1]}' Total: {frequent_unigram[0]}\n"
  frequency_info += f"Bigrama mais frequente: '{frequent_bigram[1]}' Total: {frequent_bigram[0]}\n"
  frequency_info += f"Trigrama mais frequente: '{frequent_trigram[1]}' Total: {frequent_trigram[0]}\n"
  
  # Grava as frequencias em um arquivo
  write_file(frequency_info, "contagens.txt", 'utf-8')
  
  # Carrega as palavras do dicionario
  dictionary_lines = load_dictionary("vocabulario.txt", 'utf-8')
  vocabulary = [x[0] for x in dictionary_lines]

  # Gera lista de palavras unicas
  unique_words = unique_list(text_words)

  # Busca palavras fora do vocabulário
  oov_words = busca_palavras_oov(unique_words, vocabulary)
  
  # Busca sugestoes de correcao
  correction_sugestions = find_sugestions(oov_words, vocabulary)
  
  # Grava as sugestões em arquivo
  lines_sugestions = []
  for sugestion in correction_sugestions:        
    lines = f"Palavra OOV: {sugestion[0]} Sugestão: {sugestion[1]}\n"
    lines_sugestions.append(lines)
  
  write_file(lines_sugestions, "palavras_alienigenas.txt", 'utf-8')

if __name__ == __name__=='__main__':
  main()
