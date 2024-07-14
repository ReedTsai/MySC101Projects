"""
File: blur.py
Name: DK
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    This program can blur the smile image with the number of runs by users input.
    """
    """
    These code are referenced from SC001 Assignment4 jerry's code.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()  # shows the initial image
    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()  # shows the final blurred image


def blur(img):
    """
    :param img: image, input image which will be blurred.
    :return: image, the blurred image after one time blurring.
    """
    blurred_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2):  # to average the pixel around the target pixel
                for j in range(-1, 2):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_pixel = blurred_img.get_pixel(x, y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return blurred_img


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
