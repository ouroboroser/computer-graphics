from formats.png import _PNG
from formats.bmp import _BMP
from formats.ppm import _PPM


class _CONVERTER:

    def start(self):
        print('Input image path: ')
        img = input()
        try:
            img_format = img.split('.')[-1]
        except:
            print('Invalid input data. Try again.')
            self.start()

        if img_format == 'png':
            try:
                _png_converter = _PNG()
                _ppm_converter = _PPM()
                _png_image = _png_converter.read(img)
                _to_P3 = _ppm_converter.write_from_png(_png_image)
            except FileNotFoundError:
                print("Couldn't find the .png file specified. Try again.")
                self.start()
        elif img_format == 'bmp':
            try:
                _bmp_converter = _BMP()
                _ppm_converter = _PPM()
                _bmp_image = _bmp_converter.read(img)
                _to_P3 = _ppm_converter.write_from_bmp(_bmp_image)
            except FileNotFoundError:
                print("Couldn't find the .bmp file specified. Try again.")
                self.start()
        else:
            print('Unsupported file format. Try again')
            self.start()
