
function Createm(mdName)
    


    ShowLog(pwd)
    if 4==exist(mdName,'file')
        ShowLog("model is exist");
        return
    end
    h =new_system(mdName);
    save_system(h);
    Simulink.BlockDiagram.saveActiveConfigSet(h,'mdlCfg.m');
    
end
