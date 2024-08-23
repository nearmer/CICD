% URL for the POST request

WECHAT_KEY = getenv(WECHAT_KEY);
% url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2f44d390-a990-41e0-9273-e8a2fc72b181';

url=strcat('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',WECHAT_KEY);

% Data to be sent in the request
data = struct(...
    'msgtype', 'text', ...
    'text', struct(...
        'content', '123e', ... % Replace 'Your message here' with the actual message variable
        'mentioned_list', {{'all'}} ... % Note: cell array for proper JSON formatting in MATLAB
    ) ...
);

% Options for webwrite, including specifying JSON content type
options = weboptions('MediaType', 'application/json','ContentType','text');
options.Timeout = 100;

% Send the POST request
response = webwrite(url, data, options);


