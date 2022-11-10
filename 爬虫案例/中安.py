import urllib3
import xlrd
import requests
from ffmpy import FFmpeg
import os
import uuid
import subprocess

urllib3.disable_warnings()


def getvideo():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%22181ad312773fa-0477f0a8b1e15e-26021a51-1327104'
                  '-181ad312774ced%22%7D',
        'Host': 'c-vod.hw-cdn.xiaoeknow.com',
        'If-Modified-Since': 'Sun, 18 Sep 2022 15:56:21 GMT',
        'If-None-Match': 'c3485b534f57becedf13722287bd55c8',
        'sec-ch-ua': '"Google Chrome";v="105","Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/105.0.0.0 Safari/537.36',
    }
    data = xlrd.open_workbook('demo1.xls')  # 文件名以及路径，如果路径或者文件名有中文给前面加一个 r
    table = data.sheets()[0]
    names = data.sheet_names()
    if data.sheet_loaded(names[0]):
        nrows = table.nrows
        print('表格共有', nrows - 1, '行')
        url_list = [str(table.cell_value(i, 4)) for i in range(1, nrows)]
        # print('第5列所有的值：', name_list)
        for index, url in enumerate(url_list):
            print('第%d个元素值是[%s]' % (index, url))
            video_content = requests.get(url=url, headers=headers, verify=False).content
            with open('video\\' + str(index + 1) + '.mp4', mode='wb') as f:
                f.write(video_content)
            print('视频保存完成: ', index, url)


# 视频拼接
def concat(video_list: list, output_dir: str):
    if len(video_list) == 0:
        raise Exception('video_list can not empty')
    _ext = check_format(video_list)
    # _fps = check_fps(video_list)
    _result_path = os.path.join(
        output_dir, '{}{}'.format(
            uuid.uuid1().hex, _ext))
    _tmp_config = make_tmp_concat_config(video_list, output_dir)
    ff = FFmpeg(inputs={'{}'.format(_tmp_config): '-f concat -safe 0 -y'}, outputs={
        _result_path: '-c copy'})
    print(ff.cmd)
    ff.run()
    os.remove(_tmp_config)
    return _result_path


# 构造拼接所需临时文件
def make_tmp_concat_config(video_list: list, output_dir: str):
    _tmp_concat_config_path = os.path.join(output_dir, '{}.txt'.format(uuid.uuid1().hex))
    with open(_tmp_concat_config_path, mode='w', encoding='utf-8') as f:
        f.writelines(list(map(lambda x: 'file {}\n'.format(x), video_list)))
    return _tmp_concat_config_path


# 校验每个视频的格式
def check_format(video_list: list):
    _video_format = ''
    for x in video_list:
        _ext = os.path.splitext(x)[-1]
        if _video_format == '' and _ext != '':
            _video_format = _ext
            continue
        if _video_format != '' and _ext == _video_format:
            continue
        if _video_format != '' and _ext != _video_format:
            raise Exception('Inconsistent video format')
    return _video_format


# 校验每个视频的fps
def check_fps(video_list: list):
    _video_fps = 0
    for x in video_list:
        _fps = get_video_fps(x)
        if _video_fps == 0 and _fps:
            _video_fps = _fps
            continue
        if _video_fps != 0 and _fps == _video_fps:
            continue
        if _video_fps != '' and _fps != _video_fps:
            raise Exception('Inconsistent video fps')
    if _video_fps == 0:
        raise Exception('video fps error')
    return _video_fps


# 获取视频fps
def get_video_fps(video_path: str):
    ext = os.path.splitext(video_path)[-1]
    if ext != '.mp4' and ext != '.avi' and ext != '.flv':
        raise Exception('format not support')
    ffprobe_cmd = 'ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries ' \
                  'stream=r_frame_rate {} '
    p = subprocess.Popen(
        ffprobe_cmd.format(video_path),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
    out, err = p.communicate()
    print("subprocess 执行结果：out:{} err:{}".format(out, err))
    fps_info = str(out, 'utf-8').strip()
    if fps_info:
        if fps_info.find("/") > 0:
            video_fps_str = fps_info.split('/', 1)
            print('啦啦啦啦', video_fps_str[0], video_fps_str[1])
            fps_result = int(int(video_fps_str[0]) / int(video_fps_str[1]))
        else:
            fps_result = int(fps_info)
    else:
        raise Exception('get fps error')
    return fps_result


if __name__ == '__main__':
    # 获取视频片段
    getvideo()
    # 获取文件路径
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    lst = os.listdir('./video')
    clipvideo = []
    lst.sort(key=lambda x: int(x[:-4]))
    lst = [cur_dir.replace('\\', '/') + '/video/' + y for y in lst]
    print(lst)
    print(concat(lst, r'E:/ccccc/.vscode/Python.xuexi/爬虫学习/爬虫案例/中安专升本/英语'))
