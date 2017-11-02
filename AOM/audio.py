#import pygame
#import time

import urllib.request
import urllib
import json
import base64
import os
#import sys
#sys.path.append('E:/biancheng/Python/AOM')
#import Dictionary as Dict

class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
        # token认证的url
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        # 语音合成的resturl
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
        # 语音识别的resturl
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        # 1.获取token
        token_url = self.token_url % (api_key,api_secert)
        r_str = urllib.request.urlopen(token_url).read()
        r_str = r_str.decode()
        token_data = json.loads(r_str)
        #print(token_data)
        self.token_str = token_data['access_token']
        pass

    def getVoice(self, text, filename):
        # 2. 向Rest接口提交数据
        get_url = self.getvoice_url % (urllib.parse.quote(text), self.cu_id, self.token_str)

        voice_data = urllib.request.urlopen(get_url).read()
        # 3.处理返回数据
        voice_fp = open(filename,'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        pass

    def getText(self, filename):
        # 2. 向Rest接口提交数据
        data = {}
        # 语音的一些参数
        data['format'] = 'wav'
        data['rate'] = 8000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str
        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        #print(post_data)
        r_data = urllib.request.urlopen(self.upvoice_url,data=bytes(post_data,encoding="utf-8")).read()       
        r_data = r_data.decode()
        print(r_data)
        # 3.处理返回数据
        if json.loads(r_data)['err_no']:
            return ''
        else:
            return json.loads(r_data)['result']

def thinking():
    api_key = "OawyrEjUT4Z73PGG3Vku6r8q" 
    api_secert = "RmuxbC5zjLMsdvrR2FRcSpCm5HQuPQsP"
    # 初始化
    bdr = BaiduRest("test_python", api_key, api_secert)
    for a in range(100):
        if not os.path.isfile("data/audio/record/%s.wav"%a):
            a = a-1
            record = bdr.getText("data/audio/record/%s.wav"%a)
            #pygame.mixer.init() 

#            if record == '':
#                file_music = 'E:/biancheng/Python/AOM/data/audio/xiaozhi/no_word.mp3'
#            else:
#                emo = Dict.audio(record)
#                word = str(record)
#                if re.findall('唱首歌', word):
#                    file_music = 'E:/biancheng/Python/AOM/data/audio/xiaozhi/Never be alone.mp3'
#                else:
#                    emo = emo[0]
#                    if emo == 0:
#                        file_music ='E:/biancheng/Python/AOM/data/audio/xiaozhi/no_emo.mp3'
#                    elif emo<0:
#                        file_music ='E:/biancheng/Python/AOM/data/audio/xiaozhi/sad.mp3'
#                    elif emo >0:
#                        file_music ='E:/biancheng/Python/AOM/data/audio/xiaozhi/pleasant.mp3'

            #pygame.mixer.music.load(file_music)
            #pygame.mixer.music.play()
            break
    return record
        
if __name__ == "__main__":
    a = 0
    api_key = "OawyrEjUT4Z73PGG3Vku6r8q" 
    api_secert = "RmuxbC5zjLMsdvrR2FRcSpCm5HQuPQsP"
    # 初始化
    bdr = BaiduRest("test_python", api_key, api_secert)
    # 将字符串语音合成并保存为out.mp3
    #bdr.getVoice("你说的蛮有道理", "E:/biancheng/Python/AOM/data/audio/xiaozhi/no_emo.mp3")
    thinking()


