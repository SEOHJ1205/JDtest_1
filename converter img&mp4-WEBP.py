from pathlib import Path
from PIL import Image
import imageio
import os
from glob import glob

# pip install imageio
# pip install PIL

## MP4 -> GIF
def gifConverter(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath) #데이터 및 메타데이터를 읽는 reader 개체
    fps = reader.get_meta_data()['fps'] # 메타데이터에서 FPS 
    writer = imageio.get_writer(outputPath, fps=fps) #데이터 및 메타 데이터를 사용할 수 있는 개체를 반환

    for frames in reader:
        writer.append_data(frames)
    writer.close()
    return outputPath



if __name__ == '__main__':
    folder_path = '' # 경로 입력
    assert os.path.isdir(folder_path), '폴더가 존재하지 않습니다.'
    files = glob(os.path.join(folder_path, '*'))
    
    for file in files:
        path = Path(os.path.abspath(file))
        ext = os.path.splitext(os.path.basename(path))[-1].replace('.', '')

        # MP4 파일이라면 gifConverter에서 GIF로 
        if ext.lower() == 'mp4':
            path = Path(gifConverter(path, '.gif')) # gifConverter의 inputPath, targetFormat
            

        destination = path.with_suffix(".webp")
        image = Image.open(path)  # Open image
        quali = {'quality': 90}
        image.save(destination, format="webp", **quali, save_all=True)

