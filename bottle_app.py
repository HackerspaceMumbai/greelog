import bottle127 as bottle;
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
    msg = request.query.get('msg', '');
    return render('welcome.tpl', msg=msg);

@app.get('/_login')
def login_get():
    redirect('/');

@app.post('/_login')
def login():
    iname = request.forms.get('username');
    ihasw = str(hash(request.forms.get('password')));
    cdbout = cdb.select_individual(iname);
    if cdbout is not None:
        cdb_ihasw = cdbout[xlat_i['ihasw']];
        if cdb_ihasw == ihasw:
            set_cookie(iname);
            redirect(HOME + '_dashboard');
    return render('welcome.tpl', msg="INVALID LOGIN: PLEASE TRY AGAIN")

@app.get('/_register')
def register_get():
    redirect('/');

@app.post('/_register')
def register():
    fname = request.forms.get('fname');
    lname = request.forms.get('lname');
    iname = request.forms.get('iname');
    ihasw = str(hash(request.forms.get('password')));
    rand = request.forms.get('rand');
    captcha = request.forms.get('captcha');
    veri = utils.verify_signup(fname, lname, iname, ihasw, rand, captcha);
    if veri is not True:
        msg = ('REGISTRATION FAILED: ' + veri)
        redirect('/?msg=%s' % msg);
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

@app.get('/_explore')
def explore():
    iname = check_cookie();
    if iname is not False:
        return render('list_posts.tpl')
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
        redirect(HOME);

TASKS = [
    dict(title="Rain-Water Harvesting", description="Conserve the rain water by implementing rain water harvesting system at your society.", weight=250),
    dict(title="Adopt a tree!", description="By helping to water and care for a young street tree, you can help build a healthy tree canopy on your street.", weight=50),
    dict(title="Replace standard bulbs with CFLs", description="Compact fluorescent light bulbs are more energy-efficient than regular bulbs, while giving off the same amount of light.", weight=30),
    dict(title="task4", description="description4", weight=400),
    dict(title="task5", description="description5", weight=500),
    dict(title="task6", description="description6", weight=600),
];