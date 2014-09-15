import datetime;
from urllib2 import urlopen;
import cdb;
OPEN_CAPTCHA = "http://www.opencaptcha.com/validate.php?img=%s&ans=%s"

def utcnow():
    return str(datetime.datetime.utcnow());

def check_captcha(image, answer):
    return urlopen(OPEN_CAPTCHA % (image, answer)).read() == 'pass';

def verify_signup(fname, lname, iname, ihasw, rand, captcha):
    if not all([fname, lname, iname, ihasw, rand, captcha]):
        return 'INSUFFICIENT DATA';
    if cdb.select_individual(iname) is not None:
        return 'USERNAME UNAVAILABLE';
    if not check_captcha(rand, captcha):
        return 'CAPTCHA MISMATCH';
    return True;

