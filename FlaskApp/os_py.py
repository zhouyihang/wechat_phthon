from FlaskApp import app
import time

import urllib2

from flask import Flask,g,request,make_response

import hashlib

import xml.etree.ElementTree as ET

import json

import random

import re

import urllib

import sys

#import pylibmc




def youdao(word):
		return u'youdao'



def joke():
		return u'joke'

		



def weather(city_name):

	return u'weather'





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

		if content.lower()=='joke':

			response = make_response(xml_rep % (fromu,tou,str(int(time.time())),joke()))

			response.content_type='application/xml'

			return response

		elif 'tianqi' in content.lower():

			if type(content).__name__ == "unicode":

				content = content.encode('UTF-8')

				place=content.lower().replace('+tianqi','')

				response = make_response(xml_rep % (fromu,tou,str(int(time.time())),weather(place)))

				response.content_type='application/xml'

				return response

			else:

				place=content.lower().replace('+tianqi','')

				response = make_response(xml_rep % (fromu,tou,str(int(time.time())),weather(place)))

				response.content_type='application/xml'

				return response

		else:

			if type(content).__name__ == "unicode":

				content = content.encode('UTF-8')

				new_word=youdao(content)

				response = make_response(xml_rep % (fromu,tou,str(int(time.time())),new_word))

				response.content_type='application/xml'

				return response

			else:

				new_word=youdao(content)

				response = make_response(xml_rep % (fromu,tou,str(int(time.time())),new_word))

				response.content_type='application/xml'

				return response
