import requests
import time

url = 'https://api.bilibili.com/x/v2/dm/post'
headers = {
    'Cookie': '_uuid=465B3DE2-8AD1-CA59-6643-F16EEBC1AFD045943infoc; buvid3=DDC71C87-F7CF-4D47-A758-D7C77F267BFB143111infoc; CURRENT_FNVAL=80; rpdid=|(u))u|)lkYY0JuY|ll|ullk; DedeUserID=398629090; DedeUserID__ckMd5=142bc2f433289c5e; SESSDATA=8efa0797%2C1621070768%2C5bb30*b1; bili_jct=e4cb871086b08d04ef95a1f9e70e219e; LIVE_BUVID=AUTO5416056288425944; sid=608h46o3; LNG=zh-CN; fingerprint3=02dbc096f2a17ed339ac6978d37b2617; buivd_fp=DDC71C87-F7CF-4D47-A758-D7C77F267BFB143111infoc; buvid_fp_plain=DDC71C87-F7CF-4D47-A758-D7C77F267BFB143111infoc; buvid_fp=DDC71C87-F7CF-4D47-A758-D7C77F267BFB143111infoc; CURRENT_QUALITY=120; blackside_state=1; fingerprint=e4721620d889a0e34a0da433e824acf5; fingerprint_s=728d6fbcc332a0b618b94c5fbfa54bc7; bp_t_offset_398629090=485265707422138041; bp_video_offset_398629090=485275916556316271; PVID=4; bfe_id=5db70a86bd1cbe8a88817507134f7bb5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
}


def message(msg, color):
    data = {
        'type': '1',
        'oid': '175782662',  # 该oid
        'msg': msg,
        'bvid': 'BV1mp4y1C7ZX',  # 要改BV号
        'progress': '52061',  # 时间
        'color': color,
        'fontsize': '25',
        'pool': '0',
        'mode': '5',
        'rnd': '1611846114902563',  # 该
        'plat': '1',
        'csrf': 'e4cb871086b08d04ef95a1f9e70e219e',
    }
    return data


list_strs = ['此生无悔二次元']
cloors = ['52480', '16740868', '16646914', '13369971', '4351678', '']
for color in cloors:
    for str in list_strs:
        datas = message(str, color)
        repos = requests.post(url=url, headers=headers, data=datas).text
        time.sleep(10)
        print(repos)
