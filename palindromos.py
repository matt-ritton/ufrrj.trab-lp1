import re #Expressões regulares

#Programa leitura de palindromos distintos em texto, usando manipulação de arquivos, listas
#funções, manipulação de strings, enumerate e dicionário.

# Função para remover caracteres especiais, acentos, e para padronizar
# a caixa do texto (deixando tudo em caixa baixa.)
def formataTexto(texto):
    #Diminui todos os caracteres para caracteres minúsculos
    texto = texto.lower()
 
    #Lista com todas as pontuações
    lista_pontos = [' ','?','!','.',':','-',',','"',';','-']
    
    #Lista com todas as acentuações em A
    lista_espA = ['á','à','â','ã'] 
    #Lista com todas as acentuações em E
    lista_espE = ['é','ê']
    #Lista com todas as acentuações em I
    lista_espI = ['í']
    #Lista com todas as acentuações em O
    lista_espO = ['ó','õ','ô'] 
    #Lista com todas as acentuações em U
    lista_espU = ['ú','ü']
 
    #Corrige as acentuações e caracteres especiais
    for caractere in lista_pontos:
        texto = texto.replace(caractere, '')
    for caractere in lista_espA:
        texto = texto.replace(caractere, 'a')
    for caractere in lista_espE:
        texto = texto.replace(caractere, 'e')
    for caractere in lista_espI:
        texto = texto.replace(caractere, 'i')
    for caractere in lista_espO:
        texto = texto.replace(caractere, 'o')
    for caractere in lista_espU:
        texto = texto.replace(caractere, 'u')
    return texto
 
def palindromos(texto, textoOriginal):
    resultado = []
    txt_ext = len(texto) #lê todo o conteúdo do texto
    contador = 0 #Contador de Palindromos
    for i, valor in enumerate(texto):
 
        #Funcionamento do algoritmo: ao ler o texto, verificará se os caracteres ao redor
        #são iguais. Se sim, é adiciona ao set Resultado, que recebe valores iteráveis.
        #Em seguida, verifica se o próximo caracter de cada lado é igual, novamente
        #adicionando ao Resultado, se verdadeiro. Caso falso, sai do loop.
 
        #Para palindromos de comprimentos diferentes
        start = i - 1
        end = i + 1
        while start >= 0 and end < txt_ext and texto[start] == texto[end]:
            #Posicionamento do palindromo no texto usando dicionário
            palindromo = {'posicaoInicial': start,'palavra': texto[start:end+1],'posicaoFinal': end}
            resultado.append(palindromo) #Adiciona a palindrome encontrada
            contador+=1 #Contador soma +1
            start -= 1 #Indice recua -1 caracter para a esquerda
            end += 1 #Indice avança +1 caracter para a direita
 
        #Para palindromos de mesmo tamanho
        start = i
        end = i + 1
        while start >= 0 and end < txt_ext and texto[start] == texto[end]:
            #Posicionamento do palindromo no texto usando dicionário
            palindromo = {'posicaoInicial': start,'palavra': texto[start:end+1],'posicaoFinal': end}
            resultado.append(palindromo) #Adiciona a palindrome encontrada
            contador+=1 #Contador soma +1
            start -= 1 #Indice recua -1 caractere para a esquerda
            end += 1 #Indice avança +1 caractere para a direita
 
    pattern = re.compile(r"[\_\?\!\.\:\-\,\"\'\;\-\ ]") #Caracteres que devem ser pulados
    listaP = []
    for ix, crct in enumerate(textoOriginal):
        if(not re.search(pattern, crct)): #Procura os caracteres que devem ser pulados. Se não encontra-los...
            listaP.append(ix) #Armazena sua respectiva localização, no texto original
    
    for palindromo in resultado:
        pInicialOriginal = listaP[palindromo['posicaoInicial']] #Posição inicial no texto original
        pFinalOriginal = listaP[palindromo['posicaoFinal']] #Posição final no texto original
        palindromoOriginal = textoOriginal[pInicialOriginal:pFinalOriginal+1] #Palindromo no texto original
        print("Palíndromo: [%d] %s [%d]" %(pInicialOriginal, palindromoOriginal, pFinalOriginal))
    print("Numero de Palindromos encontradas: ", contador)

#Leitura de Arquivo.txt
arq = open('texto.txt', 'r') #Abre um arquivo .txt no diretório do programa
texto = arq.read() #Variável texto lê o conteúdo de um arquivo .txt e recebe-o
arq.close() #Fecha o arquivo .txt
print ('Sentença: ',texto) #Imprime a sentença, sem alterações

texto_original = texto
texto = formataTexto(texto)
palindromos(texto, texto_original)