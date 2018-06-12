% Feb 8,2018
% The code shows how FT works and what happens in image construction 
function im=bf(m,n)
N=256;
[x,y]=meshgrid(0:(N-1),0:(N-1));
im=real(exp(-j*2*pi*(m*x/N+n*y/N)));
if (m==0) && (n==0)
    im=round(im);
end
% you can look to the overlay of images by
% c=imfuse(a,b)
% imshow (c)
% you can even look to the functions with surf command
% surf(a,'edgecolor','none')