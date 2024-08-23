function  ShowLog(event)

% TODO Integration the Wechat Robot Services and Bark  Services

py.messageRobot.barMessage(event)   
disp(strcat('Info:',string(datetime),' Action :',event))

end