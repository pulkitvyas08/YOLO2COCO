# YOLO Darknet to COCO Dataset format converter


## The two formats:

#### COCO datasets are of the format:

```Shell
    $COCO/
    $COCO/cache/
    $COCO/annotations/
    - test.json
    - train.json
    - val.json
    $COCO/images/
    $COCO/images/test/
    $COCO/images/train/
    $COCO/images/val/
```

Where the json image labels go into the ```$COCO/annotations``` directory

#### There are 3 components of the YOLO Darknet annotation format:

- ```obj.names```: Contains all the classes, here we need only "person" in it
- ```train.txt``` or ```test.txt``` or ```val.txt```: Contains all the file names of the images (absolute path) of the images of the particular split
- ```train/``` or ```test/``` or ```val/```: the folder that contains all the images and labels


## Steps of conversion

1. Extract the contents of this repo where all the ```test/``` ```train/``` and ```val/``` (or ```dev/```) directories are
2. Install all the dependencies using ```requirements.txt```
```
    pip3 install -r requirements.txt
```
3. Use the listFiles.py file to list all the file names of the ```train/``` directory into train.txt
```
    python3 listFiles.py [directory name, for e.g. train/]
```
4. (Optional) If there are classes additional to the person class then reflect the same in ```obj.names``` and ```main.py``` (line 7)
4. Run this command to convert to COCO format:
```
    python3 main.py --path [Absolute path of train.txt] --output [Name of the json file]
```
For e.g.

```
    python3 main.py --path D:\Workspace\Git-Repos\Yolo-to-COCO-format-converter\tutorial\train.txt --output train
```

Check the output folder for the resulting json file and put it into the appropriate directory as per the COCO format mentioned above
Do the same for the other two data splits (test and val/dev)
(To test this process there is some sample data in the tutorial folder that is in YOLO Darknet Format)

## For viewing the output json file in human-readable format use JQ:

Install JQ from [here]
```
    cd output
```
```
    jq . train.json > train_readable.json
```


Code from [Yolo-to-COCO-format-converter]

[Yolo-to-COCO-format-converter]: https://github.com/Taeyoung96/Yolo-to-COCO-format-converter
[here]: https://stedolan.github.io/jq/download/