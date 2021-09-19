from django.shortcuts import render
from django.http import StreamingHttpResponse
from main import camera

# Create your views here.

def index(request):
	return render(request, 'main/index.html')

def gen(camera):
	while True:
		frame = camera.getFrame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(camera.VideoCamera()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')
