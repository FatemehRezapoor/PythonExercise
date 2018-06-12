% Feb 9,2018
% shows the list of the spatial filters
a= imread('C:\Users\rezap\Desktop\valley.jpg');
ag=rgb2gray(a);
% let's make a Smoothing filter
h=ones(3)/9;
out=filter2(h,ag);
imshow(out,[])
% let's make a sharpening filter
h=[0 1 0;1 -4 1;0 1 0];
out=filter2(h,ag);
imshow(out>50,[])
% let's make another sharpening filter
id=[0 0 0;0 1 0;0 0 0];
lp=ones(3)/9
hp=id-lp
out=filter2(hp,ag);
imshow(out)
% now let's make a new filter 
k=0.5;
nfil=id+k*hp;
out=filter2(nfil,ag);
imshow(out,[])
% non symetric filters (sobel filter)
h=[-1 -2 -1;0 0 0;1 2 1];
% median filter
out=medfilt2(ag,[3 3]);



