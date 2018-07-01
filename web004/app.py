from flask import *
import mlab
from models.video import Video
from youtube_dl import YoutubeDL

mlab.connect()
app = Flask(__name__)
app.secret_key = "Dat ultra super handsome"



@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos= videos)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    if request.method =='POST':
        form = request.form
        username = form['username']
        password = form['password']
    # query from database
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for("admin"))
        else:
            return "login failed"

@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect(url_for('index'))


@app.route ('/admin', methods = ['GET','POST'])
def admin():
    if "loggedin" in session:
        if request.method == 'GET':
            videos = Video.objects()
            print(videos)
            return render_template('admin.html', videos = videos)
        elif request.method == 'POST':
            form = request.form
            link = form['link']
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download = False)

            title = data['title']
            thumbnail = data['thumbnail']
            views = data['view_count']
            youtubeid = data['id']

            new_video = Video(
                title = title,
                thumbnail = thumbnail,
                views = views,
                link = link,
                youtubeid = youtubeid
            )
            new_video.save()
            return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))

@app.route ('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template('detail.html', youtube_id = youtube_id)









if __name__ == '__main__':
  app.run(debug=True)
 