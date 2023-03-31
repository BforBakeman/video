from flask import Flask, request, render_template
import pytube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the video URL and selected resolution from the form
        url = request.form['url']
        resolution = request.form['resolution']
        
        # Create a YouTube object
        video = pytube.YouTube(url)
        
        # Get the selected stream
        stream = video.streams.filter(res=resolution).first()
        
        # Download the stream
        stream.download()
        
        # Render the download success message
        return render_template('success.html')
    
    # Render the form template
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
