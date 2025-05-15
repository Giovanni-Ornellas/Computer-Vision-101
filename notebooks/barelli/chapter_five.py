import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem_rgb = cv2.imread("data/raw/nineth_image.jpeg")
imagem_cinza = cv2.cvtColor(imagem_rgb, cv2.COLOR_BGR2GRAY)

def imprimir_pixel(imagem):
    """
    @brief Imprime o valor de um pixel específico da imagem.

    @details
    Esta função acessa diretamente o valor do pixel localizado na posição (linha=148, coluna=150)
    da imagem fornecida. O valor retornado depende do formato da imagem:

    - Para imagens coloridas (RGB ou BGR), o retorno será uma tupla/lista com 3 valores, 
      representando os canais de cor.
    - Para imagens em escala de cinza, o retorno será um único valor de intensidade (0–255).

    @param imagem: Imagem carregada como matriz NumPy.
    @return Nenhum valor é retornado, apenas imprime no terminal.
    """

    # Acessa o valor do pixel na linha 148 e coluna 150
    valor_pixel = imagem[148, 150]

    # Imprime o valor do pixel no terminal
    print(valor_pixel)

def imprimir_canal(imagem):
    """
    @brief Imprime os valores dos canais B, G e R de um pixel específico.

    @details
    Esta função acessa a imagem fornecida como matriz NumPy e imprime separadamente os valores
    dos três canais de cor (azul, verde e vermelho) do pixel localizado na linha 148 e coluna 150.

    A ordem dos canais segue o padrão BGR do OpenCV:
        - Canal 0: Azul (Blue)
        - Canal 1: Verde (Green)
        - Canal 2: Vermelho (Red)

    @param imagem: Imagem colorida no formato BGR (como lida com cv2.imread()).

    @return Nenhum valor é retornado; os valores são exibidos no terminal.
    """
    valor_pixel_b = imagem[148, 150, 0] 
    valor_pixel_g = imagem[148, 150, 1] 
    valor_pixel_r = imagem[148, 150, 2] 


    print("Valor do canal B:", valor_pixel_b)
    print("Valor do canal G:", valor_pixel_g)
    print("Valor do canal R:", valor_pixel_r)

def modifica_pixel(imagem):
    """
    @brief Modifica diretamente o valor de um pixel da imagem.

    @details
    Esta função imprime o valor original do pixel localizado na posição (150, 150),
    modifica esse pixel para a cor branca `[255, 255, 255]`, e imprime novamente o valor
    para mostrar a mudança.

    Essa operação é útil para demonstrações de manipulação direta de imagem com NumPy.
    Funciona apenas com imagens coloridas (3 canais - BGR).

    @param imagem: Imagem colorida carregada como matriz NumPy (formato BGR).

    @return Nenhum valor é retornado.
    """

    # Imprime o valor original do pixel na posição (150, 150)
    print("Antes da modificação:", imagem[150, 150])

    # Modifica o pixel para branco (255 em todos os canais)
    imagem[150, 150] = [255, 255, 255]

    # Imprime o novo valor do pixel modificado
    print("Depois da modificação:", imagem[150, 150])

def acessar_informações(imagem):
    """
    @brief Exibe as dimensões da imagem (shape).

    @details
    Esta função imprime a forma (shape) da imagem fornecida. O resultado é uma tupla
    que descreve as dimensões da matriz NumPy que representa a imagem:

        - Para imagens coloridas: (altura, largura, canais)
        - Para imagens em tons de cinza: (altura, largura)

    Também imprime o número total de **valores numéricos** armazenados na imagem,
    o que inclui todos os canais (não apenas os pixels).

    Essa informação é útil para entender o tipo da imagem (colorida ou cinza),
    sua resolução e estrutura interna.

    @param imagem: Imagem carregada como matriz NumPy.
    @return Nenhum valor é retornado; apenas imprime as dimensões.
    """

    # Exibe as dimensões da imagem:
    # (altura, largura) se for em escala de cinza
    # (altura, largura, canais) se for colorida
    print("Shape da imagem:", imagem.shape)

    # Exibe o número total de elementos (valores individuais) da matriz,
    # incluindo todos os canais (por isso pode ser maior que altura × largura)
    print("Total de Pixels:", imagem.size)

