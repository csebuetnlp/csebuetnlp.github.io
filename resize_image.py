from PIL import Image
import glob
import os

def resize_images(input_dir, output_dir, target_width=500, target_height=500):
    os.makedirs(output_dir, exist_ok=True)
    iterator = os.path.join(input_dir, "*")
    
    for input_file in glob.glob(iterator):
        output_file = os.path.join(output_dir, os.path.basename(input_file))
        try:
            im = Image.open(input_file)
        except:
            continue
        im = im.resize((target_width, target_height))
        im.save(output_file)

if __name__ == "__main__":
    resize_images(
        "img_old/",
        "img/"
    )