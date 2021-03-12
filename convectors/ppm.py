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

    def data(self, input_img):
        new_format = ' '.join(input_img)
        size = new_format.split()[1:3]
        size = list(map(int, size))

        pixels = new_format.split()[4:]
        pixels = list(map(int, pixels))
        chunks = [pixels[i:i + 3] for i in range(0, len(pixels), 3)]

        image_data = _IMAGE(
            size[0],
            size[1],
            chunks,
        )

        return image_data

    def write(self, img_data):
        format = 'P3 \n'
        size = str(img_data.width) + ' ' + str(img_data.height) + '\n'


        chunks = []
        for row in img_data.pixel_map:
            chunks += row

        _max = max(chunks)
        _max = str(_max) + '\n'

        s = ''

        new_arr = img_data.pixel_map

        new_arr.reverse()
        for chunk in new_arr:
            chunk = ' '.join([str(i) for i in chunk])
            s += chunk + '\n'

        for row in img_data.pixel_map:
            print(row)

        file = format + size + _max + s

        with open("converted.ppm", 'w+') as ppm_file:
            ppm_file.write(file)