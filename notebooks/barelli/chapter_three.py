# Importa a biblioteca do OpenCV
import	cv2

def carrega_imagem():
    """
    @brief Carrega e exibe uma imagem usando OpenCV.

    Esta função carrega uma imagem de um caminho fixo e a exibe em uma janela do sistema
    operacional com o título escolhido. A função utiliza OpenCV para leitura e exibição.

    @details
    Este método não funciona corretamente dentro de notebooks Jupyter (.ipynb), pois o 
    método cv2.imshow() requer uma interface gráfica nativa. Em ambientes como Jupyter, 
    deve-se usar matplotlib para exibir a imagem inline.

    @note
    É necessário pressionar qualquer tecla para fechar a janela de exibição.

    @return Nenhum valor é retornado.
    """
    # Carrega a imagem do caminho especificado
    imagem = cv2.imread("data/raw/first_image.jpg")

    # Exibe a imagem em uma janela com o título "Pinquim"
    cv2.imshow("Pinquim", imagem)

    # Aguarda indefinidamente até que o usuário pressione uma tecla
    cv2.waitKey(0)

    # Fecha todas as janelas abertas do OpenCV
    cv2.destroyAllWindows()

def reproduzir_video():
    """
    @brief Reproduz um vídeo quadro a quadro usando OpenCV.

    @details
    Esta função abre um arquivo de vídeo e exibe seus quadros continuamente
    em uma janela de sistema, como um player. A reprodução continua até que 
    o usuário pressione a tecla 'q'. Cada quadro é exibido com um pequeno 
    atraso de 1 milissegundo. Ideal para testes locais com arquivos de vídeo.
    
    O caminho do vídeo é fixo como "data/raw/first_video.mp4", mas também pode 
    ser usado para ler uma webcam mudando o caminho para um inteiro.

    @note
    Este código só funciona corretamente fora de ambientes como Jupyter Notebook,
    pois depende da exibição em janelas nativas do sistema operacional.

    @return Nada é retornado.
    """

    # Cria o objeto de captura para ler o vídeo
    captura = cv2.VideoCapture("data/raw/first_video.mp4")

    # Loop para ler e exibir cada quadro
    while True:
        ret, frame = captura.read()  # Lê o próximo quadro
        if not ret:
            break  # Sai do loop se o vídeo acabar ou houver erro

        cv2.imshow("Imagem", frame)  # Exibe o quadro

        # Espera 1ms por uma tecla e verifica se é 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Libera o recurso de vídeo e fecha as janelas
    captura.release()
    cv2.destroyAllWindows()


