% Feb 9,2018
% shows the FT of a filter and how it looks like
function filterft(h)
% h can be a lp filter in spatial domain
% it wants to show how spatial domain filter behave in frequency domain
% you can compare the high pass filter with low pass filter and see the
% difference
figure(1)
ft=fft2(h,512,512);
imshow(fftshift(log(abs(ft))),[]);

figure(2)
surf(fftshift(abs(ft)),'edgecolor','none');
% Good example to look at: 
% lp=[1 2 1;2 4 2;1 2 1]/16;
% This is a filter which has more weight for the center
% now try hp=1-lp