def converter_para_bmp(imagem):
    """
    @brief Salva a imagem como BMP colorida e também como bitmap preto e branco.

    @details
    A função salva a imagem original no formato .bmp e também gera uma versão em
    preto e branco (binária) usando limiarização (threshold). Ambas as versões
    são salvas em disco e exibidas com OpenCV.

    @param imagem: Imagem colorida (BGR) carregada com OpenCV.
    @return Nenhum valor é retornado.
    """

    # 1. Salva a imagem colorida no formato BMP
    cv2.imwrite("data/processed/Caneca.bmp", imagem)

    # 2. Converte para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # 3. Aplica threshold para obter imagem binária (preto e branco)
    _, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

    # 4. Salva a imagem binária como BMP
    cv2.imwrite("data/processed/Caneca-PretoBranco.bmp", imagem_binaria)

    # 5. Mostra a imagem binária
    cv2.imshow("Imagem binária (preto e branco)", imagem_binaria)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def plotar_manualmente():
    """
    @brief Conta manualmente a quantidade de pixels pretos e brancos em uma imagem binária.

    @details
    A função carrega uma imagem BMP em preto e branco (valores 0 e 255), e percorre
    os primeiros 499x499 pixels da imagem. Para cada pixel, verifica se ele é branco (255)
    ou preto (qualquer outro valor, geralmente 0), e acumula os totais.

    A imagem deve estar previamente binarizada (ex: usando cv2.THRESH_BINARY).

    @return Nenhum valor é retornado, apenas imprime os totais de pixels no terminal.
    """

    # Carrega a imagem em tons de cinza (modo 0) para garantir que os valores sejam únicos por pixel
    imagem = cv2.imread("data/processed/Segunda-Guerra-PretoBranco.bmp", 0)

    # Inicializa contadores
    total_pixels_preto  = 0
    total_pixels_branco = 0

    #

    # Percorre a imagem nas posições (0,0) até (498,498)
    for x in range(0, 499):
        for y in range(0, 499):
            # Se o valor do pixel for 255, é branco
            if imagem[x, y] == 255:
                total_pixels_branco += 1
            else:
                total_pixels_preto += 1

    # Exibe os resultados no terminal
    print("Total de pixels pretos:", total_pixels_preto)
    print("Total de pixels brancos:", total_pixels_branco)


def plotar_binário():
    """
    @brief Plota o histograma de uma imagem binária (preto e branco).

    @details
    Esta função lê uma imagem em preto e branco (valores 0 e 255),
    e utiliza o matplotlib para exibir o histograma da distribuição de
    intensidade de pixels. Ideal para verificar visualmente a proporção
    de áreas escuras (preto) e claras (branco) em uma imagem limiarizada.

    Este histograma mostra a distribuição de intensidade dos pixels da imagem.
    - imagem.ravel(): transforma a imagem em vetor 1D
    - 256: número de bins (de 0 a 255)
    - [0, 256]: intervalo das intensidades

    @return Nenhum valor é retornado; apenas exibe o gráfico.
    """

    # Carrega a imagem em escala de cinza
    imagem = cv2.imread("data/processed/Segunda-Guerra-PretoBranco.bmp", 0)

    # Plota o histograma usando matplotlib
    plt.hist(imagem.ravel(), 256, [0, 256])
    plt.title("Histograma da Imagem Binária")
    plt.xlabel("Intensidade (0=preto, 255=branco)")
    plt.ylabel("Quantidade de pixels")
    plt.grid(True)
    plt.show()

