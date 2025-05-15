import cv2

imagem = cv2.imread("data/raw/eighth_image.jpg")
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
    imagem_realçada = cv2.Laplacian(imagem, cv2.CV_8U)
    imagem_aguçada  = cv2.subtract(imagem, imagem_realçada)

    # Exibe as imagens
    cv2.imshow("Original", imagem)
    cv2.imshow("Realçada", imagem_realçada)
    cv2.imshow("Aguçada", imagem_aguçada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    operador_sobel(imagem)
    operador_laplaciano(imagem)
    aguçamento_de_borda(imagem)
 

if __name__ == "__main__":
    main()