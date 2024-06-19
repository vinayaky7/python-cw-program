from PIL import Image

def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            print(f"Image size: {width} x {height} pixels")
    except IOError:
        print(f"Unable to open image file: {image_path}")

# Example usage:
if __name__ == "__main__":
    try:
        image_path = input("Enter the path to the image file: ")
        get_image_size(image_path)
    except Exception as e:
        print(f"Error: {e}")
