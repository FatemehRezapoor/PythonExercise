% feb 8,2018
% Filter which smooth the image and then find the edge
h=fspecial('log',[101 101],10);
surf(-h,'EdgeColor','none')
%log is the laplacian of gaussian filter
% it smoothes the image and then find the edges
h1=fspecial('log',[101 101],5);
h2=fspecial('log',[101 101],10);
im1=filter2(h1,im);
% you can even conbine different filters
surf(-(h1-h2),'EdgeColor','none');
% canny edge detection
e=edge(im2,'canny');
% to find the canny threshold value
[l,h]=edge(im2,'canny');
% to set your own threshold value
[l,h]=edge(im2,'canny',0.4);
imshow(l,[])