def plotar_cinza(imagem):
    """
    @brief Plota o histograma de uma imagem em tons de cinza.

    @details
    Esta função recebe uma imagem em escala de cinza (1 canal) e plota
    seu histograma de intensidade de pixels usando Matplotlib. O histograma
    mostra a distribuição de tons (de 0 a 255) e ajuda a entender o brilho,
    contraste e conteúdo da imagem.

    @param imagem: Imagem em tons de cinza (matriz NumPy 2D).
    @return Nenhum valor é retornado; o gráfico é exibido na tela.
    """

    # Plota o histograma da imagem: 256 barras de intensidade entre 0 e 255
    plt.hist(imagem.ravel(), 256, [0, 256])

    # Define o título do gráfico
    plt.title("Histograma da Imagem Cinza")

    # Rótulo do eixo X: intensidade dos pixels (0 = preto, 255 = branco)
    plt.xlabel("Intensidade (0 a 255)")

    # Rótulo do eixo Y: quantidade de pixels em cada faixa de intensidade
    plt.ylabel("Quantidade de pixels")

    # Mostra a grade para facilitar leitura do gráfico
    plt.grid(True)

    # Exibe o histograma na tela
    plt.show()

def plotar_colorido():
    """
    @brief Plota os histogramas dos canais de cor de uma imagem colorida.

    @details
    Esta função carrega uma imagem colorida no formato BGR (padrão do OpenCV),
    separa seus três canais (Azul, Verde e Vermelho), e plota um histograma
    individual para cada canal usando matplotlib. Isso permite analisar como os
    valores de intensidade estão distribuídos em cada componente de cor da imagem.

    @return Nenhum valor é retornado; os gráficos são exibidos na tela.
    """

    # Carrega a imagem colorida (formato BGR)
    imagem = cv2.imread("data/processed/Segunda-Guerra-Colorida.bmp")

    # Separa os três canais: azul, verde e vermelho
    azul, verde, vermelho = cv2.split(imagem)

    # Plota o histograma do canal azul
    plt.hist(azul.ravel(), 256, [0, 256])
    plt.title("Histograma B")  # B = Blue (Azul)

    # Cria nova figura para o próximo gráfico
    plt.figure()

    # Plota o histograma do canal verde
    plt.hist(verde.ravel(), 256, [0, 256])
    plt.title("Histograma G")  # G = Green (Verde)

    # Cria nova figura para o próximo gráfico
    plt.figure()

    # Plota o histograma do canal vermelho
    plt.hist(vermelho.ravel(), 256, [0, 256])
    plt.title("Histograma R")  # R = Red (Vermelho)

    # Exibe todos os gráficos
    plt.show()

def equalizar_histograma():
    """
    @brief Aplica equalização de histograma em uma imagem em tons de cinza.

    @details
    Esta função realiza o processo de equalização de histograma usando OpenCV para
    melhorar o contraste de uma imagem em escala de cinza. A imagem original e a 
    imagem equalizada são exibidas lado a lado para comparação. Também são exibidos 
    os histogramas de ambas, permitindo visualizar como a distribuição de intensidades 
    foi ajustada.

    Passos realizados:
    - Leitura da imagem original em tons de cinza
    - Redução do tamanho (50%) para facilitar a visualização
    - Aplicação da equalização de histograma com `cv2.equalizeHist()`
    - Exibição das duas imagens
    - Exibição dos histogramas antes e depois

    @return Nenhum valor é retornado; apenas exibe as imagens e histogramas.
    """

    # Lê a imagem no modo grayscale (0 = cv2.IMREAD_GRAYSCALE)
    imagem_original = cv2.imread("data/raw/third_image.jpeg", 0)

    # Redimensiona a imagem para 50% do tamanho original
    imagem_original = cv2.resize(imagem_original, (0, 0), fx=0.5, fy=0.5)

    # Aplica equalização de histograma (melhora o contraste da imagem)
    imagem_equalizada = cv2.equalizeHist(imagem_original)

    # Salva a imagem tratada
    cv2.imwrite("data/processed/Segunda-Guerra-Tratada.jpeg", imagem_equalizada)

    # Exibe a imagem original
    cv2.imshow("Imagem Original", imagem_original)

    # Exibe a imagem após equalização
    cv2.imshow("Imagem Equalizada", imagem_equalizada)

    # Plota o histograma da imagem original
    plt.hist(imagem_original.ravel(), 256, [0, 256])
    plt.title("Histograma Original")

    # Cria uma nova figura para o próximo histograma
    plt.figure()

    # Plota o histograma da imagem equalizada
    plt.hist(imagem_equalizada.ravel(), 256, [0, 256])
    plt.title("Histograma Equalizado")

    # Mostra os gráficos
    plt.show()

