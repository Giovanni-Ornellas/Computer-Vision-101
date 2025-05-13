import cv2
import numpy as np
import matplotlib.pyplot as plt

def processar_imagem_pb_antiga(caminho_entrada, caminho_saida):
    """
    @brief Processa uma imagem preto e branco: equaliza, colore (HSV) e converte para RGB.

    @param caminho_entrada: Caminho da imagem preto e branco (grayscale).
    @param caminho_saida: Caminho para salvar a imagem colorizada.
    """

    # 1. Carrega a imagem em escala de cinza
    imagem_pb = cv2.imread(caminho_entrada, 0)
    imagem_pb = cv2.resize(imagem_pb, (0, 0), fx=0.6, fy=0.6)
    if imagem_pb is None:
        print("❌ Erro ao carregar a imagem.")
        return

    # 2. Equaliza o histograma (melhora contraste)
    imagem_eq = cv2.equalizeHist(imagem_pb)

    # 3. Converte para HSV artificial
    # Explicação: canal H define a cor, vamos "pintar" esse canal
    h = np.full_like(imagem_eq, 15)  # tom de laranja (H varia de 0 a 179)
    s = cv2.normalize(imagem_eq, None, alpha=100, beta=255, norm_type=cv2.NORM_MINMAX)
    v = imagem_eq.copy()

    imagem_hsv = cv2.merge((h, s, v))

    # 4. Converte para BGR (para visualização/salvamento no OpenCV)
    imagem_colorida = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)

    # 5. Exibe os resultados
    cv2.imshow("Original PB", imagem_pb)
    cv2.imshow("Equalizada", imagem_eq)
    cv2.imshow("Colorizada (HSV->BGR)", imagem_colorida)

    # 6. Salva o resultado
    cv2.imwrite(caminho_saida, imagem_colorida)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 🔧 Caminhos
entrada = "data/raw/third_image.jpeg"
saida = "data/processed/foto_colorizada.jpeg"

# 🚀 Executa
processar_imagem_pb_antiga(entrada, saida)
