import time

class Camera():
	imgs = [open(f + '.jpg', 'rb').read() for f in ['1','2','3']]

	@staticmethod
	def frames():
		while True:
			time.sleep(1)
			yield Camera.imgs[int(time.time())%3]