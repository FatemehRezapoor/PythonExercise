% Feb 8, 2018
% The code will help with K-sapce and fftshift/ why Log and what happens

a= imread('C:\Users\rezap\Desktop\cpost.png');
c=rgb2gray(a);
b=fft2(c);
% it is complex value so you need to read the abs
imshow(abs(b),[])
% it is completely black becasue the difference between values are big
% you can check the histogram to see what's going on
hist(abs(b(:)))
% but to know exactly the intensity distribution you can go with
hist(log(abs(b(:))))
% so to see the b values you need to use log scale
imshow(log(abs(b)),[])
% what you see is bright corners which corresponds to F(0,0)
b(1,1)
% check with
sum(c(:))
% The values are the same because F(0,0) equals the summation of all f(x,y)
% to show the values in the center 
imshow(fftshift(log(abs(b))),[])
