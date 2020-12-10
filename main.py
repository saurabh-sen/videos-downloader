from flask import Flask, render_template, flash, request, redirect, url_for
import youtube_dl

app = Flask(__name__)


# defining ENDPOINTS
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download/", methods=['GET', 'POST'])
def download():
    
    # Logic
    url = request.form['url']
    print("tries to download", url)
    with youtube_dl.YoutubeDL() as ydl:
        url = ydl.extract_info(url, download=False)
        download_link = url['formats'][-1]['url']
        return redirect(download_link+ "?dl=1")

# starting the server
app.run(debug=True)