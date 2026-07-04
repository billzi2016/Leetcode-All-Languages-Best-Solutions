# 0232. Implement Queue using Stacks

## Cpp

```cpp
#include <stack>
using namespace std;

class MyQueue {
private:
    stack<int> s1, s2;
    int frontVal;
public:
    MyQueue() {
    }
    
    void push(int x) {
        if (s1.empty()) frontVal = x;
        s1.push(x);
    }
    
    int pop() {
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        int val = s2.top();
        s2.pop();
        return val;
    }
    
    int peek() {
        if (!s2.empty()) return s2.top();
        return frontVal;
    }
    
    bool empty() {
        return s1.empty() && s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```

## Java

```java
import java.util.Stack;

class MyQueue {
    private Stack<Integer> inStack;
    private Stack<Integer> outStack;
    private int front;

    public MyQueue() {
        inStack = new Stack<>();
        outStack = new Stack<>();
    }

    public void push(int x) {
        if (inStack.isEmpty()) {
            front = x;
        }
        inStack.push(x);
    }

    public int pop() {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.push(inStack.pop());
            }
        }
        return outStack.pop();
    }

    public int peek() {
        if (!outStack.isEmpty()) {
            return outStack.peek();
        }
        return front;
    }

    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
```

## Python

```python
class MyQueue(object):
    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._in.append(x)

    def _transfer(self):
        while self._in:
            self._out.append(self._in.pop())

    def pop(self):
        """
        :rtype: int
        """
        if not self._out:
            self._transfer()
        return self._out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self._out:
            self._transfer()
        return self._out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self._in and not self._out
```

## Python3

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.in_stack and not self.out_stack:
            self.front = x
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        return self.front

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int *s1;
    int s1Size;
    int s1Cap;
    int *s2;
    int s2Size;
    int s2Cap;
} MyQueue;

static void pushStack(int **arr, int *size, int *cap, int val) {
    if (*size == *cap) {
        int newCap = (*cap == 0) ? 4 : (*cap * 2);
        *arr = realloc(*arr, newCap * sizeof(int));
        *cap = newCap;
    }
    (*arr)[(*size)++] = val;
}

static int popStack(int **arr, int *size) {
    return (*arr)[--(*size)];
}

static int topStack(int *arr, int size) {
    return arr[size - 1];
}

/** Initialize your data structure here. */
MyQueue* myQueueCreate() {
    MyQueue *obj = malloc(sizeof(MyQueue));
    obj->s1 = NULL; obj->s1Size = 0; obj->s1Cap = 0;
    obj->s2 = NULL; obj->s2Size = 0; obj->s2Cap = 0;
    return obj;
}

/** Push element x to the back of queue. */
void myQueuePush(MyQueue* obj, int x) {
    pushStack(&obj->s1, &obj->s1Size, &obj->s1Cap, x);
}

/** Transfers elements from s1 to s2 if s2 is empty. */
static void transferIfNeeded(MyQueue *obj) {
    if (obj->s2Size == 0) {
        while (obj->s1Size > 0) {
            int val = popStack(&obj->s1, &obj->s1Size);
            pushStack(&obj->s2, &obj->s2Size, &obj->s2Cap, val);
        }
    }
}

/** Removes the element from in front of queue and returns that element. */
int myQueuePop(MyQueue* obj) {
    transferIfNeeded(obj);
    return popStack(&obj->s2, &obj->s2Size);
}

/** Get the front element. */
int myQueuePeek(MyQueue* obj) {
    transferIfNeeded(obj);
    return topStack(obj->s2, obj->s2Size);
}

/** Returns whether the queue is empty. */
bool myQueueEmpty(MyQueue* obj) {
    return (obj->s1Size == 0 && obj->s2Size == 0);
}

