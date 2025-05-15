import cv2

imagem = cv2.imread("data/raw/fourth_image.jpg")  


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

    # 2. Converte para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # 3. Aplica threshold para obter imagem binária (preto e branco)
    _, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

    # 4. Salva a imagem binária como BMP
    cv2.imwrite("data/processed/Nova.bmp", imagem_binaria)

    # 5. Mostra a imagem binária
    cv2.imshow("Imagem binária (preto e branco)", imagem_binaria)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def erosão(imagem):
    pass


def main():
    converter_para_bmp(imagem)

if __name__ == "__main__":
    main()