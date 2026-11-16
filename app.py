from flask import Flask, request, send_from_directory
import os, time

app = Flask(__name__)
UP = "uploads"
os.makedirs(UP, exist_ok=True)

@app.route("/up", methods=["POST"])
def up():
    f = request.files.get("file")
    if f:
        name = time.strftime("%H%M%S") + "_" + str(int(time.time()*1000)%1000) + ".jpg"
        f.save(os.path.join(UP, name))
    return "ok"

@app.route("/")
def index():
    files = sorted(os.listdir(UP), reverse=True)[:30]
    imgs = "".join(f'<img src="/img/{x}" style="width:48%;margin:1%">' for x in files)
    return f"<body style='background:#111'>{imgs or 'لا صور بعد'}</body>"

@app.route("/img/<name>")
def img(name):
    return send_from_directory(UP, name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
