import os
import random as rnd

from PIL import Image, ImageFilter
Image.MAX_IMAGE_PIXELS = None
from trdg import computer_text_generator, background_generator, distorsion_generator
import uuid
from trdg.colorize3_poisson import FontColor
from trdg.font_utils import color_convert

import numpy as np
from trdg import handwritten_text_generator_v2
# try:
#     from trdg import handwritten_text_generator_v2
# except ImportError as e:
#     # print("Missing modules for handwritten text generation.")
#     pass


class FakeTextDataGenerator(object):
    @classmethod
    def generate_from_tuple(cls, t):
        """
            Same as generate, but takes all parameters as one tuple
        """

        cls.generate(*t)

    @classmethod
    def generate(
        cls,
        index,
        text,
        font,
        out_dir,
        size,
        extension,
        skewing_angle,
        random_skew,
        blur,
        random_blur,
        background_type,
        distorsion_type,
        distorsion_orientation,
        is_handwritten,
        name_format,
        width,
        alignment,
        text_color,
        orientation,
        space_width,
        character_spacing,
        margins,
        fit,
        output_mask,
        word_split,
        image_dir,
        prefix_name,
        colors_generator,
    ):

        # try:
            ### Background Image ###

            # If complex background
            if background_type == 1:

                bg_max_height = 64
                bg_max_width = 1500
                background_image = background_generator.image(bg_max_height, bg_max_width, image_dir)

                #Choose color
                # colors = ['#990028', '#E500AF', '#000000', '#4C4C4C']   # id
                # colors = ['#000000']  # text
                # text_color = rnd.choice(colors)

                # Gen color for text
                try:
                    text_color_rgb, bg_col = colors_generator.sample_from_data(background_image)
                except Exception as e :
                    print("Error load color: ", e)
                    return
                text_color_hex = "rgb(" + ",".join(str(item) for item in text_color_rgb) + ")"
                text_color = color_convert.rgb2hex(text_color_hex)

                # Choose rotate aug

                if rnd.random() < 0.2:   # 20% rot
                    random_skew = True
                    skewing_angle = 3
                else:
                    random_skew = False
                    skewing_angle = 0

                distor_rnd = rnd.random()
                if distor_rnd < 0.35:
                    distorsion_type = 3  # 0 (None), 1 (Sin), 2 (Cos), 3 (Random)
                    distorsion_orientation = 0  # 0 (up-down),1 (left-right) ,2 (both)
                elif 0.35 <= distor_rnd < 0.4:
                    distorsion_type = 3  # 0 (None), 1 (Sin), 2 (Cos), 3 (Random)
                    distorsion_orientation = 1  # 0 (up-down),1 (left-right) ,2 (both)
                elif 0.4 <= distor_rnd < 0.45:
                    distorsion_type = 1  # 0 (None), 1 (Sin), 2 (Cos), 3 (Random)
                    distorsion_orientation = 2  # 0 (up-down),1 (left-right) ,2 (both)
                else:
                    distorsion_type = 0
                    distorsion_orientation = 0

            else:
                ### Simple random background ###
                ##########################
                # Create picture of text #
                ##########################
                # 1 - white + black text, 3 - black  + white text , 4 - gray  + back/white text
                # "#282828" - black,              # or #FFFFFF : white   or #b0aeae : gray


                '''ROT'''
                if rnd.random() < 0.2:   # 20% rot
                    random_skew = True
                    skewing_angle = 3
                else:
                    random_skew = False
                    skewing_angle = 0

                '''DISTOR'''
                distor_rnd = rnd.random()
                if distor_rnd < 0.3:
                    distorsion_type = 3          # 0 (None), 1 (Sin), 2 (Cos), 3 (Random)
                    distorsion_orientation = 0   # 0 (up-down),1 (left-right) ,2 (both)
                elif 0.3 <= distor_rnd < 0.5:
                    distorsion_type = 3  # 0 (None), 1 (Sin), 2 (Cos), 3 (Random)
                    distorsion_orientation = 1  # 0 (up-down),1 (left-right) ,2 (both)
                elif 0.5 <= distor_rnd < 0.55:
                    distorsion_type = 1  # 0 (None), 1 (Sin), 2 (Cos), 3 (Random)
                    distorsion_orientation = 2  # 0 (up-down),1 (left-right) ,2 (both)
                else:
                    distorsion_type = 0
                    distorsion_orientation = 0



                '''BLUR'''
                if rnd.random() < 0.1:   # 10% blur
                    random_blur = True
                    blur = 1

                '''BACKGROUND COLOR '''
                if rnd.random() < 0.9:                 # 50% black color text
                    text_color = "#000000"
                    bg_prob = rnd.random()
                    if bg_prob < 0.1:                  # 20% white bg
                        background_type = 2
                    elif 0.1 <= bg_prob < 0.8:         # 20 % gauss bg
                        background_type = 0
                    else:
                        background_type = 5            # 40% gray
                else:                                  #
                    text_color = "#FFFFFF"            #
                    background_type = 4

            ### TEXT ###
            if 'UTM' in font:
                if rnd.random() < 0.5:
                    text = text.lower()
                else:
                    text = text[0].upper() + text[1:].lower()


            ''' RANDOM PADDING / FIT '''
            if rnd.random() < 0.5:
                if rnd.random() < 0.8:
                    fit = True
                    # margins = (5, rnd.randint(0, 10), 5, rnd.randint(5, 10))
                    margins = (rnd.randint(4, 10), rnd.randint(4, 20), rnd.randint(4, 10), rnd.randint(4, 20))   # top, left, bottom, right
                else:  # larger
                    margins = (rnd.randint(4, 10), rnd.randint(10, 30), rnd.randint(4, 10), rnd.randint(10, 30))   # top, left, bottom, right

            else:
                fit = True
                margin_rand = rnd.randint(0, 5)
                # margins = (1, 1, 1, 1)
                margins = [margin_rand] * 4

            margin_top, margin_left, margin_bottom, margin_right = margins
            horizontal_margin = margin_left + margin_right
            vertical_margin = margin_top + margin_bottom

            '''character space:'''
            # character_spacing = rnd.randint(0, 4)  # id

            character_spacing = rnd.randint(0, 1)  # text


            ##########################
            # Create picture of text #
            ##########################
            if is_handwritten:
                if orientation == 1:
                    raise ValueError("Vertical handwritten text is unavailable")
                image, mask = handwritten_text_generator_v2.generate(text, text_color)
            else:
                image, mask = computer_text_generator.generate(
                    text,
                    font,
                    text_color,
                    size,
                    orientation,
                    space_width,
                    character_spacing,
                    fit,
                    word_split,
                )
            random_angle = rnd.randint(0 - skewing_angle, skewing_angle)

            rotated_img = image.rotate(
                skewing_angle if not random_skew else random_angle, expand=1
            )

            rotated_mask = mask.rotate(
                skewing_angle if not random_skew else random_angle, expand=1
            )

            #############################
            # Apply distorsion to image #
            #############################
            if distorsion_type == 0:
                distorted_img = rotated_img  # Mind = blown
                # distorted_mask = rotated_mask
            elif distorsion_type == 1:
                distorted_img, distorted_mask = distorsion_generator.sin(
                    rotated_img,
                    rotated_mask,
                    vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                    horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
                )
            elif distorsion_type == 2:
                distorted_img, distorted_mask = distorsion_generator.cos(
                    rotated_img,
                    rotated_mask,
                    vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                    horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
                )
            else:
                distorted_img, distorted_mask = distorsion_generator.random(
                    rotated_img,
                    rotated_mask,
                    vertical=(distorsion_orientation == 0 or distorsion_orientation == 2),
                    horizontal=(distorsion_orientation == 1 or distorsion_orientation == 2),
                )

            ##################################
            # Resize image to desired format #
            ##################################
            # Horizontal text
            if orientation == 0:
                new_width = int(
                    distorted_img.size[0]
                    * (float(size - vertical_margin) / float(distorted_img.size[1]))
                )
                resized_img = distorted_img.resize(
                    (new_width, size - vertical_margin), Image.ANTIALIAS
                )
                # resized_mask = distorted_mask.resize((new_width, size - vertical_margin), Image.NEAREST)
                background_width = width if width > 0 else new_width + horizontal_margin
                background_height = size
            # Vertical text
            elif orientation == 1:
                new_height = int(
                    float(distorted_img.size[1])
                    * (float(size - horizontal_margin) / float(distorted_img.size[0]))
                )
                resized_img = distorted_img.resize(
                    (size - horizontal_margin, new_height), Image.ANTIALIAS
                )
                # resized_mask = distorted_mask.resize(
                #     (size - horizontal_margin, new_height), Image.NEAREST
                # )
                background_width = size
                background_height = new_height + vertical_margin
            else:
                raise ValueError("Invalid orientation")

            #############################
            # Generate background image #
            #############################
            if background_type == 0:
                background_img = background_generator.gaussian_noise(
                    background_height, background_width
                )
            elif background_type == 2:
                background_img = background_generator.plain_white(
                    background_height, background_width
                )
            elif background_type == 3:
                background_img = background_generator.quasicrystal(
                    background_height, background_width
                )
            elif background_type == 4:
                background_img = background_generator.plain_black(
                    background_height, background_width
                )
            elif background_type == 5:
                background_img = background_generator.plan_gray(
                    background_height, background_width
                )

            else:
                background_img = background_generator.image_ver2(
                    background_height, background_width, background_image
                )

            # DISABLE BACKGROUND MASK
            # background_mask = Image.new(
            #     "RGB", (background_width, background_height), (0, 0, 0)
            # )

            #############################
            # Place text with alignment #
            #############################

            new_text_width, _ = resized_img.size
            # print("Background: {}, text: {}, margin: {}".format(background_img.size, resized_img.size, margins))
            if alignment == 0 or width == -1:
                background_img.paste(resized_img, (margin_left, margin_top), resized_img)
                # background_mask.paste(resized_mask, (margin_left, margin_top))
            elif alignment == 1:
                background_img.paste(
                    resized_img,
                    (int(background_width / 2 - new_text_width / 2), margin_top),
                    resized_img,
                )
                # background_mask.paste(
                #     resized_mask,
                #     (int(background_width / 2 - new_text_width / 2), margin_top),
                # )
            else:
                background_img.paste(
                    resized_img,
                    (background_width - new_text_width - margin_right, margin_top),
                    resized_img,
                )
                # background_mask.paste(
                #     resized_mask,
                #     (background_width - new_text_width - margin_right, margin_top),
                # )

            ##################################
            # Apply gaussian blur #
            ##################################

            gaussian_filter = ImageFilter.GaussianBlur(
                radius=blur if not random_blur else rnd.randint(0, blur)
            )
            final_image = background_img.filter(gaussian_filter)
            # final_mask = background_mask.filter(gaussian_filter)

            #####################################
            # Generate name for resulting image #
            #####################################
            if name_format == 2:   # best
                image_name = "{}_{}.{}".format(prefix_name, str(index), extension)
                mask_name = "{}_mask.png".format(str(index))
            elif name_format == 0:
                image_name = "{}_{}.{}".format(text, str(index), extension)
                mask_name = "{}_{}_mask.png".format(text, str(index))
            elif name_format == 1:
                image_name = "{}_{}.{}".format(str(index), text, extension)
                mask_name = "{}_{}_mask.png".format(str(index), text)

            elif name_format == 3:
                uuid_rand = uuid.uuid4()
                image_name = "{}_{}_{}.{}".format(str(uuid_rand), text.replace('/', '#'), str(uuid_rand), extension)
                mask_name = "{}_{}_{}_mask.png".format(str(uuid_rand), text.replace('/', '#'), str(uuid_rand), extension)
            else:
                print("{} is not a valid name format. Using default.".format(name_format))
                image_name = "{}_{}.{}".format(text, str(index), extension)
                mask_name = "{}_{}_mask.png".format(text, str(index))

            # Save the image
            if out_dir is not None:
                final_image.convert("RGB").save(os.path.join(out_dir, image_name))
                # print("DONE")
                # if output_mask == 1:
                #     final_mask.convert("RGB").save(os.path.join(out_dir, mask_name))
            else:
                # if output_mask == 1:
                #     return final_image.convert("RGB"), final_mask.convert("RGB")
                return final_image.convert("RGB")
        # except Exception as err:
        #     print(err)
        #     return
