from formats.png import _PNG
from formats.bmp import _BMP
from formats.ppm import _PPM


class _CONVERTER:
    def start(self):
        print('Input source and goal format\nExample: --source=example.bmp --goal-format=ppm --output=result.ppm')
        user_input = input()
        source = ''
        source_format = ''
        output_directory = ''
        try:
            source = user_input.split()[0][9:]
            source_format = source.split('.')[-1]
            goal_format = user_input.split()[1][14:]
            if goal_format != 'ppm':
                print('Unsupported goal file format. Try again')
                self.start()
            output_directory = source.split('.')[0] + '.ppm'
            if 'output' in user_input:
                output_directory = user_input.split()[2][9:]
        except:
            print('Invalid input data. Make sure you adhere to the input format described.')
            self.start()

        if source_format == 'png':
            try:
                _png_converter = _PNG()
                _ppm_converter = _PPM()
                _png_image = _png_converter.read(source)
                _to_P3 = _ppm_converter.write_from_png(_png_image, output_directory)
            except FileNotFoundError:
                print("Couldn't find the .png file specified. Try again.")
                self.start()
        elif source_format == 'bmp':
            try:
                _bmp_converter = _BMP()
                _ppm_converter = _PPM()
                _bmp_image = _bmp_converter.read(source)
                _to_P3 = _ppm_converter.write_from_bmp(_bmp_image, output_directory)
            except FileNotFoundError:
                print("Couldn't find the .bmp file specified. Try again.")
                self.start()
        else:
            print('Unsupported source format. Try again')
            self.start()
