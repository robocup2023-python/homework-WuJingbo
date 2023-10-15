import requests

if __name__ == '__main__':
    while True:
        Q = ''
        while Q.strip() == '' or len(Q.strip()) > 1000:
            Q = input('输入欲翻译文本：')
            if Q.strip() == '':
                print('欲翻译文本不可以为空！')
            if len(Q.strip()) > 1000:
                print('欲翻译文本长度不可以超过1000！')
        print('欲翻译文本 => %s' % (Q))
        From = input('请输入原文本语种(为空或没有输入采用自动识别)：')
        if From.strip() == '':
            From = 'Auto'
        print('原文本语种 => %s' % ({'Auto': 'Auto(自动识别)'}.get(From, From)))
        To = input('请输入翻译文本语种(为空或没有输入采用自动识别)：')
        if To.strip() == '':
            To = 'Auto'
        print('翻译文本语种 => %s' % ({'Auto': 'Auto(自动识别)'}.get(To, To)))
        data = {
            'q': Q,
            'from': From,
            'to': To
        }
        information = requests.post('https://aidemo.youdao.com/trans', data)
        json = information.json()
        errorCode = json['errorCode']
        if errorCode != '0':
            print('出现错误！返回的状态码为：%s' % (errorCode))
            break
        # tSpeakUrl = json['tSpeakUrl']
        # speakUrl = json['speakUrl']
        # web = json['web']
        query = json['query']
        translation = json['translation']
        print('原文本:' + query)
        for x in range(len(translation)):
            print('翻译结果' + str(x + 1) + " : " + translation[x])

'''
其中auto可以识别中文、英文、日文、韩文、法文、西班牙文、葡萄牙文、俄文、越南文、德文、阿拉伯文、印尼文、意大利文
简体中文：zh-CHS
英语：en
德语：de
法语：fr
日语：ja
官方链接：https://ai.youdao.com/DOCSIRMA/html/trans/api/wbfy/index.html
'''
