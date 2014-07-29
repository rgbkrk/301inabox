import os
from flask import Flask

appname = "app"

app = Flask(appname)
app.config.from_object(appname)

app.config.update(dict(
    #SERVER_NAME="301.devsupport.me:5000",
    DEBUG=True
))

@app.route('/')
def test():
    return "Hello 301 in a Box!\n"

if __name__ == '__main__':
    app.run()