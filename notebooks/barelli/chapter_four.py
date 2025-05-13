import cv2

# Carrega a imagem a partir do caminho especificado
imagem = cv2.imread("data/raw/second_image.jpg")


def segmentar_imagem(imagem):
    """
    @brief Segmenta uma imagem em seus canais de cores (BGR) usando OpenCV.

    @details
    Esta função recebe uma imagem no formato BGR (padrão do OpenCV) e a divide em
    três canais individuais: azul, verde e vermelho. Cada um desses canais é exibido
    separadamente em uma janela e também salvo como arquivo JPEG.

    A função utiliza cv2.split() para realizar a separação e cv2.imwrite() para salvar
    os canais como imagens independentes. As janelas permanecem abertas até que o usuário
    pressione uma tecla.

    @note
    As imagens segmentadas são salvas nos caminhos:
        - data/processed/Frutas-canal-vermelho.jpeg
        - data/processed/Frutas-canal-verde.jpeg
        - data/processed/Frutas-canal-azul.jpeg

    @param imagem: Imagem carregada a ser segmentada.
    @return Nenhum valor é retornado.
    """

    # Segmenta os canais da imagem (OpenCV usa BGR, não RGB)
    azul, verde, vermelho = cv2.split(imagem)

    # Exibe a imagem original e os canais separadamente
    cv2.imshow("Original", imagem)
    cv2.imshow("Canal R", vermelho)
    cv2.imshow("Canal G", verde)
    cv2.imshow("Canal B", azul)

    # Salva os canais como arquivos de imagem
    cv2.imwrite("data/processed/Frutas-canal-vermelho.jpeg", vermelho)
    cv2.imwrite("data/processed/Frutas-canal-verde.jpeg", verde)
    cv2.imwrite("data/processed/Frutas-canal-azul.jpeg", azul)

    # Espera até que o usuário pressione uma tecla
    cv2.waitKey(0)

    # Fecha todas as janelas abertas
    cv2.destroyAllWindows()


def combinar_segmentos(imagem):
    """
    @brief Recombina os canais de uma imagem separada e exibe o resultado.

    @details
    Esta função recebe uma imagem, separa seus canais (azul, verde, vermelho),
    e depois os recombina em uma imagem única com cv2.merge(). Em seguida, a imagem
    recombinada é exibida em uma janela até que o usuário pressione uma tecla.

    @param imagem: Imagem carregada a ser recombinada.
    @return Nenhum valor é retornado.
    """

    # Verifica se a imagem foi carregada corretamente
    if imagem is None:
        print("Erro: imagem não encontrada ou não pôde ser carregada.")
        exit()

    # Segmenta os canais da imagem
    azul, verde, vermelho = cv2.split(imagem)

    # Recombina os canais em uma única imagem
    imagem = cv2.merge((azul, verde, vermelho))

    # Exibe a imagem recombinada
    cv2.imshow("Imagem recombinada", imagem)

    # Aguarda até que o usuário pressione uma tecla
    cv2.waitKey(0)

    # Fecha todas as janelas
    cv2.destroyAllWindows()

def converter_para_cinza(imagem):
    """
    @brief Converte uma imagem colorida para tons de cinza usando OpenCV.

    @details
    Esta função recebe uma imagem colorida no formato RGB e a converte para uma
    imagem em escala de cinza usando a função cv2.cvtColor(). A imagem convertida
    é então exibida em uma janela de visualização até que o usuário pressione
    uma tecla.

    A conversão para tons de cinza reduz a imagem de três canais (RGB) para um
    único canal de intensidade luminosa, facilitando análises de contraste, 
    segmentação e outras operações em visão computacional.

    @param imagem: Imagem colorida no formato RGB.

    @return Nenhum valor é retornado.
    """

    # Converte a imagem de RGB para escala de cinza
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Exibe a imagem em tons de cinza
    cv2.imshow("Escala de Cinza", imagem)

    # Aguarda uma tecla para continuar
    cv2.waitKey(0)

    # Fecha todas as janelas abertas
    cv2.destroyAllWindows()

def segmentar_hsv(imagem):
    """
    @brief Segmenta uma imagem nos canais HSV (Matiz, Saturação e Valor).

    @details
    Esta função converte uma imagem do espaço de cores BGR (padrão OpenCV) para HSV,
    e separa seus três canais: Matiz (H), Saturação (S) e Valor (V). Cada canal é
    exibido separadamente em uma janela, permitindo a visualização isolada da tonalidade,
    da intensidade de cor e da luminosidade da imagem.

    Isso é útil para tarefas de filtragem de cores, segmentação e análise de componentes
    cromáticos em visão computacional.

    @param imagem: Imagem no formato BGR a ser convertida e segmentada.

    @return Nenhum valor é retornado.
    """

    # Converte a imagem de BGR para HSV (Hue, Saturation, Value)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Separa os três canais da imagem HSV
    matiz, saturação, valor = cv2.split(imagem)

    # Exibe cada canal separadamente
    cv2.imshow("Canal H", matiz)        # Matiz: tipo da cor (0–179)
    cv2.imshow("Canal S", saturação)    # Saturação: intensidade da cor (0–255)
    cv2.imshow("Canal V", valor)        # Valor: brilho/luminosidade (0–255)

    # Aguarda o pressionamento de uma tecla
    cv2.waitKey(0)

    # Fecha todas as janelas abertas
    cv2.destroyAllWindows()

def combinar_segmentos_hsv(imagem):
    """
    @brief Exibe os canais HSV separadamente e recombina a imagem.

    @details
    Esta função recebe uma imagem no formato BGR (padrão OpenCV), converte-a para
    o espaço de cores HSV e separa os canais de Matiz (H), Saturação (S) e Valor (V).
    Após exibir os canais individualmente, a função recombina os canais com
    cv2.merge() e converte novamente para o espaço BGR para exibição final da imagem
    recomposta.

    Esta função é útil para visualizar e verificar o efeito de separar e combinar canais
    no espaço HSV, e garante que a recombinação preserve as características visuais da imagem.

    @param imagem: Imagem colorida no formato BGR.

    @return Nenhum valor é retornado.
    """

    # Converte a imagem de BGR para HSV (Hue, Saturation, Value)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Separa os três canais HSV (matiz, saturação, valor)
    matiz, saturação, valor = cv2.split(imagem)

    # Exibe separadamente os canais HSV
    cv2.imshow("Canal H", matiz)        # Matiz: tonalidade da cor (0–179)
    cv2.imshow("Canal S", saturação)    # Saturação: intensidade da cor (0–255)
    cv2.imshow("Canal V", valor)        # Valor: brilho/luminosidade (0–255)

    # Recombina os canais HSV em uma imagem única
    imagem = cv2.merge((matiz, saturação, valor))

    # Converte de volta para BGR para exibir como imagem colorida
    imagem = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)

    # Exibe a imagem recombinada
    cv2.imshow("Imagem", imagem)

    # Espera o pressionamento de uma tecla
    cv2.waitKey(0)

    # Fecha todas as janelas
    cv2.destroyAllWindows()


# Chamada das funções
segmentar_imagem(imagem)
combinar_segmentos(imagem)
converter_para_cinza(imagem)
segmentar_hsv(imagem)
combinar_segmentos_hsv(imagem)