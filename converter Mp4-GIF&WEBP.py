from pathlib import Path as pt
from PIL import Image
import imageio
import os

clip = os.path.abspath('PinguinMeme.mp4')


def gifConverter(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame {frames}')
    print('Gif Done!')
    writer.close()


gifConverter(clip, '.gif')

src_f = pt(clip.strip(".mp4")+'.gif')
dst_f = pt(src_f).with_suffix('.webp')

quali = {'quality': 90} 

Image.open(src_f).save(dst_f, 'webp', **quali, save_all=True)
print('Webp Done!')
