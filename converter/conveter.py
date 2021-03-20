from formats.png import _PNG
from formats.bmp import _BMP
from formats.ppm import _PPM

class _CONVETER:

    def start(self):
        print('Input image name: ')
        img_name = input()
        img_name = img_name.split('.')[1]
        if img_name == 'png':
            _png_converter = _PNG()
            _ppm_converter = _PPM()
            _png_image = _png_converter.read(img_name)
            _to_P3 = _ppm_converter.write_from_png(_png_image)
        if img_name == 'bmp':
            _bmp_converter = _BMP()
            _bmp_image = _bmp_converter.read(img_name)
            _to_P3 = _ppm_converter.write_from_bmp(_bmp_image)