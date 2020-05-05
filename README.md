# Coin-Detection-Open-Cv-

## Extracting value of coin from its images.
### Hough's Transform
##### Software-Python

This method can succcessfuly do the following mentioned features.

  - Detect multiple coins in a single image. 
  - Demarcate their denominations at their location in the image.
  - state the total number of coins present.

#### Hierarchy of steps involed in the code:
(these same statements are commented aswell in the code)
  - Input image.
  - Threshold values defined for various denominations.
  - Conversion of input rgb image to grayscale image.
  - Detection of coins in the input image.
  - Demarcation of the detected coins as per the tolerances.

#### 1.Input Image

> There are ten different input images named as digits from 1 to 10. Any one of these images can be selected through user input as shown to the end. 

#### 2.Threshold Values

> Herein the minimun tolerance in radius values are defined for 5, 2, 10 denominations. (anything less than five_min will be obviously 1 so no need to define it )

#### 3. RGB to Grayscale 

> A user defined function is written to convert rgb image to grayscale. Here note that the image is converted to an 8 bit image (uint8) from float64 as these are the requirements to be met before applying Hough's Transform. 

#### 4.Detecting the coins
>The parameters set for detection of only permissible circles are as follow:
- cv2.HOUGH_GRADIENT: detection method
- dp = 1: The inverse ratio of resolution
- 50 : minimum distance betweeen centres of two detected circles
- param1 = 50 : upper canny edge detector threshold
- param2 = 30 : lower canny edge detecteor threshold 
- minRadius = 30 minmium value of detectabe radius
- maxRadius = 60 maximum value of detectable radius
> Circles = Output is a 3-D list whose elements are a 1-D list in the format (x,y,r)
- x : x-cordinate of the centre
- y: y-cordinate of the centre
- r: radius of the circle

#### Demarcation of number of coins and its values.
>The length of circles[0,:] a 2-D list, gives the number of coins in the image. 
>The 1-D elements are referred by the variable 'i' in the code .This is then used to highlight the coin and mark its value at the centre (i[0], i[1]) after comparing radius i[2] with different tolerance values.
> Text is added using cv2.putText function and cirle is drawn using cv2.Circle function as seen in the code.



 
#### Output Image
> The output image is resized to fit in the screen. Further all details i.e. number and values of the coins will be indicated in the image itself.  




## Example of executing code on cmd.

```sh
D:\directory>python final_code.py
enter any number between 1 to 10 : 4
(Herein 4.jpg image file gets selected.)
```









  

 
