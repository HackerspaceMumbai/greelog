DROP_INDIVIDUALS = 'DROP TABLE IF EXISTS individuals';
CREATE_INDIVIDUALS = '''CREATE TABLE IF NOT EXISTS individuals(
                            fname VARCHAR(40),
                            lname VARCHAR(40),
                            iname VARCHAR(40),
                            ihasw VARCHAR(40),
                            iscore INTEGER
                        );''';
XLAT_INDIVIDUALS = dict(fname=0, lname=1, iname=2, ihasw=3, iscore=4);
INSERT_INDIVIDUAL = 'INSERT INTO individuals (fname, lname, iname, ihasw, iscore) VALUES (%s, %s, %s, %s, %s);';
SELECT_INDIVIDUAL = 'SELECT * FROM individuals WHERE iname = %s;';


DROP_ORGANIZATIONS = 'DROP TABLE IF EXISTS organizations';
CREATE_ORGANIZATIONS = '''CREATE TABLE IF NOT EXISTS organizations(
                              oname VARCHAR(40),
                              ohasw VARCHAR(40),
                              ovols INTEGER
                          );''';
XLAT_ORGANIZATIONS = dict(oname=0, ohasw=1, ovols=2);
INSERT_ORGANIZATION = 'INSERT INTO organizations (oname, ohasw, ovols) VALUES (%s, %s, %s);';
SELECT_ORGANIZATION = 'SELECT * FROM organizations WHERE oname = %s;';


DROP_POSTS = 'DROP TABLE IF EXISTS posts;';
CREATE_POSTS = '''CREATE TABLE IF NOT EXISTS posts(
                      pid INTEGER PRIMARY KEY AUTO_INCREMENT,
                      ind_org VARCHAR(40),
                      author VARCHAR(40),
                      title VARCHAR(100),
                      body TEXT,
                      date_x VARCHAR(40)
                  );''';
XLAT_POSTS = dict(pid=0, ind_org=1, author=2, title=3, body=4, date_x=5);
INSERT_POST = 'INSERT INTO posts (ind_org, author, title, body, date_x) values (%s, %s, %s, %s, %s);''';
SELECT_POST = 'SELECT * FROM posts WHERE pid = %s;';
SELECT_ALL_POSTS = 'SELECT * FROM posts WHERE autohr = %s;';
UPDATE_POST = 'UPDATE posts SET tilte = %s, body = %s, date_x=%s WHERE pid = %s';
DELETE_POST = 'DELETE FORM posts WHERE pid = %s';


DROP_EVENTS = 'DROP TABLE IF EXISTS events';
CREATE_EVENTS = '''CREATE TABLE IF NOT EXISTS events(
                       eid INTEGER PRIMARY KEY AUTO_INCREMENT,
                       oname VARCHAR(40),
                       title VARCHAR(100),
                       body TEXT,
                       venue VARCHAR(40),
                       date_s VARCHAR(40),
                       date_e VARCHAR(40)
                   )''';
XLAT_EVENT = dict(eid=0, oname=1, title=2, body=3, venue=4, date_s=5, date_e=6);
INSERT_EVENT = 'INSERT INTO events (oname, title, body, venue, date_s, date_e) VALUES (%s, %s, %s, %s, %s, %s);';
UPDATE_EVENT = 'UPDATE events SET title = %s, body = %s, venue = %s, date_s = %s, date_e = %s WHERE eid = %s;';
SELECT_EVENT = 'SELECT * FROM events WHERE eid = %s;';
SELECT_ALL_EVENTS = 'SELECT * FROM events WHERE oname = %s;';
DELETE_EVENT = 'DELETE FROM events WHERE eid = %s;';


DROP_RSVPS = 'DROP TABLE IF EXISTS rsvps';
CREATE_RSVPS = '''CREATE TABLE IF NOT EXISTS rsvps(
                      eid INTEGER,
                      iname VARCHAR(40),
                      ans VARCHAR(40)
                  );''';
XLAT_RSVPS = dict(eid=0, iname=1, ans=2);
INSERT_RSVP = 'INSERT INTO rsvps (eid, iname, ans) VALUES (%s, %s, %s);';
UPDATE_RSVP = 'UPDATE rsvps SET ans = %s WHERE eid = %s and iname = %s;';
SELECT_RSVP = 'SELECT * FROM rsvps WHERE eid = %s and iname = %s;';


DROP_VOLUNTEERS = 'DROP TABLE IF EXISTS volunteers';
CREATE_VOLUNTEERS = '''CREATE TABLE IF NOT EXISTS volunteers(
                           oname VARCHAR(40),
                           iname VARCHAR(40)
                       );''';
XLAT_VOLUNTEERS = dict(oname=0, iname=1);
INSERT_VOLUNTEER = 'INSERT INTO volunteers (oname, iname) VALUES (%s, %s);';
SELECT_VOLUNTEERS = 'SELECT * FROM volunteers WHERE oname = %s';
DELETE_VOLUNTEER = 'DELETE FROM volunteers WHERE oname = %s and iname = %s;';
                                                  
