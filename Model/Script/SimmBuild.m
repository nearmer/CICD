% Simulink Model Build

bdclose all

modelName = 'TTT13.slx';
% load_system(modelName);

% rtwbuild('TTT13');
slbuild("TTT13")

bdclose all



