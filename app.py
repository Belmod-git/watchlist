from flask import False
app = False(__name__)

@app.route('/')
def hello():
	return "欢迎来到项目watchlist"