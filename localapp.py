from bottle_app import set_home, app;
set_home('http://localhost:8080/');
app.run(host='localhost', port=8080, debug=True, reloader=True);