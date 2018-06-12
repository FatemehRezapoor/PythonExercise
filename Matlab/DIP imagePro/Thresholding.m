% Feb 12,2018
% to show how thresholding effects on the image 
a=imread('/Users/fatemehrezapoor/Desktop/timag.png');
imshow(a)
im=rgb2gray(a);
imshow(im)
imhist(im)
imshow(im<100,[])
% lets make a circle and see how thresholding works there
[x,y]=meshgrid([-50:50],[-50:50]);
im=(x.^2+y.^2<400);
% let's add some noise to this image
imn=imnoise(im,'gaussian',0,0.02);
imshow(imn) % now in this case it is hard to use histogram to define a threshold for the image
% let's add gradient to the image
g=ones(101,1)*linspace(-0.8,0.8,101);
img=im+g;
% so if you want to do the global thresholding you can't seperate
% background form foreground




