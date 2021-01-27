import requests ,os
# server酱开关，填0不开启(默认)，填2同时开启cookie失效通知和签到成功通知
sever = 'on'
# 填写server酱sckey,不开启server酱则不用填（自己更改）
sckey = 'SCU38632T227a1bf30184008e4ec3cee158b877b25c2ce25bf3b54'
# 填入glados账号对应cookie
cookie = '_ga=GA1.2.1661826757.1605233816; koa:sess=eyJ1c2VySWQiOjUyMDI1LCJfZXhwaXJlIjoxNjMxMTUzOTM0MTQ3LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=-o4tsijFdbQB0kOCdsKaB1lsfIs; __cfduid=d3fdd9afe58df99b7a1a0caea019f99ca1611730606; _gid=GA1.2.155735652.1611730608; _gat_gtag_UA_104464600_2=1'
referer = 'https://glados.rocks/console/checkin'

def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    origin = "https://glados.rocks"
    referer = "https://glados.rocks/console/checkin"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    payload={
        'token': 'glados_network'
    }
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()
