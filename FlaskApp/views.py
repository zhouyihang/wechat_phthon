from FlaskApp import app




#@app.route('/')
#def index():
#    return "Hello, World!"

# @app.route('/wx', methods = ['GET', 'POST'] )
# def wx():
#     from WeiXinCore.WeiXin import check_signature,echo
#     from flask import request
#     if not check_signature(request.args) and not app.debug:
#         return ""
#     return echo

@app.route('/',methods=['GET','POST'])
def wechat():
if request.method=='GET':
token='weixin'
data=request.args
signature=data.get('signature','')
timestamp=data.get('timestamp','')
nonce =data.get('nonce','')
echostr=data.get('echostr','')
s=[timestamp,nonce,token]
s.sort()
s=''.join(s)
if(hashlib.sha1(s).hexdigest()==signature):
return make_response(echostr)
else:
rec=request.stream.read()
xml_rec=ET.fromstring(rec)
tou = xml_rec.find('ToUserName').text
fromu = xml_rec.find('FromUserName').text
content = xml_rec.find('Content').text
xml_rep = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
