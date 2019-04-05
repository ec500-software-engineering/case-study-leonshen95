from urllib.request import Request, urlretrieve
import cv2
import numpy as np
import os
import urllib
import sys

def store_raw_images():
    url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04402449'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    urls = response.read().decode('utf-8')

    if not os.path.exists('/Users/leon/utility_pole'):
        os.makedirs('/Users/leon/utility_pole')

    pic_num = 1
    for i in urls.split('\n'):
        try:
            print(i)
            urlretrieve(i, "/Users/leon/utility_pole/"+str(pic_num)+".jpg")
            # img = cv2.imread("vegetable/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # # should be larger than samples / pos pic (so we can place our image on it)
            # resized_image = cv2.resize(img, (100, 100))
            # cv2.imwrite("vegetable/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

store_raw_images()