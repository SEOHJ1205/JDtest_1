from pathlib import Path
from PIL import Image
import imageio
import os

def gifConverter(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
    writer.close()
    return outputPath


if __name__ == '__main__':
    path = Path(os.path.abspath('')) # path!! 
    ext = os.path.splitext(os.path.basename(path))[-1].replace('.', '')

    if ext.lower() == 'mp4':
        path = Path(gifConverter(path, '.gif'))

    destination = path.with_suffix(".webp")
    image = Image.open(path)  # Open image
    quali = {'quality': 90}
    image.save(destination, format="webp", **quali, save_all=True)

