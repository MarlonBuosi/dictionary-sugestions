# Nome: Marlon Vinicius Souza Buosi
# RA: 12461539
# Disciplina: Projeto de Software II
# Data: 25/09/2021

def n_gramas(palavras, n):
    '''
    Gera uma lista de n-gramas
    Exemplos:
        n_gramas(['amanhá', 'será', 'um', 'lindo', 'dia'], 2)
            deve retornar [ ['amanhá', 'será'],
                            ['será', 'um'],
                            ['um', 'lindo'],
                            ['lindo', 'dia'] ]

        n_gramas(['amanhá', 'será', 'um', 'lindo', 'dia'], 3)
            deve retornar [ ['amanhá', 'será', 'um'],
                            ['será', 'um', 'lindo'],
                            ['um', 'lindo', 'dia'] ]
    '''
    # <INSIRA SEU CÓDIGO AQUI>


def limpa_texto(texto):
    '''
    Remove caracteres indesejados de um texto.

    Exemplo:

        Ao receber o texto "Olá mundo! Mundo, mundo, mundo."
        Deverá devolver o texto: "Olá mundo Mundo mundo mundo"
    '''
    # <INSIRA SEU CÓDIGO AQUI>
    

def le_linhas_arquivo(arquivo):
    '''
    Abre um arquivo em modo leitura e devolve uma lista 
    com as suas linhas
    '''
    linhas = []
    try:
        # <INSIRA SEU CÓDIGO AQUI>
    except IOError:
        print("Erro ao abrir o arquivo {arquivo}")

    return linhas

def carrega_arquivo():

def grava_em_arquivo(linhas, arquivo, modo='w'):
    '''
    Recebe uma lista de linhas de texto e escreve no arquivo
    passado
    '''
    try:
        # <INSIRA SEU CÓDIGO AQUI>
    except IOError:
        print("Erro ao abrir o arquivo {arquivo}")

def carrega_dicionario(arquivo_dicionario):
    '''
    Recebe um arquivo de vocabulário, carrega em memória e 
    separa a palavra e a sua frequência, armazenando em uma estrutura
    aninhada (lista de listas ou lista de tuplas)
    
    Exemplo:
        Ao ler um arquivo com as seguintes linhas:
            que 12021478
            não 9712854
            o 9578625
        Deve retornar uma estrutura do tipo:
            [ ('que', 12021478), ('não', 9712854), ('o', 9578625) ]
    '''
    # <INSIRA SEU CÓDIGO AQUI>

def conta_mais_frequente(colecao):
    '''
    Dada uma determinada estrutura, conta qual o elemento
    mais frequente 

    Exemplo:
        Caso receba uma lista de palavras (unigramas) como:
         [ 'a', 'que', 'a', 'o', 'Nolan', 'em', 'a']
        Deve retornar:
         ['a', 3]

        Caso receba uma lista de bigramas como:
        [ ['a', 'Universal'],
          ['produção', 'em'],
          ['em', 'parceria'],
          ['parceria', 'com'],
          ['com', 'a'],
          ['a', 'Universal'],
          ['Universal', 'Pictures']]
        Deve retornar:
        [['a', 'Universal'], 2]

    '''
    # <INSIRA SEU CÓDIGO AQUI>
    
def gera_lista_unica(palavras):
    '''
    Recebe uma lista de palavras e gera uma lista onde cada
    palavra aparece apenas uma única vez

    Exemplo:
        Ao receber a lista de palavras:
            ['Python',  'é',  'uma',  'linguagem',  'de',  'programação',  'de',  'alto',
             'nível', 'Python', 'é', 'uma', 'linguagem', 'de', 'propósito', 'geral', 'multiparadigma']
        Deve retornar:
            ['python',  'é', 'uma', 'linguagem', 'de', 'programação', 'alto', 'nível', 'propósito', 
            'geral', 'multiparadigma']
    '''
    # <INSIRA SEU CÓDIGO AQUI>

def busca_palavras_oov(palavras, vocabulario):
    '''
    Deve receber uma lista de palavras e uma segunda lista de palavras
    contendo as palavras do vocabulário. 
    Retornar uma lista com todas as palavras que estão fora do vocabulário. 
    '''
    # <INSIRA SEU CÓDIGO AQUI>

def busca_sugestoes_correcao(palavras_oov, vocabulario):
    """
    Deve receber uma lista de palavras fora do vocabulário e uma lista
    de palavras do vocabulário. Para cada palavra da lista de palavras 
    fora do vocabulário (palavras_oov), verificar se há alguma palavra
    no vocabulário com o mesmo tamanho. Se houver, comparar com a palavra_oov
    e armazenar a palavra e a similaridade em uma lista. Se

    Depois de checar todo o vocabulário, pegar a lista de palavras similares
    criada, ordenar pelo valor da similaridade e pegar aquela com maior similaridade.
    Lembre-se de não inserir na lista palavras com similaridade igual a 0 (zero).

    Exemplo:                       vou 
        palavras_oov = ['kuando', 'zei']
        vocabulario =  [('vou', 896624), ('brando', 857006), ('quando', 848838), 
                        ('fazer', 841339), ('sei', 838749), ('famosa', 838449)]       

        busca_sugestoes_correcao(palavras_oov, vocabulario)

        Gere a lista de similaridade para 'kuando':
            As palavras 'vou', 'fazer' e 'sei' não serão comparadas, pois não tem
            o mesmo tamanho de 'kuando'.
            Assim, a lista de similaridade de 'kuando' será:
                [('brando', 4), ('quando', 5), ('famosa', 0)]
            Após ordenar, pela similaridade:
                [('famosa', 0), ('brando', 4), ('quando', 5)]

        Gere a lista de similaridade para 'zei':
            As palavras 'vou', 'fazer' e 'sei' não serão comparadas, pois não tem
            o mesmo tamanho de 'kuando'.
            Assim, a lista de similaridade de 'kuando' será:
                [('vou', 0), ('sei', 2)]
            Após ordenar, pela similaridade:
                [('vou', 0), ('sei', 2)]

        A lista final de sugestões de correções será a seguinte:
            [('kuando', 'quando'), ('zei', 'sei')]
    """
    # <INSIRA SEU CÓDIGO AQUI>


def main():
    # Abra o arquivo de texto e carregue o seu conteudo
    exemplo_texto = "".jon(le_linhas_arquivo("exemplo_texto.txt"))
    
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
