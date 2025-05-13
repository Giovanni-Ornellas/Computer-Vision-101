import cv2
import numpy as np

# Carrega a imagem no formato BGR
imagem_bgr = cv2.imread("data/raw/second_image.jpg")

# Verifica se a imagem foi carregada corretamente
if imagem_bgr is None:
    print("Erro ao carregar a imagem.")
    exit()

# Converte para RGB (para facilitar leitura humana)
imagem_rgb = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)

# Separa os canais (R, G, B)
R, G, B = cv2.split(imagem_rgb)

# Converte para escala de cinza
imagem_cinza = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2GRAY)

# Exibe as matrizes no terminal
print("=== Matriz do Canal Vermelho (R) ===")
print(R)

print("\n=== Matriz do Canal Verde (G) ===")
print(G)

print("\n=== Matriz do Canal Azul (B) ===")
print(B)

print("\n=== Matriz da Imagem em Escala de Cinza ===")
print(imagem_cinza)
