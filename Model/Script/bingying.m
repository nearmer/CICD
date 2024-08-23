% 设置文件保存路径
save_path = 'Images';



% 读取RSSFeed
rss_url = 'https://rsshub.baitry.com/bing';
rss_data = webread(rss_url);


rss_struct = xml2struct(rss_data);




% 获取图片链接并下载
for i = 20:numel(rss_struct.Children(2).Children)
    % 获取图片链接
    img_url = rss_struct.Children(2).Children(i).Children(4).Children.Data;
    img_url_start = strfind(img_url, 'src=') + 5;
    img_url_end = strfind(img_url, '.jpg') + 3;
    img_url = img_url(img_url_start:img_url_end);
    
    % 下载图片
    [~,img_name,img_ext] = fileparts(img_url);
    img_save_path=[save_path,img_name,img_ext];
    websave(img_url,img_save_path);
end

disp('All Bing wallpapers have been downloaded!');
