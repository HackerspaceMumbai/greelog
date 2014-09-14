import datetime;
from urllib2 import urlopen;

def utcnow():
    return str(datetime.datetime.utcnow());

def check_captcha(rand, captcha):
    return True;

