% Feb 8,2018
% edge detection(Gradient)
im= rgb2gray(imread('C:\Users\rezap\Desktop\robot.png'));
imshow (im)
h1=[1 -1];
h2=[1;-1];
gx=filter2(h1,im);
gy=filter2(h2,im);
imshow(gx,[])
imshow(gy,[])
colormap jet
colorbar
% Edge detection (sobel)
hx=[-1 0 1;-2 0 2;-1 0 1];
hy=hx';
ed1=filter2(hx,im);
figure
imshow (ed1,[])
colormap jet
colorbar
imshow (abs(ed1),[])
% Now lets take a look to the magnitude. This is where both vertical and
% horizantal lines are clear
m=sqrt(ed1.^2+ed2.^2);
angle= atan(ed2./ed1)*180/pi;
imshow(m,[])
imshow(abs(angle),[])
% you can even give a range to show only specific angles
imshow(abs(angle+30)<10,[])
e= (m>200)&(abs(angle<30));
