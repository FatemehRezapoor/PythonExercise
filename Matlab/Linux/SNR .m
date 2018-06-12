% 1-Read the Dicom
image=dicomread('IM-0002-0001.dcm');
% 2- Show the Dicom
imshow(image,[])
% 3- Draws a handsfree ROI on the image
roi=imellipse;
% 4- Creates a mask from that ROI
bw=createMask(roi);
% 5- Converts the mask from logical to int
mask=int16(bw);
% 6- Extracts signal ROI from the image
signalROI=image.*mask;
% Shows the ROI to double check the precision
imshow(signalROI,[])
% save the ROI
save('signal.mat','signalROI')
% How to read the ROI again
% Sread=load('signal.mat');
% Sroi=Sread.signalROI;

% to get the average value for signal do not forget to only extract the non
% zero elements from your materix. Otherwise the resutls are wrong.
