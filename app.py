# 忽略文件 .gitigone
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "欢迎来到项目watchlist"