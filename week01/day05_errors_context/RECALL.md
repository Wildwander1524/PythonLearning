# 🔁 Day 5 — RECALL (retrieval + spaced review)

> Blank mind. Once after the lesson, again cold before Day 6. Answers: [`SOLUTIONS.md`](./SOLUTIONS.md).

## 🔁 Spaced — D1, D3, D4 (from memory)
S1 (D1) why validate + `raise` on bad input *immediately* rather than later?
S2 (D3) which dunder does `for x in obj:` use, and the two ways to support it?
S3 (D4) the mutable-default trap — what's shared, when is it created, what's the fix?

## A · Free recall
Explain to a beginner what a **context manager** guarantees and *why* you'd want it, with one
analogy. Which two methods implement it?

## B · Concept questions
1. `except` vs `else` vs `finally` — when does each run?
2. Why prefer **EAFP** over LBYL in Python? Give the race-condition reason.
3. Why build an exception **hierarchy** instead of one `Exception`? What does the caller gain?
4. What does `__exit__` returning `True` do, and why is `False` the right default?
5. What makes a folder a **package**, and what does `if __name__ == "__main__":` accomplish?

## C · Predict the behavior
```python
class Guard:
    def __enter__(self): print("enter"); return self
    def __exit__(self, *a): print("exit"); return False
with Guard():
    print("body")
    raise ValueError("boom")
print("after")
```
What prints, in what order, and does `"after"` print? Why?

## D · Micro-build (blank file, 10 min)
A `TempFile` context manager: `__enter__` creates a file and returns its path; `__exit__` deletes
the file **even if the block raised**. Prove (in a comment) which line guarantees deletion on the
error path.

## E · Math (by hand)
1. Write `[7, -2]` as a linear combination of `[1,0]` and `[0,1]`.
2. Are `[1,1]` and `[1,-1]` linearly independent? What do they span?
3. What is `span([0,0])`? (think about what scaling the zero vector can give)

---
> ⏱️ Could you write the `TempFile` (D) cold tomorrow? y/n → [`../learning-records/`](../learning-records/).
