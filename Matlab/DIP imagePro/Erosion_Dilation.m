% Feb 14,2018
% Erode and dilute the image
% The structure which is defined
se = strel('line',4,0);
% Useing these commands to inly take lines which are at 0 angle
ime=imdilate(im,se);
% use this to retrieve the thickness of the lines
ime2=imerode(ime,se);