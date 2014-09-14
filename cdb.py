import db;
from db_cons import XLAT_POSTS;

MAX_CACHE_LEN = 500;

class Cache(object):
    def __init__(self):
        self.li = [];
        self.di = {};
    def put(self, uid, data):
        if len(self.li) < MAX_CACHE_LEN:
            self.li.append(uid);
            self.di[uid] = data;
        else:
            self.di.pop(self.li.pop(0));
    def pop(self, uid):
        self.di.pop(self.li.pop());
    def get(self, uid):
        return self.di.get(uid);
    def show(self):
        return self.li;
    def has(self, uid):
        return uid in self.di;

ci = Cache();
def insert_individual(fname, lname, iname, ihasw):
    db.insert_individual(fname, lname, iname, ihasw);
    ci.put(iname, (fname, lname, iname, ihasw, 0));
def select_individual(iname):
    if ci.has(iname): return ci.get(iname);
    dbout = db.select_individual(iname);
    if not dbout: return None;
    ci.put(iname, dbout);
    return ci.get(iname);

cp = Cache();
def insert_post(author, title, body, date_x):
    pid = db.insert_post(author, title, body, date_x);
    cp.put(pid, (pid, author, title, body, date_x));
    return pid;
def select_post(pid):
    if cp.has(pid): return cp.get(pid);
    dbout = db.select_post(pid);
    if not dbout: return None;
    cp.put(pid, dbout);
    return cp.get(pid);
def select_all_posts(author):
    if cp.has(author): return cp.get(author);
    dbout = db.select_all_posts(author);
    if not dbout: return None;
    cp.put(author, dbout);
    return cp.get(author);
def update_post(pid, title, body, date_x):
    db.update_post(pid, title, body, date_x);
    dbout = select_post(pid);
    xlat = XLAT_POSTS;
    cp.put(pid, (pid, dbout[xlat['author']], title, body, date_x));
def delete_post(pid):
    db.delete_post(pid);
    cp.pop(pid);

def restart():
	global ci, cp;
	ci = Cache();
	cp = Cache();
	db.restart();
