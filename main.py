from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        pixel_value = min(max(pixel_value, 0), 255)
        ascii_index = int((pixel_value / 255) * (len(ascii_chars) - 1))
        ascii_str += ascii_chars[ascii_index]
    return ascii_str

def image_to_ascii(image_path, output_path, new_width=100, resolution_multiplier=1):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    new_width *= resolution_multiplier

    image = resize_image(image, new_width=new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    aspect_ratio = image.height / image.width
    ascii_str = "\n".join(
        [ascii_str[i : i + new_width] for i in range(0, len(ascii_str), new_width)]
    )

    with open(output_path, "w") as output_file:
        output_file.write(ascii_str)

if __name__ == "__main__":
    input_image_path = r"YOUR_FILE_PATH.jpg"
    output_text_path = "OUTPUT_PATH.txt"
    new_width = 100
    resolution_multiplier = 2

    image_to_ascii(
        input_image_path, output_text_path, new_width, resolution_multiplier
    )
    print(f"Image converted to ASCII art and saved in {output_text_path}")
