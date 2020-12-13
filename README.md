# Lost & Found with Few Shot Object Detection

Our Repo consists of three major parts.

Each parts include their on README files with instructions, so follow the steps there.

## Crawler
Crawler crawls images by keyword from internet.

Although making custom images is possible, it is recommended to use the crawler for convinience.

You could designate thye keyword you want to search for such as "brown wallet" and the crawler will crawl images for you.

Detailed information is included in https://github.com/paulkth2/fewshotLAF/AutoCrawler


## Image Labeler
Just having the images is not enough.

Since we've trained our base model with PascalVOC dataset, we've included a image labeler for the PascalVOC dataset with bounding boxes.

Detailed steps could be found on
https://github.com/paulkth2/fewshotLAF/labelImg


## Our model
The original library could be found below.

https://github.com/ucbdrive/few-shot-object-detection

We have modified parts of it to enable training with new custom objects.

Detailed steps to train with new objects are written in
https://github.com/paulkth2/fewshotLAF/few-shot-object-detection

The full instruction regarding the library could be found on the original repo.