import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		process = time.time()- start 
		print(f"Time: {process}")
		return result
	return wrapper

@timer
def glacier(x):
	for _ in range(35000):
		pass

@timer
def fast_food():
	time.sleep(3)


glacier(5)
fast_food()

