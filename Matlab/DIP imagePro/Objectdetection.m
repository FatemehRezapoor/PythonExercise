function findtemp(im,temp,th,showtemp)
% compares the template with the image
% as you decrease the gamma you ca nfind more and more donates which are
% similar to template but not exactly our template
out=normxcorr2(temp,im);
[m,n]=size(temp);
out=out(m+1:end,n+1:end);
% Defines a threshold to for Gamma to only show Gamma which is high
bw=out>th;
r=regionprops(bwlabel(bw));

if nargin>3
    im(1:m,1:n)=temp;
end
clf
imshow(im,[])
hold on
end

