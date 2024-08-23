function  ShowLog(event)

% TODO Integration the Wechat Robot Services and Bark  Services

py.messageRobot.WechatsendAll(event)   
disp(strcat('Info:',string(datetime),' Action :',event))

end