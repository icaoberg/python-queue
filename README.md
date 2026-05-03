# python-queue

> [!WARNING]
> This implementation is inspired by a homework assignment from [15-213](https://www.cs.cmu.edu/~213/) at Carnegie Mellon University. It is intended for educational purposes only and is not suitable for production use.

[![CI](https://github.com/icaoberg/python-queue/actions/workflows/ci.yml/badge.svg)](https://github.com/icaoberg/python-queue/actions/workflows/ci.yml)
[![Release Status](https://img.shields.io/badge/release-v0.1-red.svg)](https://github.com/icaoberg/python-queue)
[![GitHub issues](https://img.shields.io/github/issues/icaoberg/python-queue.svg)](https://github.com/icaoberg/python-queue/issues)
[![GitHub forks](https://img.shields.io/github/forks/icaoberg/python-queue.svg)](https://github.com/icaoberg/python-queue/network)
[![GitHub stars](https://img.shields.io/github/stars/icaoberg/python-queue.svg)](https://github.com/icaoberg/python-queue/stargazers)
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

A simple naive implementation of a [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) in Python.

The purpose of this repo is to serve as an example of how to set up a GitHub Actions workflow.

## Definition

> A collection of items in which only the earliest added item may be accessed. Basic operations are add (to the tail) or enqueue and delete (from the head) or dequeue. Also known as "first-in, first-out" or FIFO.

— Paul E. Black, *[queue](https://xlinux.nist.gov/dads/HTML/queue.html)*, Dictionary of Algorithms and Data Structures [online], NIST.

## When to Use

A queue is the right structure any time ordering must be preserved and the first item in should be the first item out:

- **Task scheduling** — operating system process schedulers and print spoolers process jobs in the order they arrive.
- **Breadth-first search (BFS)** — graph and tree traversals use a queue to visit nodes level by level.
- **Message brokers** — systems like RabbitMQ and Kafka model streams of events as queues so consumers process messages in order.
- **Rate limiting** — incoming requests are held in a queue and released at a controlled rate to protect downstream services.
- **Buffering I/O** — keyboard input and network packet buffers use queues so data is processed in the order it was received.

## Requirements

- Python 3.6+

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/icaoberg/python-queue.git
cd python-queue
pip install -r requirements.txt
```

## Usage

```python
from Queue import Queue

q = Queue()

q.push(1)
q.push(2)
q.push(3)

print(q.size())    # 3
print(q.peek())    # 1
print(q.pop())     # 1
print(q.size())    # 2
print(q.is_empty()) # False
```

### Methods

| Method | Description |
|--------|-------------|
| `push(element)` | Add an element to the back of the queue |
| `pop()` | Remove and return the front element |
| `peek()` | Return the front element without removing it |
| `is_empty()` | Return `True` if the queue has no elements |
| `size()` | Return the number of elements in the queue |

## Testing

```bash
pytest tests.py
```

## Support

If you found this project helpful, consider buying me a coffee!

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/icaoberg)

Copyright © [icaoberg](https://github.com/icaoberg) at [Carnegie Mellon University](https://www.cmu.edu). All rights reserved.
