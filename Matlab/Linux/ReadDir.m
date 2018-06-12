% Fatemeh Rezapoor, July 6, 2017.

function [fdir,name] = ReadDir(prompt)
% Input: Patient and Scan number
% Output: List of directories

%==========================================================================
    
[~,~,raw] = xlsread('/home/fatemeh/Data/Directory.xlsx');

%==========================================================================
% *POP UP WINDOW TO GET DATA*

% Input format: T1,T2 (The same scan for all patients)
% Input format: T1;T2 (Individual scan number for each patients)
% Shows total number of Patients and scans
strp=sprintf('Patient number: T1,T2 OR T1;T2 (For seperate interval)\nTotal: %d\n',size(raw,2)-1); 
strs=sprintf('Scan number: S1,S2 OR S1;S2(For seperate interval)\nTotal: %d\n',size(raw,1)-1); 
% number of inputs for inputdlg
prompt = {strp,strs}; 
% Title of inputdlg
title= 'Patient/Scan Info'; 
% Width of window
N=55; 
answer = inputdlg(prompt,title,[1,N]); 
%==========================================================================
%   CHECK INPUT FORMAT (NO EMPTY)/  CREATES CELL FOR DIRACTORY

if isempty(answer{1}) || isempty(answer{2})
warndlg('Wrong input:Character or empty')
return
end
% Creates an empty cell for maximum 50 directories
Dircell=cell(200,1);
n=1;
m=1;% the counter for Dir cell
% INDIVIDUAL SCANS
failscan=cell(200,1);
name=cell(200,1);
%==========================================================================
% INDIVISUAL SCANS:

% Checks to see if there is ; in user input
if strfind(answer{1},';')&strfind(answer{2},';')~=0 
% checks to see if there is enough input from user
if length(strfind(answer{1},';'))==length(strfind(answer{2},';')) 
    % reads patient information from user input
    Patient = str2num(answer{1});
    % seperate input in each ;
    scanf=strsplit(char(answer{2}),';'); 
    % find the length of inputs and goes through directory
    for j=1:length(Patient)
            scandata=str2num(scanf{j})
        for k=1:length(scandata)
            Dircell(n,1)=raw(scandata(1,k)+1,Patient(j,1)+1);
            % checks to make sure the element is not empty
            if  isnan(Dircell{n,1}) 
                % shows on the screen if the element is empty
                failscan(m,1)=cellstr(sprintf('No valid scan#%i for patient#%i', scandata(1,k), Patient(j,1)));
                m=m+1;
                break
            else 
                name(n,1)=cellstr(sprintf('TUM0%i,SC%i',Patient(j,1),scandata(1,k)))
                Dircell(n,1)=Dircell(n,1);
            end
            n=n+1;
        end
    end
%==========================================================================
 % IF THE NUMBER OF ; IS NOT EQUAL FOR SCAN AND PATIENT
   
else
    warndlg('Number of patients and scan group does not match (missing input)')
    return
end
%==========================================================================
% NO ; IN INPUT. SIMILAR SCAN

elseif isempty(strfind(answer{1},';')) & isempty(strfind(answer{2},';'))
    Patient = str2num(answer{1});
    Scan=str2num(answer{2});
    for i=1:length(Patient)
        for j=1:size(Scan,2)
            Dircell(n,1)= raw(Scan(j)+1,Patient(i)+1);
            if  isnan(Dircell{n,1}) 
                failscan(m,1)=cellstr(sprintf('No valid scan#%i for patient#%i', Scan(j), Patient(i)));
                m=m+1;
                break 
            else
                name(n,1)=cellstr(sprintf('TUM0%i,SC0%i',Patient(i),Scan(j)));
                Dircell(n,1)=Dircell(n,1);
            end
            n=n+1;
        end
    end
%==========================================================================
% DOES NOT MATCH ABOVE CRITERIA

else
warndlg('Number of patients and scan group does not match (missing input)')
return
end

%==========================================================================
%  RESULT

%sprintf('Directories loaded successfully:');
 % deletes empty arrays created inthe top

if cellfun(@isempty,failscan)
   fprintf('All directories are available')
else
   % Delete empty arrays created on top
   failscan=failscan(~cellfun(@isempty, failscan)) 
end
name=name(~cellfun(@isempty,name))
Dircell= Dircell(~cellfun(@isempty, Dircell));
fdir=Dircell(cellfun(@(x)all(~isnan(x(:))),Dircell))
%FDir=Dircell(cellfun(@(x)all(~isnan(x(:))),Dircell));% Deletes NAN from directory






