# Projeto de Redução de Dimensionalidade em Imagens

Este projeto demonstra como ler uma imagem colorida no formato JPG, convertê-la para tons de cinza e para uma imagem binária, e salvar as imagens resultantes no formato JPG utilizando a biblioteca Pillow.

## Estrutura do Repositório

```
├── README.md
└── input
    ├── lena.jpg
└── output
    ├── grayscale_image.jpg
    └── binary_image.jpg
└── main.py
```

## Pré-requisitos

Certifique-se de ter o Python instalado e a biblioteca Pillow. Você pode instalar a biblioteca Pillow utilizando o pip:

```python
pip install pillow
```

## Descrição do Código

O código é composto pelas seguintes funções:

- **convert_to_grayscale(image):** Converte uma imagem colorida para tons de cinza.

- **convert_to_binary(image, threshold=128):** Converte uma imagem em tons de cinza para uma imagem binária usando um limiar (threshold) especificado.

- **main():** Função principal que lê a imagem colorida, aplica as conversões e salva as imagens resultantes na pasta output.

## Código

Aqui está o código completo (**main.py**):

```python
import os
from PIL import Image


def convert_to_grayscale(image):
   return image.convert("L")


def convert_to_binary(image, threshold=128):
   binary_image = image.point(lambda p: p > threshold and 255)
   return binary_image.convert("1")


def main():
   output_dir = 'output'
   os.makedirs(output_dir, exist_ok=True)

   input_image_path = r'input\lena.jpg'  # Substitua pelo caminho da sua imagem

   image = Image.open(input_image_path)

   grayscale_image = convert_to_grayscale(image)
   grayscale_image.save(os.path.join(output_dir, 'grayscale_image.jpg'))

   binary_image = convert_to_binary(grayscale_image)
   binary_image.save(os.path.join(output_dir, 'binary_image.jpg'))

   print("Imagens salvas na pasta 'output'.")


if __name__ == '__main__':
   main()
```

## Como Executar

1. Coloque a imagem que você deseja processar no diretório do projeto com o nome **input**.

2. Execute o script **main.py** no seu terminal:

```
python main.py
```

3. As imagens convertidas serão salvas na pasta output com os nomes **grayscale_image.jpg** e **binary_image.jpg**.

## Observações

- Certifique-se de substituir **r'input\lena.jpg'** pelo caminho real da sua imagem de entrada, caso esteja usando um arquivo diferente.

- O projeto utiliza a biblioteca **Pillow** para manipulação de imagens, que é uma biblioteca poderosa e amplamente utilizada para esse propósito.

## Contribuição <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" />

Sinta-se à vontade para contribuir com este projeto. Você pode abrir issues para relatar problemas ou fazer pull requests para melhorias.
