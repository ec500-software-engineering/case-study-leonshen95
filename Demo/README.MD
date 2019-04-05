### Installing and Instruction

- Download all the files. You may save them in the same directory. Otherwise, you need to change the file path accordingly in the following steps.

- First, install **tensorflow** by:

```
- pip3 install tensorflow
```

And repeat for tensorflow_hub and any other packages that may be needed for the future. 

- Use **_image_Download.py_** to download dataset for any specific class from [ImageNet](http://www.image-net.org/). You can also use [Kaggle](https://www.kaggle.com/) or any other images websites to get the dataset ready. Dataset of different classes will be the core to train our model. For this project, I chose [ImageNet](http://www.image-net.org/) because it is more intuitive and much easier to download.  

In Python file, you can change the URL to whatever dataset you want to download. 
```
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04490091';
```
Also you can change the path where downloaded images will be stored and rename them accordingly.
```
e.g if not os.path.exists('/Users/leon/vehicle_photos/truck'):
        os.makedirs('/Users/leon/vehicle_photos/truck')
    urlretrieve(i, "/Users/leon/vehicle_photos/truck/"+str(pic_num)+".jpg")
```

* The images we are downloading are used as training set. Now you can randomly choose some other images and download them from Google images as testing set and keep in the same directory for future use.

- After obtaining different classes of dataset, run the **_retrain.py_** to train our model. Run the following command and you can change the target training dataset to whatever you want. I chose **vechicle_photos** for the following example. My sample flower_photo folder contains different classes folders of **car**, **SUV** and **truck**.
```
- python retrain.py --image_dir ~/vechicle_photos
```

It wil take some time to train depending on how large your dataset is. 

The trained model will be evetually stored in /tmp/output_graph.pb and your classes label will be stored in /tmp/output_labels.txt

- Finally, run the **_label_image.py_** 
```
python label_image.py \
--graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt \
--input_layer=Placeholder \
--output_layer=final_result \
--image=$HOME/Users/leon/SUV_car_truck_test/1.jpg
```
To change the test images to whatever you want, all you need is to change the path:
```
--image=PATH of the image
```
**Running the tests:** 

You should see someting like this:
```
2018-10-20 13:03:42.703097: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
truck 0.99930465
car 0.00049284665
suv 0.00020254114
```

**And what was the image we just used to test?**

![Alt text](https://github.com/leonshen95/deepLearning/blob/master/1.jpg?raw=true)
**Success!The image is indeed a truck.**