def rotacionar():
    """
    @brief Rotaciona uma imagem em 90 graus no sentido horário.

    @details
    Esta função carrega uma imagem em tons de cinza do caminho especificado,
    calcula a matriz de rotação usando o centro da imagem como ponto de referência
    e aplica a transformação afim (rotação) com OpenCV. A imagem resultante é exibida
    em uma nova janela.

    A função inclui uma verificação para garantir que a imagem foi carregada corretamente.
    O processo usa rotação de 90 graus no sentido horário com escala igual a 1.

    @return Nenhum valor é retornado. A imagem rotacionada é exibida em tela.
    """

    # Lê a imagem em escala de cinza (modo 0)
    imagem_original = cv2.imread("data/raw/first_image.jpg", 0)

    # Verifica se a imagem foi carregada corretamente
    if imagem_original is None:
        print("Erro: imagem não encontrada ou caminho inválido.")
        return

    # Obtém altura e largura da imagem
    total_de_linhas, total_de_colunas = imagem_original.shape

    # Cria matriz de rotação em torno do centro da imagem (ângulo 90°)
    matriz = cv2.getRotationMatrix2D((total_de_colunas / 2, total_de_linhas / 2), 90, 1)

    # Aplica a rotação à imagem
    imagem_rotacionada = cv2.warpAffine(imagem_original, matriz, (total_de_colunas, total_de_linhas))

    # Exibe o resultado
    cv2.imshow("Resultado", imagem_rotacionada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transladar():
    """
    @brief Aplica uma translação (deslocamento) à imagem carregada.

    @details
    Esta função lê uma imagem colorida e aplica uma transformação afim (translação),
    deslocando a imagem 100 pixels para a direita (eixo X) e 100 pixels para baixo (eixo Y).
    A translação é definida por uma matriz 2x3, aplicada com a função `cv2.warpAffine()`.

    A imagem deslocada é então exibida em uma janela OpenCV.

    @note
    O deslocamento aplicado é fixo: (x + 100, y + 100). Para usar outros valores,
    é necessário alterar a matriz de translação.

    @return Nenhum valor é retornado. A imagem transladada é apenas exibida em tela.
    """

    # Carrega a imagem em formato BGR
    imagem_original = cv2.imread("data/raw/first_image.jpg")

    # Verifica se a imagem foi carregada corretamente
    if imagem_original is None:
        print("Erro: imagem não encontrada ou caminho inválido.")
        return

    # Obtém as dimensões da imagem (altura e largura)
    total_de_linhas, total_de_colunas = imagem_original.shape[:2]

    # Define a matriz de translação: move 100 px para a direita e 100 px para baixo
    matriz = np.array([[1, 0, 100],   # [1, 0, deslocamento X]
                       [0, 1, 100]],  # [0, 1, deslocamento Y]
                      dtype=np.float32)

    # Aplica a translação usando transformação afim
    imagem_deslocada = cv2.warpAffine(imagem_original, matriz, (total_de_colunas, total_de_linhas))

    # Exibe a imagem transladada
    cv2.imshow("Resultado", imagem_deslocada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def escalonar():
    """
    @brief Redimensiona (escalona) uma imagem, ampliando-a em 2x.

    @details
    Esta função carrega uma imagem colorida e a amplia em 2 vezes seu tamanho original
    tanto na largura (eixo X) quanto na altura (eixo Y). Para preservar melhor a nitidez
    da imagem durante o redimensionamento, é utilizada a interpolação bicúbica (`cv2.INTER_CUBIC`),
    que calcula novos valores de pixels considerando uma vizinhança de 4x4.

    A imagem ampliada é exibida em uma janela com o título "Resultado".

    @note
    Ao ampliar uma imagem, é comum ocorrer suavização (borramento) devido à interpolação,
    especialmente se a imagem original tiver baixa resolução. A escolha do tipo de interpolação
    influencia diretamente na nitidez percebida.

    @return Nenhum valor é retornado. A imagem ampliada é apenas exibida.
    """

    # Carrega a imagem original colorida
    imagem_original = cv2.imread("data/raw/first_image.jpg")

    # Verifica se a imagem foi carregada corretamente
    if imagem_original is None:
        print("Erro: imagem não encontrada.")
        return

    # Redimensiona a imagem com fator 2x usando interpolação bicúbica
    imagem_modificada = cv2.resize(
        imagem_original, None, fx=2, fy=2, 
        interpolation=cv2.INTER_CUBIC
    )

    # Exibe a imagem redimensionada
    cv2.imshow("Resultado", imagem_modificada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ajustar_perspectiva():
    """
    @brief Corrige a perspectiva da imagem de uma pista com base em 4 pontos manuais.

    @details
    Esta função carrega uma imagem da pista e aplica uma transformação de perspectiva,
    convertendo a área definida por 4 pontos iniciais (obtidos visualmente) em uma visão
    retangular padronizada. Essa técnica é útil para eliminar distorções de perspectiva
    quando a imagem é capturada com ângulo inclinado.

    A transformação é feita com cv2.getPerspectiveTransform e aplicada com cv2.warpPerspective.

    - Os pontos iniciais devem corresponder aos 4 cantos da pista preta no plano original.
    - Os pontos finais definem o plano de saída (retângulo retificado).
    
    @return Nenhum valor é retornado. A função exibe as imagens original e transformada.
    """

    # Carrega a imagem da pista
    imagem = cv2.imread("data/raw/fourth_image.jpeg")

    # Define os 4 pontos da área preta (ajuste conforme necessário)
    pontos_iniciais = np.float32([
        [80, 100],
        [1230, 80],
        [60, 720],
        [1240, 730]
    ])

    # Define os 4 pontos do plano de saída (retângulo final)
    pontos_finais = np.float32([
        [0, 0],
        [800, 0],
        [0, 600],
        [800, 600]
    ])

    # Gera a matriz de transformação
    matriz = cv2.getPerspectiveTransform(pontos_iniciais, pontos_finais)

    # Aplica a transformação de perspectiva
    imagem_transformada = cv2.warpPerspective(imagem, matriz, (800, 600))

    # Exibe os resultados
    cv2.imshow("Original", imagem)
    cv2.imshow("Transformada", imagem_transformada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def somar_imagens():
    """
    @brief Soma duas imagens e exibe o resultado.

    @details
    Esta função realiza a leitura de duas imagens do disco, redimensiona a segunda imagem para
    ter o mesmo tamanho da primeira (caso necessário) e aplica uma operação de soma pixel a pixel.
    O resultado da soma é então exibido em uma janela.

    A função verifica se as imagens foram carregadas corretamente antes de continuar. Caso uma delas
    não seja encontrada, a execução é interrompida com uma mensagem de erro.

    A função usa cv2.add() para somar as imagens, garantindo saturação dos valores de cor (valores
    maiores que 255 são truncados para 255).


    @return Nenhum valor é retornado. A imagem somada é exibida em uma janela.
    """

    # Lê as duas imagens do disco
    primeira_imagem = cv2.imread("data/raw/first_image.jpg")
    segunda_imagem  = cv2.imread("data/raw/second_image.jpg")

    # Verifica se ambas foram carregadas com sucesso
    if primeira_imagem is None or segunda_imagem is None:
        print("Erro: Imagem não encontrada.")
        return

    # Redimensiona a segunda imagem para ter o mesmo tamanho da primeira
    segunda_imagem = cv2.resize(segunda_imagem, (primeira_imagem.shape[1], primeira_imagem.shape[0]))

    # Soma pixel a pixel as duas imagens
    imagem_somada = cv2.add(primeira_imagem, segunda_imagem)

    # Exibe a imagem resultante da soma
    cv2.imshow("Resultado", imagem_somada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mudar_contraste():
    """
    @brief Altera o brilho da imagem e plota os histogramas.

    @details
    Esta função carrega uma imagem e gera duas variações:
    uma imagem mais clara e uma mais escura. Isso é feito adicionando e subtraindo
    um valor constante dos valores de intensidade de cada pixel (com `cv2.add()`).

    Em seguida, plota os histogramas das três versões:
    - Original
    - Clara (mais brilho)
    - Escura (menos brilho)

    Essa técnica não altera o contraste diretamente, mas sim o brilho da imagem.
    Para modificar o contraste, seria necessário aplicar uma multiplicação escalar nos pixels.

    @return Nenhum valor é retornado. Os histogramas são exibidos com Matplotlib.
    """

    # Carrega a imagem original
    imagem_original = cv2.imread("data/raw/second_image.jpg")

    # Gera uma imagem mais clara e uma mais escura
    imagem_clara  = cv2.add(imagem_original, 40)   # Aumenta brilho
    imagem_escura = cv2.add(imagem_original, -40)  # Diminui brilho

    # Plota o histograma da imagem original
    plt.hist(imagem_original.ravel(), 256, [0, 256])
    plt.title("Histograma - Original")

    # Plota o histograma da imagem mais clara
    plt.figure()
    plt.hist(imagem_clara.ravel(), 256, [0, 256])
    plt.title("Histograma - Mais Clara")

    # Plota o histograma da imagem mais escura
    plt.figure()
    plt.hist(imagem_escura.ravel(), 256, [0, 256])
    plt.title("Histograma - Mais Escura")

    # Exibe os gráficos
    plt.show()

    # Fecha qualquer janela aberta do OpenCV (por segurança)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def misturar_imagens():
    """
    @brief Realiza a mistura de duas imagens com pesos diferentes.

    @details
    Esta função lê duas imagens do disco e redimensiona a segunda imagem
    para que tenha as mesmas dimensões da primeira. Em seguida, combina
    as duas imagens utilizando a função `cv2.addWeighted()`.

    A operação de mistura é feita com os seguintes pesos:
    - 0.6 para a primeira imagem
    - 0.3 para a segunda imagem
    - 0 como deslocamento (bias)

    A soma ponderada resulta em uma nova imagem com efeito de sobreposição.

    @return Nenhum valor é retornado; a imagem resultante é exibida na tela.
    """

    # Lê as duas imagens do disco
    primeira_imagem = cv2.imread("data/raw/first_image.jpg")
    segunda_imagem  = cv2.imread("data/raw/second_image.jpg")

    # Redimensiona a segunda imagem para o tamanho da primeira
    segunda_imagem = cv2.resize(segunda_imagem, (primeira_imagem.shape[1], primeira_imagem.shape[0]))

    # Mistura as imagens com pesos 0.6 e 0.3 (respectivamente)
    imagem_misturada = cv2.addWeighted(
        primeira_imagem, 0.6, segunda_imagem, 0.6, 1
    )

    # Exibe a imagem resultante
    cv2.imshow("Resultado", imagem_misturada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # imprimir_pixel(imagem_rgb)
    # imprimir_pixel(imagem_cinza)
    # imprimir_canal(imagem_rgb)
    # modifica_pixel(imagem_rgb)
    # acessar_informações(imagem_rgb)
     converter_para_bmp(imagem_rgb)
    # plotar_manualmente()
    # plotar_binário()
    # plotar_cinza(imagem_cinza)
    # plotar_colorido()
    # equalizar_histograma()
    # rotacionar()
    # transladar()
    # escalonar()
    # ajustar_perspectiva()
    # somar_imagens()
    # mudar_contraste()
    # misturar_imagens()

if __name__ == "__main__":
    main()