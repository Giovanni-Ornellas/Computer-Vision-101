import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

imagem_rgb = cv2.imread("data/raw/first_image.jpg")

def exibir_estrutura_bgr(imagem):
    """
    @brief Gera um cubo 3D que representa a estrutura de uma imagem BGR.

    @details
    Essa função cria uma visualização em 3D com base nas dimensões da imagem:
        - Eixo X: largura (colunas)
        - Eixo Y: altura (linhas)
        - Eixo Z: canais de cor (B, G, R)

    Cada ponto representado indica a existência de um valor de pixel em determinado
    canal e posição espacial da imagem.

    """

    altura, largura, canais = imagem.shape

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Cria coordenadas para o cubo de dados
    x = np.repeat(np.arange(largura), altura * canais)
    y = np.tile(np.repeat(np.arange(altura), canais), largura)
    z = np.tile(np.arange(canais), largura * altura)

    # Gera as cores para o eixo Z (canal)
    canal_cores = ['b', 'g', 'r']
    cores = [canal_cores[i % 3] for i in z]

    ax.scatter(x, y, z, c=cores, marker='s', alpha=0.3)

    ax.set_xlabel('Largura (X)')
    ax.set_ylabel('Altura (Y)')
    ax.set_zlabel('Canais (Z)')
    ax.set_zticks([0, 1, 2])
    ax.set_zticklabels(['B', 'G', 'R'])
    ax.set_title('Estrutura 3D da Imagem BGR')

    plt.show()

exibir_estrutura_bgr(imagem_rgb)