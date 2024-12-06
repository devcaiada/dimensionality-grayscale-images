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
