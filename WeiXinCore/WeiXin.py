# coding:utf-8
#import time
#import MySQLdb
from flask import Flask, g, request, make_response
import hashlib
#import xml.etree.ElementTree as ET
#import urllib2
#import json



from Handlers.weixin_handler import *
#from index import app
#from WeiXin.weixin_handler import *
TOKEN = 'weixin'

EventType ={
    "subscribe":onSubscribe,
    "unsubscribe":onUnsubscribe,
    "scan":onScan,
    "location":onEventLocation,
    "click":onClick,
    "view":onView
}
#def onEvent(wxmsg):
#    return EventType[wxmsg.Event](wxmsg) if EventType.has_key(wxmsg.Event) else ''
Response = {
    "event":lambda wxmsg:EventType[wxmsg.Event](wxmsg) \
            if EventType.has_key(wxmsg.Event) else '',
    "text":onText,
    "voice":onVoice,
    "image":onImage,
    "video":onVideo,
    "shortvideo":onShortVideo,
    "location":onLocation,
    "link":onLink,
    }    
    


#print(youdao(u'who'))  

def check_signature(request_args):    
    query = request.args
    signature = query.get('signature', '')
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    #echostr = query.get('echostr', '')
    s = [timestamp, nonce, TOKEN]
    s.sort()
    s = ''.join(s)
    return hashlib.sha1(s).hexdigest() == signature

from FlaskApp import app
@app.route('/wx', methods = ['GET', 'POST'] )
def echo():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echo_str = request.args.get('echostr', '')
    encrypt_type = request.args.get('encrypt_type', '')
    msg_signature = request.args.get('msg_signature', '')

    print('signature:', signature)
    print('timestamp: ', timestamp)
    print('nonce:', nonce)
    print('echo_str:', echo_str)
    print('encrypt_type:', encrypt_type)
    print('msg_signature:', msg_signature)

    ##if not app.debug and not check_signature(request.args):
    if not app.debug and not check_signature(TOKEN, signature, timestamp, nonce):
        #不在Debug模式下，则需要验证。
        return ""
    if request.method == 'GET':
        return make_response(request.args.get('echostr', ''))      
    else:
        wxmsg = WeiXinMsg(request.data)        
        respXml = Response[wxmsg.MsgType](wxmsg) if wxmsg.MsgType in Response else ''
        #return respXml
        response = make_response(respXml)
        response.content_type = 'application/xml'
        return response
    
    
    
  
    
    
