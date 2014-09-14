import db;

MAX_CACHE_LEN = 500;

class Cache(object):
    def __init__(self):
        self.li = [];
        self.di = {};
    def put(self, uid, data):
        if len(self.list) < MAX_CACHE_LEN:
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

def insert_organization(oname, ohasw):
    db.insert_organization(oname , ohasw);
    ci.put(oname , (oname , ohasw);
def select_organization(oname):
    if ci.has(oname): return ci.get(oname);
    dbout = db.select_organization(oname);
    if not dbout: return None;
    ci.put(oname , dbout);
    return ci,get(oname);
    
    
co = Cache();

cp = Cache();
def insert_post(ind_org, author, title, body, date_x):
    pid = db.insert_individual(ind_org, author, title, body, date_x);
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
    cp.put(pid, (pid, author, title, body, date_x));
def delete_post(pid):
    db.delete_post(pid);
    cp.pop(pid);
    
ce = Cache();    
def insert_event(oname, title, body, venue, date_s, date_e):
    eid = db.insert_event(oname , title , body , venue , date_s , date_e);
    ce.put(eid , (eid, title ,body , venue , date_s , date_e));
    return eid ;
def update_event(eid, title, body, venue, date_s, date_e):
    db.update_event(eid , title , body , venue , date_s , date_e);
    ce.put(eid ,(eid , title , body , venue , date_s , date_e)); 
def select_event(eid):
    if ce.has(eid): return ce.get(eid);
    dbout = db.select_event(eid);
    if not dbout: return None;
    ce.put(eid,dbout);
    return ce.get(eid);
def select_all_events(oname):
     if ce.has(oname): return ce.get(oname);
    dbout = db.select_all_posts(oname);
    if not dbout: return None;
    ce.put(oname, dbout);
    return ce.get(oname);
def delete_event(tid):
    db.delete_event(tid);
    ce.pop(tid);

cr = Cache();
def insert_rsvp(eid, iname, ans):
    eid = db.insert_rsvp(eid , iname , ans);
    cr.put(eid ,(eid , iname , ans));
def update_rsvp(eid, iname, ans):
    db.update(eid , iname , ans);
    cr.put(eid , (eid , iname , ans));
def select_rsvp(eid, iname):
    if cr.has(eid): return cr.get(eid);
    dbout = db.select_rsvp(eid , iname);
    if not dbout: return None;
    cr.put(eid , dbout);
    return cr.get(eid);

cv= Cache();
def insert_volunteer(oname, iname):
    oname = db.insert(oname , iname);
    cv.put(oname ,(oname , iname));
def select_volunteers(oname):
    if cv.has(oname): return cv.get(oname);
    dbout = db.select_all_posts(oname);
    if not dbout: return None;
    cv.put(oname, dbout);
    return cv.get(oname);
def delete_volunteer(oname, iname):  
    db.delete_volunteer(oname ,iname);
    db.pop(oname);  
    
