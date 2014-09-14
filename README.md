Greelog is a green web blogging/networking platform.

It is currently being worked on.

The web application is currently live @ http://greelog.pythonanywhere.com

## To run the application locally:
1. Ammend HOME in `bottle_app.py` as follows:
```py
HOME = "http://localhost:8080/";
```
2. Add the following line to the end of `bottle_app.py`
```py
app.run(host='localhost', port=8080)
```
3. Run `bottle_app.py`:
```bash
$ python bottle_app.py
```
4. Open a browser and visit `http://localhost:8080`