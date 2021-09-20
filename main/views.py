from django.shortcuts import render
from django.http import StreamingHttpResponse
from main import controller

# Create your views here.

def index(request):
	return render(request, 'main/index.html')

def gen():
	while True:
		frame = controller.getProcessedFrame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')
