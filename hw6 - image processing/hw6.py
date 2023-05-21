# *************** HOMEWORK 6 ***************
# GOOD LUCK!

# ********************* Helper functions ***********************
import matplotlib.pyplot as plt


def display(image):
    plt.imshow(image, cmap="gist_gray")
    plt.show()


# ************************ QUESTION 1 **************************
def load_binary_image(img_path):
    file_content = open(img_path, 'r').read()
    file_content = file_content.split('\n')
    result = []
    for line in file_content:
        sublist = [int(binary_num) for binary_num in line]
        if sublist == []:
            continue
        result.append(sublist)
    return result


# ************************ QUESTION 2 **************************
def add_padding(image, padding):
    padded_image = []

    # preparing top and bottom padding
    width = len(image[0])
    top_n_bottom = [0]*width + [0]*2*padding

    # adding top padding
    for i in range(padding):
        padded_image.append(top_n_bottom)

    # adding side padding
    for line in image:
        new_line = [0]*padding + line + [0]*padding
        padded_image.append(new_line)

    # adding bottom padding
    for i in range(padding):
        padded_image.append(top_n_bottom)

    return padded_image

# ************************ QUESTION 3 **************************
def erosion(img_path, structuring_element):
    """
    This func progresses pixel by pixel and compared the 3x3 area around
    the chosen pixel to the structuring element.
    If there is a match, the new pixel in the eroded image will be white.
    """
    # prep
    load_image = load_binary_image(img_path)
    image = add_padding(load_image, 1)
    eroded_image = []

    width = len(image[0])
    height = len(image)

    # checking if structuring element is all zeros
    all_zeros = True
    for line in structuring_element:
        for pixel in line:
            if pixel == 1:
                all_zeros = False
    if all_zeros:
        return load_binary_image(img_path)

    # going pixel by pixel
    for h in range(1,height-1):
        new_line = []
        # looking at 3x3 areas around the chosen pixel's location
        for w in range(1, width - 1):
            # comparing kernel to current 3x3 area using locations
            locs = [[(h - 1, w - 1), (h - 1, w), (h - 1, w + 1)],
                    [(h, w - 1), (h, w), (h, w + 1)],
                    [(h + 1, w - 1), (h + 1, w), (h + 1, w + 1)]]
            matching = True
            for i in range(0, 3):
                for j in range(0, 3):
                    loc_i = locs[i][j][0]
                    loc_j = locs[i][j][1]
                    if structuring_element[i][j] == 1 and \
                            image[loc_i][loc_j] == 0:
                        matching = False

            # adding a pixel
            new_line.append((0,1)[matching])
        eroded_image.append(new_line)

    return eroded_image


# ************************ QUESTION 4 **************************
def dilation(img_path, structuring_element):
    """
        This func progresses pixel by pixel and compared the 3x3 area around
        the chosen pixel to the structuring element.
        If even one pixel is white, the new pixel in the dilated image will be white.
        """
    # prep
    load_image = load_binary_image(img_path)
    image = add_padding(load_image, 1)
    dilated_image = []

    width = len(image[0])
    height = len(image)

    # going pixel by pixel
    for h in range(1, height - 1):
        new_line = []
        # looking at 3x3 areas around the chosen pixel's location
        for w in range(1, width - 1):
            # comparing kernel to current cube using locations
            locs = [[(h-1,w-1), (h-1,w), (h-1, w+1)],
                    [(h, w-1), (h, w), (h, w+1)],
                    [(h+1, w-1), (h+1, w), (h+1, w+1)]]
            matching = False
            for i in range(0,3):
                for j in range(0,3):
                    loc_i = locs[i][j][0]
                    loc_j = locs[i][j][1]
                    if image[loc_i][loc_j] == 1 and \
                        image[loc_i][loc_j] == structuring_element[i][j]:
                        matching = True

            # adding a pixel
            new_line.append((0, 1)[matching])
        dilated_image.append(new_line)

    return dilated_image

