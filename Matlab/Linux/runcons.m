

%==========================================================================
% CALL DIRECTORY AND PROGRESS BAR

 [fdir,name]=ReadDir
 h=waitbar(0,sprintf('Reconstruction in progress: 0 %% \n Calculating 1 out of %3d',length(fdir)));
 % set the name of the progress bar
 set(h,'Name','Progress');
% =========================================================================
% FUNCTIONS YOU WANT TO CALL   

% start a stop watch 
tstart=tic;
 for i=1:length(fdir)
    b= cd(char(fdir(i)));
    % FUNCTIONS AND RECONSTRUCTION 
    %------------------------------
    % Name and save the figures
    set(gcf,'numbertitle','off','name',char(name(i)))
    filename=['B',char(name(i))]
    savefig(filename) 
    %-------------------------------

    %-------------------------------
    % Calculate the progress
   percentDone = 100 * i / length(fdir);
   if i+1<=length(fdir)
   waitbar(i/length(fdir),h,sprintf('Reconstruction progress: %3.1f %%\n Calculating %3.1f out of %3d',percentDone,i+1,length(fdir)));
   else
   waitbar(i/length(fdir),h,sprintf('End of reconstruction'));
   end
    
 end
 % stop the stopwatch
 tend=toc(tstart);
 fprintf('Construction time:%d minutes and %f seconds\n',floor(tend/60),rem(tend,60));
 

