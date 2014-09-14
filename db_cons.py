DROP_INDIVIDUALS = 'DROP TABLE IF EXISTS individuals';
CREATE_INDIVIDUALS = '''CREATE TABLE IF NOT EXISTS individuals(
                            fname VARCHAR(40),
                            lname VARCHAR(40),
                            iname VARCHAR(40) PRIMARY KEY,
                            ihasw VARCHAR(40),
                            iscore INTEGER
                        );''';
XLAT_INDIVIDUALS = dict(fname=0, lname=1, iname=2, ihasw=3, iscore=4);
INSERT_INDIVIDUAL = 'INSERT INTO individuals (fname, lname, iname, ihasw, iscore) VALUES (%s, %s, %s, %s, %s);';
SELECT_INDIVIDUAL = 'SELECT * FROM individuals WHERE iname = %s;';

DROP_POSTS = 'DROP TABLE IF EXISTS posts;';
CREATE_POSTS = '''CREATE TABLE IF NOT EXISTS posts(
                      pid INTEGER PRIMARY KEY AUTO_INCREMENT,
                      author VARCHAR(40),
                      title VARCHAR(100),
                      body TEXT,
                      date_x VARCHAR(40)
                  );''';
XLAT_POSTS = dict(pid=0, author=1, title=2, body=3, date_x=4);
INSERT_POST = 'INSERT INTO posts (author, title, body, date_x) values (%s, %s, %s, %s);''';
SELECT_POST = 'SELECT * FROM posts WHERE pid = %s;';
SELECT_ALL_POSTS = 'SELECT * FROM posts WHERE author = %s;';
UPDATE_POST = 'UPDATE posts SET title = %s, body = %s, date_x=%s WHERE pid = %s';
DELETE_POST = 'DELETE FROM posts WHERE pid = %s';

