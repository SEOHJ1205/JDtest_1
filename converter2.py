from pathlib import Path as pt
from PIL import Image

src_f = pt("PinguinMeme.gif")
dst_f = pt(src_f).with_suffix('.webp')

quali = {'quality': 100}

Image.open(src_f).save(dst_f, 'webp', **quali, save_all=True)
