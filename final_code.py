import cv2
import numpy as np
#Input image
num=input('enter any number between 1 to 10: ');
file='input images/'+num+'.jpg'
image=cv2.imread(file)
output=image

#threshold values for various denominations 
five_min=40.8
ten_min=49.5
two_min=43.6


# conversion of rgb image to grayscale image
def cvt_grayscale(input):
	color_img = input/255 
	row,col,ch=color_img.shape
	img = np.zeros([row,col],dtype=np.float64)
	for i in range(row):	
		for j in range(col):
			img[i,j]=255*((color_img[i][j][0]+color_img[i][j][1]+color_img[i][j][2]))/3
	# the input for houghs function has to be 8 bit so we convert it 
	img=img.astype(np.uint8)
	return img

# detection of circles in the input image
gray=cvt_grayscale(image)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,50,param1=50,param2=30,minRadius=30,maxRadius=60)

#Demarcation of the detected coins as per the tolerances.
if circles is not None:
	number_of_coins="This image has %d coin(s)"%(circles.shape[1])
	cv2.putText(output, number_of_coins, (50,50),cv2.FONT_HERSHEY_SIMPLEX, 2 , (255,0,0), 2, cv2.LINE_AA)
	for i in circles[0,:]:
		if(i[2]> ten_min):
			cv2.putText(output, 'ten rupee', (i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX, 1 , (255,0,0), 2 , cv2.LINE_AA) 
		if ( two_min < i[2] and i[2]< ten_min):
			cv2.putText(output, ' two rupee', (i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX, 1 , (255,0,0), 2 , cv2.LINE_AA) 
		if ( five_min < i[2] and  i[2]< two_min):
			cv2.putText(output, ' five rupee', (i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX, 1 , (255,0,0), 2 , cv2.LINE_AA) 
		if ( i[2] < five_min):
			cv2.putText(output, 'one rupee', (i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX, 1 , (255,0,0), 2 , cv2.LINE_AA) 
		cv2.circle(output , (i[0],i[1]), i[2],(0,255,0),2)

	#resize the output window to fit it in the computer screen.
	resized_output = cv2.resize(output, (900, 900))
	cv2.imshow('output',resized_output)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	print('no coins detected')