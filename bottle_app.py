import bottle;
import utils;
import cdb;
from db_cons import XLAT_INDIVIDUALS as xlat_i;
from db_cons import XLAT_POSTS as xlat_p;

bottle.TEMPLATE_PATH.append('/home/greelog/hubsite');
bottle.TEMPLATE_PATH.append('/home/greelog/hubsite/');
bottle.debug(True);
HOME = 'http://greelog.pythonanywhere.com/';

app = bottle.Bottle();
request = bottle.request;
response = bottle.response;
render = bottle.template;
redirect = bottle.redirect;

def set_cookie(iname):
    response.set_cookie('u', iname + ',' + str(hash(iname)));

def check_cookie():
    hiname = request.get_cookie('u');
    if (',') not in hiname: return False;
    [iname, h] = hiname.split(',');
    if str(hash(iname)) == h:
        return iname;
    return False;

@app.get('/')
def homepage():
    return render('welcome.tpl');

@app.post('/_login')
def login():
    iname = request.forms.get('username');
    ihasw = str(hash(request.forms.get('password')));
    cdbout = cdb.select_individual(iname);
    cdb_ihasw = cdbout[xlat_i['ihasw']];
    if cdb_ihasw == ihasw:
        set_cookie(iname);
        redirect(HOME + '_dashboard');
    return 'INVALID LOGIN ATTEMPT. PLEASE RETRY.'

@app.post('/_register')
def register():
    fname = request.forms.get('fname');
    lname = request.forms.get('lname');
    iname = request.forms.get('iname');
    ihasw = str(hash(request.forms.get('password')));
    rand = request.forms.get('rand');
    captcha = request.forms.get('captcha');
    veri = utils.verify_signup(fname, lname, iname, ihasw, rand, captcha);
    if veri is not True: return 'INVALID REGISTRATION ATTEMPT(%s.)' % veri;
    cdb.insert_individual(fname, lname, iname, ihasw);
    set_cookie(iname);
    redirect(HOME + '_dashboard');


@app.get('/_dashboard')
def dahsboard():
    iname = check_cookie();
    if iname is False: return 'AUTHENTICATION FAILED. PLEASE LOGIN.';
    return render('dashboard.tpl', TASKS=TASKS);

@app.get('/_events')
def events():
    iname = check_cookie();
    if iname is not False:
        return render('events.tpl')
    redirect(HOME);

@app.get('/_insert_post')
def insert_post():
    if check_cookie() is False: return 'INVALID REQUEST. PLEASE LOGIN FIRST.';
    return render('posts.tpl');

@app.post('/_insert_post')
def insert_post_2():
    iname = check_cookie();
    if iname is False: return 'AUTHENTICATION FAILED. PLEASE LOGIN FIRST';
    title = request.forms.get('title');
    body = request.forms.get('description');
    pid = cdb.insert_post(iname, title, body, utils.utcnow());
    redirect(HOME + '_select_post/' + str(pid));

@app.get('/_select_post/<pid:int>')
def select_post(pid):
    cdbout = cdb.select_post(pid);
    if cdbout:
        return render('read_post.tpl', title=cdbout[xlat_p['title']], body=cdbout[xlat_p['body']]);
    return 'Dang!! No such post was found!';

@app.get('/_select_all_posts/<iname>')
def select_all_posts(iname):
    cdbout= cdb.selectl_all_posts(iname);
    if cdbout:
        return render('list_posts.tpl', data=cdbout);
    return 'Dang!! No such posts were found!';

@app.get('/_logout')
def logout():
        response.set_cookie('u', 'empty');
        return render('''YOU HAVE SUCCESSFULLY LOGGED OUT.<br>
            <a href="{{home}}">&lt;&lt;&lt; &nbsp; Return Home</a>?''', home=HOME);

TASKS = {
    1: dict(title="task1", description="description1", weight=100),
    2: dict(title="task2", description="description2", weight=200),
    3: dict(title="task3", description="description3", weight=300),
    4: dict(title="task4", description="description4", weight=400),
    5: dict(title="task5", description="description5", weight=500),
    6: dict(title="task6", description="description6", weight=600),
};

def set_home(home):
    "Helpful in running code on localhost";
    global HOME;
    HOME = home;