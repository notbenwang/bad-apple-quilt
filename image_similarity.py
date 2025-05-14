import json
from PIL import Image
import imagehash
import numpy as np

def find_closest_hash(hash, hashes):
    # hash: string of a 16 byte hash
    # hashes: list of 16 byte string hashes

    # binary search
    i = 0
    j = len(hashes)-1
    while i < j and abs(i-j) > 1:
        middle_index = (i + j) // 2
        middle_hash = hashes[middle_index]
        if middle_hash > hash: # go left
            j = middle_index
        else: # go right
            i = middle_index
    # tiebreaker
    left_hash = imagehash.hex_to_hash(hashes[i])
    right_hash = imagehash.hex_to_hash(hashes[j])
    image_hash = imagehash.hex_to_hash(hash)
    return str(left_hash) if abs(left_hash - image_hash) < abs(right_hash - image_hash) else str(right_hash) 

def check_none_hash_color(img):
    # Assume image is either fully black or fully white (i.e, average hash produces null-hash)
    # if true, image is black. if false, image is white.
    img_np = np.array(img)
    black_pixels = np.sum(img_np < 128)
    white_pixels = np.sum(img_np >= 128)
    return black_pixels > white_pixels

if __name__ == "__main__":
    with open('hash_indices.json', 'r') as f:
        hash_information = json.load(f)['Hash Information']
        hashes = list(hash_information.keys())
        hashes.sort()

    test_image_path = 'testing/test2.jpg'
    test_hash = str(imagehash.average_hash(Image.open(test_image_path)))
    closest_test_hash = find_closest_hash(str(test_hash), hashes)
    print(test_hash)
    print(closest_test_hash)
    print(hash_information[closest_test_hash])