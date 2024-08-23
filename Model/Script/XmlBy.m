% ��ȡRSSFeed
rss_url = 'https://rsshub.moeyy.cn/bing';
websave('BY.xml',rss_url,weboptions('ContentType','xmldom','Timeout',30));


rss_struct= xml2struct('BY.xml');


%%
% ��ȡͼƬ���Ӳ�����
for i = 20:numel(rss_struct.Children(2).Children)
    % ��ȡͼƬ����
    img_url = rss_struct.Children(2).Children(i).Children(4).Children.Data;
    img_url_start = strfind(img_url, 'src=') + 5;
    img_url_end = strfind(img_url, '.jpg') + 3;
    img_url = img_url(img_url_start:img_url_end);
    
    % ����ͼƬ
    [~,img_name,img_ext] = fileparts(img_url);
    img_save_path=[save_path,img_name,img_ext];
    websave(img_url,img_save_path);
end

disp('All Bing wallpapers have been downloaded!');