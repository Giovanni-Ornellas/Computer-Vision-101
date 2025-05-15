import cv2
import numpy as np

imagem = cv2.imread("data/raw/nineth_image.png",0)
imagem = cv2.resize(imagem, (0, 0), fx=0.5, fy=0.5)

import cv2

def converter_para_bmp_binaria(limiar=127):
    """
    Converte uma imagem para formato BMP binário (preto e branco).
    
    Parâmetros:
        caminho_entrada (str): Caminho da imagem de entrada.
        caminho_saida (str): Caminho onde a imagem binária será salva.
        limiar (int): Valor de limiar para binarização (padrão: 127).
    """
    # Carrega a imagem em escala de cinza
    imagem_cinza = cv2.imread("data/raw/nineth_image.png", cv2.IMREAD_GRAYSCALE)

    # Verifica se a imagem foi carregada
    if imagem_cinza is None:
        raise FileNotFoundError("Imagem de entrada não encontrada.")

    # Aplica a binarização
    _, imagem_binaria = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

    # Salva no formato BMP
    cv2.imwrite("data/processed/Caneca-PretaBranca.bmp", imagem_binaria)




def erosão():
    imagem = cv2.imread("data/processed/Caneca-PretaBranca.bmp",0)
    elemento_estruturante = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (5,5)
    )
    imagem_processada = cv2.erode(
        imagem, elemento_estruturante, iterations = 5
    )

    # Exibe as imagens
    cv2.imshow("Original", imagem)
    cv2.imshow("Tratada", imagem_processada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
   erosão()

if __name__ == "__main__":
    main()