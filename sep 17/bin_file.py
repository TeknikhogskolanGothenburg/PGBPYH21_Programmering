def main():
    with open('image.gif', 'rb') as image_file:
        # image_file.seek(13)
        # for color in range(256):
        #     r = image_file.read(1)
        #     g = image_file.read(1)
        #     b = image_file.read(1)
        #     print(color, r.hex(), g.hex(), b.hex())
        with open('image2.gif', 'wb') as image_copy:
            data = image_file.read(19)
            image_copy.write(data)

            image_copy.write(bytearray([255, 0, 0]))
            image_file.seek(22, 0)

            data = image_file.read()
            image_copy.write(data)


if __name__ == '__main__':
    main()
