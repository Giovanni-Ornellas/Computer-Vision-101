import cv2

imagem = cv2.imread("data/raw/third_image.jpeg")
imagem = cv2.resize(imagem, (0, 0), fx=0.6, fy=0.6)

def filtro_de_média(imagem):
    """
    @brief Aplica um filtro de média (blur) à imagem.

    @details
    Esta função aplica um filtro de média utilizando a função `cv2.blur()` com
    um kernel de tamanho 5x5. Esse tipo de filtro é usado para suavizar a imagem,
    reduzindo ruídos e variações bruscas de intensidade. Ele substitui cada pixel
    pelo valor médio de seus vizinhos dentro da janela definida.

    O efeito resultante é uma imagem mais “borrada” ou suavizada.

    @param imagem: Imagem original (colorida ou em escala de cinza) carregada como NumPy array.

    @return Nenhum valor é retornado. A imagem original e a tratada são exibidas em janelas separadas.
    """

    # Aplica o filtro de média com kernel 5x5
    imagem_tratada = cv2.blur(imagem, (5, 5))

    # Exibe a imagem original e a imagem tratada
    cv2.imshow("Original", imagem)
    cv2.imshow("Tratada", imagem_tratada)

    # Espera por uma tecla e fecha as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def filtro_gaussiano(imagem):
    """
    @brief Aplica um filtro Gaussiano à imagem para suavização.

    @details
    Esta função utiliza `cv2.GaussianBlur()` para aplicar um filtro de desfoque
    baseado em uma distribuição gaussiana. Diferente do filtro de média simples,
    o filtro gaussiano dá mais peso aos pixels centrais e menos aos vizinhos distantes,
    preservando melhor as bordas.

    O kernel utilizado é de tamanho (5,5), e o desvio padrão (sigma) é definido como 0,
    o que faz com que o OpenCV o calcule automaticamente com base no tamanho do kernel.

    Este filtro é muito eficaz para remoção de ruídos leves e preparação para detecção
    de bordas, contornos e outras operações de pré-processamento.

    @param imagem: Imagem de entrada (colorida ou em escala de cinza), carregada como array NumPy.

    @return Nenhum valor é retornado. A imagem original e a filtrada são exibidas em janelas.
    """

    # Aplica o filtro Gaussiano com kernel 5x5 e sigma automático
    imagem_tratada = cv2.GaussianBlur(imagem, (5, 5), 0)

    # Exibe a imagem original e a imagem suavizada
    cv2.imshow("Original", imagem)
    cv2.imshow("Tratada", imagem_tratada)

    # Aguarda uma tecla e fecha as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def filtro_de_mediana(imagem):
    """
    @brief Aplica um filtro de mediana à imagem para remoção de ruído.

    @details
    Esta função aplica o filtro de mediana com kernel de tamanho 3 utilizando
    `cv2.medianBlur()`. O filtro de mediana substitui cada pixel pelo valor
    mediano dos pixels vizinhos dentro da janela especificada. É especialmente
    eficaz para remoção de ruídos do tipo "sal e pimenta" (pixels pretos ou brancos isolados).

    Como o filtro preserva melhor as bordas em comparação com os filtros de média e Gaussiano,
    é amplamente utilizado em pré-processamento para segmentação e análise de contornos.

    @param imagem: Imagem de entrada (colorida ou em escala de cinza) carregada como array NumPy.

    @return Nenhum valor é retornado. A imagem original e a tratada são exibidas em janelas separadas.
    """

    # Aplica o filtro de mediana com kernel 3x3
    imagem_tratada = cv2.medianBlur(imagem, 3)

    # Exibe a imagem original e a imagem suavizada
    cv2.imshow("Original", imagem)
    cv2.imshow("Tratada", imagem_tratada)

    # Aguarda uma tecla e fecha as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def filtro_bilateral(imagem):
    imagem_tratada = cv2.bilateralFilter(imagem, 8,10,10)

    # Exibe a imagem original e a imagem suavizada
    cv2.imshow("Original", imagem)
    cv2.imshow("Tratada", imagem_tratada)

    # Aguarda uma tecla e fecha as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    filtro_de_média(imagem)
    filtro_gaussiano(imagem)
    filtro_de_mediana(imagem)
    filtro_bilateral(imagem)

if __name__ == "__main__":
    main()