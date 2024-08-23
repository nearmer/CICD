
%% Get current system
% Simulink
%   Commonly Used Blocks
%       In1
%       Ou1
%  h = add_block(source,dest)
%  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
% | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
% | | ____    ____ | || |      __      | || |  _________   | || |   _____      | || |      __      | || |   ______     | |
% | ||_   \  /   _|| || |     /  \     | || | |  _   _  |  | || |  |_   _|     | || |     /  \     | || |  |_   _ \    | |
% | |  |   \/   |  | || |    / /\ \    | || | |_/ | | \_|  | || |    | |       | || |    / /\ \    | || |    | |_) |   | |
% | |  | |\  /| |  | || |   / ____ \   | || |     | |      | || |    | |   _   | || |   / ____ \   | || |    |  __'.   | |
% | | _| |_\/_| |_ | || | _/ /    \ \_ | || |    _| |_     | || |   _| |__/ |  | || | _/ /    \ \_ | || |   _| |__) |  | |
% | ||_____||_____|| || ||____|  |____|| || |   |_____|    | || |  |________|  | || ||____|  |____|| || |  |_______/   | |
% | |              | || |              | || |              | || |              | || |              | || |              | |
% | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
%  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 



% source  
LSimulink = 'simulink/';
    Commonly_Used_Blocks = 'Commonly Used Blocks/';
        CIn1 = strcat(LSimulink,Commonly_Used_Blocks,'In1');
        COu1 = strcat(LSimulink,Commonly_Used_Blocks,'Out1');
        CSubsystem = strcat(LSimulink,Commonly_Used_Blocks,'Subsystem');
   Math_Operations = 'Math Operations/'; 
        MSum =  strcat(LSimulink,Math_Operations,'Sum');
        MAdd =  strcat(LSimulink,Math_Operations,'Add');
        
        
 
        
% dest
dest=bdroot(gcs);
    DSubsystem=strcat(dest,'/Add');
    DIn1=strcat(dest,'/DataIn1');
    DIn2=strcat(dest,'/DataIn2');
    DOu1=strcat(dest,'/DataOu1');
        DAdd = strcat(DSubsystem,'/add');
    
  
 % Create model   
 
add_block(CSubsystem,DSubsystem);

add_block(CIn1,DIn1);
add_block(CIn1,DIn2);
add_block(COu1,DOu1);

add_block(MAdd,DAdd);


