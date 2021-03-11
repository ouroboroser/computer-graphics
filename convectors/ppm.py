from convectors.image import _IMAGE

class _PPM:
    def __init__(self, name):
        self.name = name

    def read(self, name):
        with open(name, 'rb') as ppm_file:
            return [row for row in ppm_file.readlines()]

    def clean(self, input_img):
        output_img = []
        for row in input_img:
            output_img.append(row.decode())
        for row in output_img:
            if ('#' in row) == True:
                output_img.remove(row)
        return  output_img
