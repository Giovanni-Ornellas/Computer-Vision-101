# Computer Vision 101 📸🧠

Este repositório tem como objetivo explorar e estudar técnicas de **visão computacional** usando **Python**. Aqui serão implementados algoritmos clássicos e modernos, passando por pré-processamento, detecção de objetos, classificação de imagens e aplicações com redes neurais profundas (CNNs, YOLO, Vision Transformers etc.).

O foco é **aprender fazendo**, com uma estrutura organizada e escalável, como em projetos reais de machine learning.

---

## 🧭 Estrutura do Projeto

```bash
visao-computacional/
├── data/                    # Dados brutos e processados
│   ├── raw/                # Dados originais (não modificados)
│   ├── processed/          # Dados tratados (redimensionados, normalizados, etc.)
│   └── annotations/        # Labels, bounding boxes, segmentações, etc.
│
├── notebooks/              # Notebooks Jupyter para testes exploratórios
│
├── src/                    # Código-fonte organizado em módulos
│   ├── datasets/           # Scripts de carregamento e parsing de datasets
│   ├── preprocessing/      # Funções de tratamento de imagem
│   ├── models/             # Arquivos de definição e uso de modelos
│   ├── inference/          # Scripts para realizar inferência com os modelos
│   └── utils/              # Funções auxiliares reutilizáveis (ex: visualização)
│
├── experiments/            # Resultados de execuções e testes
│
├── tests/                  # Testes unitários para garantir funcionamento correto
│
├── configs/                # Arquivos de configuração para treinos e modelos
│
├── docs/                   # Documentação técnica adicional
│
├── requirements.txt        # Lista de dependências do projeto
├── .gitignore              # Arquivos e pastas ignorados pelo Git
└── README.md               # Este arquivo :)