/** Deallocate memory. */
void myQueueFree(MyQueue* obj) {
    free(obj->s1);
    free(obj->s2);
    free(obj);
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class MyQueue {
    private Stack<int> s1 = new Stack<int>();
    private Stack<int> s2 = new Stack<int>();

    public MyQueue() { }

    public void Push(int x) {
        s1.Push(x);
    }

    private void TransferIfNeeded() {
        if (s2.Count == 0) {
            while (s1.Count > 0) {
                s2.Push(s1.Pop());
            }
        }
    }

    public int Pop() {
        TransferIfNeeded();
        return s2.Pop();
    }

    public int Peek() {
        TransferIfNeeded();
        return s2.Peek();
    }

    public bool Empty() {
        return s1.Count == 0 && s2.Count == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */
```

## Javascript

```javascript
var MyQueue = function() {
    this.inStack = [];
    this.outStack = [];
};

MyQueue.prototype.push = function(x) {
    this.inStack.push(x);
};

MyQueue.prototype.pop = function() {
    if (this.outStack.length === 0) {
        while (this.inStack.length > 0) {
            this.outStack.push(this.inStack.pop());
        }
    }
    return this.outStack.pop();
};

MyQueue.prototype.peek = function() {
    if (this.outStack.length === 0) {
        while (this.inStack.length > 0) {
            this.outStack.push(this.inStack.pop());
        }
    }
    return this.outStack[this.outStack.length - 1];
};

MyQueue.prototype.empty = function() {
    return this.inStack.length === 0 && this.outStack.length === 0;
};
```

## Typescript

```typescript
class MyQueue {
    private inStack: number[];
    private outStack: number[];

    constructor() {
        this.inStack = [];
        this.outStack = [];
    }

    push(x: number): void {
        this.inStack.push(x);
    }

    pop(): number {
        if (this.outStack.length === 0) {
            while (this.inStack.length > 0) {
                this.outStack.push(this.inStack.pop() as number);
            }
        }
        return this.outStack.pop() as number;
    }

    peek(): number {
        if (this.outStack.length === 0) {
            while (this.inStack.length > 0) {
                this.outStack.push(this.inStack.pop() as number);
            }
        }
        return this.outStack[this.outStack.length - 1];
    }

    empty(): boolean {
        return this.inStack.length === 0 && this.outStack.length === 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
```

## Php

```php
class MyQueue {
    private $stackIn;
    private $stackOut;

    /**
     * Initialize your data structure here.
     */
    public function __construct() {
        $this->stackIn = [];
        $this->stackOut = [];
    }

    /**
     * @param Integer $x
     * @return NULL
     */
    public function push($x) {
        array_push($this->stackIn, $x);
    }

    /**
     * @return Integer
     */
    public function pop() {
        if (empty($this->stackOut)) {
            while (!empty($this->stackIn)) {
                $val = array_pop($this->stackIn);
                array_push($this->stackOut, $val);
            }
        }
        return array_pop($this->stackOut);
    }

    /**
     * @return Integer
     */
    public function peek() {
        if (empty($this->stackOut)) {
            while (!empty($this->stackIn)) {
                $val = array_pop($this->stackIn);
                array_push($this->stackOut, $val);
            }
        }
        return end($this->stackOut);
    }

    /**
     * @return Boolean
     */
    public function empty() {
        return empty($this->stackIn) && empty($this->stackOut);
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * $obj = new MyQueue();
 * $obj->push($x);
 * $ret_2 = $obj->pop();
 * $ret_3 = $obj->peek();
 * $ret_4 = $obj->empty();
 */
```

## Swift

```swift
class MyQueue {
    private var inStack: [Int] = []
    private var outStack: [Int] = []

    init() { }

    func push(_ x: Int) {
        inStack.append(x)
    }

    private func transferIfNeeded() {
        if outStack.isEmpty {
            while let element = inStack.popLast() {
                outStack.append(element)
            }
        }
    }

    func pop() -> Int {
        transferIfNeeded()
        return outStack.removeLast()
    }

    func peek() -> Int {
        transferIfNeeded()
        return outStack.last!
    }

    func empty() -> Bool {
        return inStack.isEmpty && outStack.isEmpty
    }
}
```

## Kotlin

```kotlin
class MyQueue() {
    private val inStack = java.util.ArrayDeque<Int>()
    private val outStack = java.util.ArrayDeque<Int>()

    fun push(x: Int) {
        inStack.addLast(x)
    }

    fun pop(): Int {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.addLast(inStack.removeLast())
            }
        }
        return outStack.removeLast()
    }

    fun peek(): Int {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.addLast(inStack.removeLast())
            }
        }
        return outStack.peekLast()!!
    }

    fun empty(): Boolean {
        return inStack.isEmpty() && outStack.isEmpty()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
```

## Dart

```dart
class MyQueue {
  final List<int> _inStack = [];
  final List<int> _outStack = [];

  MyQueue();

  void push(int x) {
    _inStack.add(x);
  }

  int pop() {
    if (_outStack.isEmpty) {
      while (_inStack.isNotEmpty) {
        _outStack.add(_inStack.removeLast());
      }
    }
    return _outStack.removeLast();
  }

  int peek() {
    if (_outStack.isEmpty) {
      while (_inStack.isNotEmpty) {
        _outStack.add(_inStack.removeLast());
      }
    }
    return _outStack.last;
  }

  bool empty() => _inStack.isEmpty && _outStack.isEmpty;
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = MyQueue();
 * obj.push(x);
 * int param2 = obj.pop();
 * int param3 = obj.peek();
 * bool param4 = obj.empty();
 */
```

## Golang

```go
type MyQueue struct {
	in  []int
	out []int
}

func Constructor() MyQueue {
	return MyQueue{
		in:  []int{},
		out: []int{},
	}
}

func (this *MyQueue) Push(x int) {
	this.in = append(this.in, x)
}

func (this *MyQueue) Pop() int {
	if len(this.out) == 0 {
		for len(this.in) > 0 {
			n := this.in[len(this.in)-1]
			this.in = this.in[:len(this.in)-1]
			this.out = append(this.out, n)
		}
	}
	val := this.out[len(this.out)-1]
	this.out = this.out[:len(this.out)-1]
	return val
}

func (this *MyQueue) Peek() int {
	if len(this.out) == 0 {
		for len(this.in) > 0 {
			n := this.in[len(this.in)-1]
			this.in = this.in[:len(this.in)-1]
			this.out = append(this.out, n)
		}
	}
	return this.out[len(this.out)-1]
}

func (this *MyQueue) Empty() bool {
	return len(this.in) == 0 && len(this.out) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
```

## Ruby

```ruby
class MyQueue
  def initialize()
    @in = []
    @out = []
  end

=begin
    :type x: Integer
    :rtype: Void
=end
  def push(x)
    @in << x
  end

=begin
    :rtype: Integer
=end
  def pop()
    transfer if @out.empty?
    @out.pop
  end

=begin
    :rtype: Integer
=end
  def peek()
    transfer if @out.empty?
    @out[-1]
  end

=begin
    :rtype: Boolean
=end
  def empty()
    @in.empty? && @out.empty?
  end

  private

  def transfer
    while !@in.empty?
      @out << @in.pop
    end
  end
end
```

## Scala

```scala
class MyQueue() {
    private val s1 = new java.util.ArrayDeque[Int]()
    private val s2 = new java.util.ArrayDeque[Int]()
    private var front = 0

    def push(x: Int): Unit = {
        if (s1.isEmpty && s2.isEmpty) {
            front = x
        }
        s1.addFirst(x)
    }

    def pop(): Int = {
        if (s2.isEmpty) {
            while (!s1.isEmpty) {
                s2.addFirst(s1.removeFirst())
            }
        }
        val res = s2.removeFirst()
        if (!s2.isEmpty) {
            front = s2.peekFirst()
        }
        res
    }

    def peek(): Int = {
        if (!s2.isEmpty) s2.peekFirst() else front
    }

    def empty(): Boolean = {
        s1.isEmpty && s2.isEmpty
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * val obj = new MyQueue()
 * obj.push(x)
 * val param_2 = obj.pop()
 * val param_3 = obj.peek()
 * val param_4 = obj.empty()
 */
```

## Rust

```rust
use std::cell::RefCell;

struct MyQueue {
    s1: RefCell<Vec<i32>>,
    s2: RefCell<Vec<i32>>,
}

impl MyQueue {
    fn new() -> Self {
        MyQueue {
            s1: RefCell::new(Vec::new()),
            s2: RefCell::new(Vec::new()),
        }
    }

    fn push(&self, x: i32) {
        self.s1.borrow_mut().push(x);
    }

    fn pop(&self) -> i32 {
        if self.s2.borrow().is_empty() {
            let mut s1 = self.s1.borrow_mut();
            let mut s2 = self.s2.borrow_mut();
            while let Some(v) = s1.pop() {
                s2.push(v);
            }
        }
        self.s2.borrow_mut().pop().unwrap()
    }

    fn peek(&self) -> i32 {
        if self.s2.borrow().is_empty() {
            let mut s1 = self.s1.borrow_mut();
            let mut s2 = self.s2.borrow_mut();
            while let Some(v) = s1.pop() {
                s2.push(v);
            }
        }
        *self.s2.borrow().last().unwrap()
    }

    fn empty(&self) -> bool {
        self.s1.borrow().is_empty() && self.s2.borrow().is_empty()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */
```

## Racket

```racket
(define my-queue%
  (class object%
    (super-new)

    ;; internal stacks
    (define s1 '())
    (define s2 '())

    ;; push : exact-integer? -> void?
    (define/public (push x)
      (set! s1 (cons x s1)))

    ;; pop : -> exact-integer?
    (define/public (pop)
      (when (null? s2)
        (let loop ()
          (unless (null? s1)
            (set! s2 (cons (car s1) s2))
            (set! s1 (cdr s1))
            (loop))))
      (let ((res (car s2)))
        (set! s2 (cdr s2))
        res))

    ;; peek : -> exact-integer?
    (define/public (peek)
      (when (null? s2)
        (let loop ()
          (unless (null? s1)
            (set! s2 (cons (car s1) s2))
            (set! s1 (cdr s1))
            (loop))))
      (car s2))

    ;; empty : -> boolean?
    (define/public (empty)
      (and (null? s1) (null? s2)))))
```

## Erlang

```erlang
-module(my_queue).
-export([my_queue_init_/0,
         my_queue_push/1,
         my_queue_pop/0,
         my_queue_peek/0,
         my_queue_empty/0]).

-spec my_queue_init_() -> any().
my_queue_init_() ->
    put(stack_in, []),
    put(stack_out, []).

-spec my_queue_push(X :: integer()) -> any().
my_queue_push(X) ->
    In = get(stack_in),
    put(stack_in, [X | In]).

-spec my_queue_pop() -> integer().
my_queue_pop() ->
    ensure_stack_out(),
    Out = get(stack_out),
    case Out of
        [Top | Rest] ->
            put(stack_out, Rest),
            Top;
        [] ->
            erlang:error(empty_queue)
    end.

-spec my_queue_peek() -> integer().
my_queue_peek() ->
    ensure_stack_out(),
    Out = get(stack_out),
    case Out of
        [Top | _] -> Top;
        [] -> erlang:error(empty_queue)
    end.

-spec my_queue_empty() -> boolean().
my_queue_empty() ->
    case {get(stack_in), get(stack_out)} of
        {[], []} -> true;
        _ -> false
    end.

ensure_stack_out() ->
    case get(stack_out) of
        [] ->
            In = get(stack_in),
            put(stack_out, lists:reverse(In)),
            put(stack_in, []);
        _ -> ok
    end.
```

## Elixir

```elixir
defmodule MyQueue do
  @spec init_() :: any
  def init_() do
    case Process.whereis(__MODULE__) do
      nil -> :ok
      pid -> Agent.stop(pid)
    end

    {:ok, _pid} = Agent.start_link(fn -> %{in: [], out: []} end, name: __MODULE__)
    :ok
  end

  @spec push(x :: integer) :: any
  def push(x) do
    Agent.update(__MODULE__, fn state ->
      %{state | in: [x | state.in]}
    end)
  end

  @spec pop() :: integer
  def pop() do
    ensure_out()
    Agent.get_and_update(__MODULE__, fn state ->
      [head | tail] = state.out
      {head, %{state | out: tail}}
    end)
  end

  @spec peek() :: integer
  def peek() do
    ensure_out()
    Agent.get(__MODULE__, fn state -> hd(state.out) end)
  end

  @spec empty() :: boolean
  def empty() do
    Agent.get(__MODULE__, fn state ->
      state.in == [] and state.out == []
    end)
  end

  defp ensure_out do
    case Agent.get(__MODULE__, & &1.out) do
      [] ->
        Agent.update(__MODULE__, fn state ->
          %{in: [], out: Enum.reverse(state.in)}
        end)

      _ -> :ok
    end
  end
end
```
