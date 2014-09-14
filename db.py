import MySQLdb as mysql;
from db_cons import *;

def run(func):
    con = mysql.connect('mysql.server', 'greelog', 'king_kong', 'greelog$one')
    #con = mysql.connect('localhost', 'tuser', 'tpasw', 'tdb');
    with con:
        cur = con.cursor();
        ans = func(cur);
    return ans;


def insert_individual(fname, lname, iname, ihasw):
    def script(cur):
        cur.execute(INSERT_INDIVIDUAL, (fname, lname, iname, ihasw, 0));
    run(script);
def select_individual(iname):
    def script(cur):
        cur.execute(SELECT_INDIVIDUAL, (iname,));
        return cur.fetchone();
    return run(script);


def insert_organization(oname, ohasw):
    def script(cur):
        cur.execute(INSERT_ORGANIZATION, (oname, ohasw, 0));
    run(script);
def select_organization(oname):
    def script(cur):
        cur.execute(SELECT_ORGANIZATION, (oname,));
        return cur.fetchone();
    return run(script);


def insert_post(author, title, body, date_x):
    def script(cur):
        cur.execute(INSERT_POST, (author, title, body, date_x));
        return cur.lastrowid;
    return run(script);
def select_post(pid):
    def script(cur):
        cur.execute(SELECT_POST, (pid,));
        return cur.fetchone();
    return run(script);
def select_all_posts(author):
    def script(cur):
        cur.execute(SELECT_ALL_POSTS, (author,));
        return cur.fetchall();
    return run(script);
def update_post(pid, title, body, date_x):
    def script(cur):
        cur.execute(UPDATE_POST, (title, body, date_x, pid));
    run(script);
def delete_post(pid):
    def script(cur):
        cur.execute(DELETE_POST, (pid,));
    run(script);


def restart():
    def script(cur):
        for i in [
            DROP_INDIVIDUALS,
            CREATE_INDIVIDUALS,
            DROP_POSTS,
            CREATE_POSTS,
            DROP_POSTS,
            CREATE_POSTS
        ]:
            #print i;
            cur.execute(i);
            #print;
    run(script);
