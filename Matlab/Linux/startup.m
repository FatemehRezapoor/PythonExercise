diary('comhistory.txt')
disp('***************')
Date=datestr(now)
disp('***************')
format compact
format short g

% %------------ FreeSurfer -----------------------------%
% fshome = getenv('FREESURFER_HOME');
% fsmatlab = sprintf('%s/matlab',fshome);
% if (exist(fsmatlab) == 7)
%     path(path,fsmatlab);
% end
% clear fshome fsmatlab;
% %-----------------------------------------------------%
% 
% %------------ FreeSurfer FAST ------------------------%
% fsfasthome = getenv('FSFAST_HOME');
% fsfasttoolbox = sprintf('%s/toolbox',fsfasthome);
% if (exist(fsfasttoolbox) == 7)
%     path(path,fsfasttoolbox);
% end
% clear fsfasthome fsfasttoolbox;
%-----------------------------------------------------%


%% Change default pathdef directory
% Save starting directory
%startdir=pwd;
% specify new directory containing pathdef.m
%pathdir='home/fatemeh';
% change directory so that the new pathdef has highest precendence in 
%matlab search path
%cd(pathdir)
% set matlab search apth using path
%path(pathdef)
% change directory back to the starting directory
%cd(startdir)
