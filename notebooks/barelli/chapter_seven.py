import cv2

imagem = cv2.imread("data/raw/fifth_image.jpg",0)
imagem = cv2.resize(imagem, (0, 0), fx=1, fy=1)

def operador_sobel(imagem):
    """
    @brief Aplica o operador de Sobel para detecção de bordas nas direções X e Y.

    @details
    Esta função aplica o operador de Sobel nas direções horizontal (X) e vertical (Y)
    com kernel de tamanho 9. O operador de Sobel realça regiões com variação de intensidade,
    sendo útil para detecção de bordas e contornos.

    O parâmetro `cv2.CV_8U` define o tipo de saída como imagem de 8 bits por canal.

    @param imagem: Imagem de entrada em escala de cinza (recomendado), como array NumPy.

    @return Nenhum valor é retornado. As imagens de borda em X e Y são exibidas separadamente.
    """

    # Aplica o operador de Sobel na direção X (horizontal)
    sobel_x = cv2.Sobel(imagem, cv2.CV_8U, 1, 0, ksize=3)

    # Aplica o operador de Sobel na direção Y (vertical)
    sobel_y = cv2.Sobel(imagem, cv2.CV_8U, 0, 1, ksize=3)

    # Exibe a imagem original e os resultados do filtro de Sobel
    cv2.imshow("Original", imagem)
    cv2.imshow("Sobel X", sobel_x)
    cv2.imshow("Sobel Y", sobel_y)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def operador_laplaciano(imagem):
    """
    @brief Aplica o operador de Laplaciano à imagem para realce de bordas.

    @details
    Esta função aplica o operador de Laplace usando `cv2.Laplacian()` para detectar bordas 
    na imagem com base na segunda derivada. O resultado realça regiões onde há mudanças 
    rápidas de intensidade, como contornos e arestas.

    Ao contrário do Sobel, que usa primeira derivada e direção (X ou Y), o Laplaciano 
    é **isotrópico** e detecta bordas em todas as direções simultaneamente.

    O tipo de saída é `cv2.CV_8U`, que retorna imagem em 8 bits (valores de 0 a 255).

    @param imagem: Imagem de entrada, preferencialmente em escala de cinza (NumPy array).

    @return Nenhum valor é retornado. A imagem original e a com bordas são exibidas na tela.
    """

    # Aplica o operador de Laplaciano
    imagem_tratada = cv2.Laplacian(imagem, cv2.CV_8U)

    # Exibe as imagens
    cv2.imshow("Original", imagem)
    cv2.imshow("Tratada", imagem_tratada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def aguçamento_de_borda(imagem):
    """
    @brief Aplica aguçamento de bordas utilizando o operador Laplaciano.

    @details
    Esta função realça os contornos da imagem original aplicando o operador 
    Laplaciano para detectar bordas e, em seguida, subtrai a imagem de bordas 
    da imagem original para gerar uma versão aguçada (realçada).

    Esse processo funciona como uma técnica de realce, pois preserva as 
    informações de alta frequência (bordas) da imagem, aumentando o contraste 
    entre regiões.

    A função exibe três janelas:
      - "Original": a imagem de entrada.
      - "Realçada": o resultado do filtro Laplaciano (bordas).
      - "Aguçada": imagem final com realce de bordas.

    @param imagem: Imagem de entrada em tons de cinza (np.ndarray).
    @return Nenhum valor é retornado. As imagens são exibidas em janelas.
    """
    imagem_realçada = cv2.Laplacian(imagem, cv2.CV_8U)
    imagem_aguçada  = cv2.subtract(imagem, imagem_realçada)

    # Exibe as imagens
    cv2.imshow("Original", imagem)
    cv2.imshow("Realçada", imagem_realçada)
    cv2.imshow("Aguçada", imagem_aguçada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def desaguçamento(imagem):
    """
    @brief Realça os detalhes de uma imagem utilizando o filtro de desaguçamento (unsharp mask).

    @details
    Essa técnica visa melhorar os contornos e bordas da imagem, realçando os detalhes
    de alta frequência. O processo é baseado na criação de uma "máscara de detalhes",
    que é obtida subtraindo a versão suavizada da imagem original.

    A sequência de etapas é a seguinte:
    1. Aplica um filtro gaussiano para suavizar a imagem (remoção de ruídos e detalhes finos).
    2. Subtrai a imagem suavizada da original para extrair apenas os detalhes (bordas).
    3. Multiplica a máscara de detalhes por um fator de intensidade (aqui, 3×).
    4. Soma os detalhes realçados de volta à imagem original, gerando uma imagem com bordas mais nítidas.

    A função exibe quatro janelas:
      - "Original": imagem de entrada.
      - "Suavizada": imagem borrada com filtro gaussiano.
      - "Detalhes": máscara de detalhes (alta frequência).
      - "Realçada": imagem final com realce aplicado.

    @param imagem: Imagem original (np.ndarray), preferencialmente em escala de cinza.
    @return Nenhum valor é retornado. As imagens são exibidas na tela.
    """
    imagem_suavizada = cv2.GaussianBlur(imagem, (13,13), 3)
    imagem_detalhes  = 3 * cv2.subtract(imagem, imagem_suavizada)
    imagem_realçada  = cv2.add(imagem, imagem_detalhes)

    # Exibe as imagens
    cv2.imshow("Original", imagem)
    cv2.imshow("Suavizada", imagem_suavizada)
    cv2.imshow("Detalhes", imagem_detalhes)
    cv2.imshow("Realçada", imagem_realçada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def canny(imagem):
    """
    @brief Aplica o detector de bordas de Canny em uma imagem.

    @details
    O algoritmo de Canny é um dos mais utilizados para detecção de bordas. Ele identifica
    regiões de transição brusca de intensidade (bordas) na imagem, utilizando operações
    de gradiente. Esta implementação usa limiares de histerese fixos:
      - Limiar inferior: 100
      - Limiar superior: 200

    A imagem resultante é binária (preto e branco), onde os pixels brancos representam bordas.

    A função exibe duas janelas:
      - "Original": imagem de entrada.
      - "Tratada": imagem com as bordas detectadas pelo Canny.

    @param imagem: Imagem de entrada (np.ndarray), preferencialmente em tons de cinza.
    @return Nenhum valor é retornado. As imagens são exibidas na tela.
    """
    imagem_tratada = cv2.Canny(imagem, 100, 200)

    cv2.imshow("Original", imagem)
    cv2.imshow("Tratada", imagem_tratada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



def main():
    operador_sobel(imagem)
    operador_laplaciano(imagem)
    aguçamento_de_borda(imagem)
    desaguçamento(imagem)
    canny(imagem)
 

if __name__ == "__main__":
    main()