import os

from PIL import Image


class Converter:
    
    def __init__(self):
        self.src = '../images/ships'
        self.dst = '../images/ships/'

    def main(self):
        self.pngs_to_bmp(self.src, self.dst)
    
    def pngs_to_bmp(self, src, dst):
        print(f'Src: {src}')
        print(f'Dst: {dst}')

        if not os.path.exists(dst):
            os.makedirs(dst)

        for file in os.listdir(src):
            if file.endswith('.png'):
                src_path = os.path.join(src, file)
                dst_path = os.path.join(dst, f'{os.path.splitext(file)[0]}.bmp')

                print(f'Src_path: {src_path}')
                print(f'Dst_path: {dst_path}')
                self.png_to_bmp(src_path, dst_path)

    @staticmethod
    def png_to_bmp(src_path, dst_path):
        try:
            png_image = Image.open(src_path)
            png_image.save(dst_path, format='BMP')
        except Exception as e:
            print(f'Err: {e}')


if __name__ == '__main__':
    converter = Converter()
    converter.main()
            