from Queue import Queue

def test_empty():
	q = Queue()
	assert q.isEmpty()
	assert q.size() == 0

def test_it():
	q = Queue()
	for i in range(100):
		q.push(i)
		assert q.size() == i+1
