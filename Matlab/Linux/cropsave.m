function [ image ] = cropsave( imagefiles )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
imagefiles=dir('*.png');
for i=1:length(imagefiles)
    m=imread(imagefiles(i).name);
    n=m(75:550,70:500,:);
    a=imagefiles(i).name;
    figname=sprintf('C %s',a);
    imwrite(n,figname,'png')
end


