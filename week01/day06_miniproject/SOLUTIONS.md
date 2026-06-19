# ✅ Day 6 — SOLUTIONS (cumulative answer key + capstone notes)

> Open only after attempting [`RECALL.md`](./RECALL.md) and the capstone.

## Part 1 · Concept answers
1. **Instance** = per-object state (`self.x`); **class** = one shared copy (`Cls.count`). Shared
   constants/counters → class; per-object data → instance.
2. Method exposed as a controlled attribute — encapsulation/validation *without* changing caller
   syntax (`obj.balance`, not `obj.get_balance()`). Omitting the setter makes it read-only.
3. So callers can't mutate your internal list and silently corrupt state.
4. Inheritance for genuine **is-a** subtypes (and ABCs/framework bases); composition for **has-a**
   and assembling behaviour. Default to composition.
5. Runs the parent's initializer so inherited attributes exist; skip it → `AttributeError` later.
6. A class that can't be instantiated and forces `@abstractmethod`s; a subclass skipping one
   **can't be instantiated** (`TypeError`) — fails early and loudly.
7. `super()` → **the next class in the MRO** (possibly a *sibling* in multiple inheritance). MRO =
   the fixed, left-to-right, deduplicated ancestor order (`Cls.__mro__`), via C3 linearization.
   Bonus: `D.__mro__ = (D, B, C, A, object)`.
8. `__repr__` → REPL/debugger/containers (**always**); `__str__` → `print`/users (when it
   differs). `__str__` falls back to `__repr__`, not vice-versa.
9. `__iter__` (best a generator) **or** `__getitem__` indexed `0,1,2…` until `IndexError`.
10. A **new** object — operators must not mutate operands.
11. `__eq__` sets `__hash__ = None` (equal must hash equal; Python can't verify your logic).
    Immutable → add `__hash__`; mutable → leave unhashable.
12. The default list is created **once at `def`-time** and shared across calls → accumulates. Fix:
    default `None`, create inside.
13. For data-holding classes (auto `__init__`/`__repr__`/`__eq__`). Mutable default →
    `field(default_factory=list)`, never `= []`.
14. Trades dynamic attributes (no per-instance `__dict__`) for lower memory + slightly faster
    access; worth it only with very many instances + a profiler's say-so.
15. `except` on a matching raise; `else` only if try raised nothing; `finally` always.
16. Guaranteed setup *and* teardown even on error; `__enter__` and `__exit__`.
17. An `__init__.py` makes it a package; the `__main__` guard runs a block only when executed
    directly, not imported.

## Part 2 · Math answers
1. `[6, 4]` · 2. `[3, -6]` · 3. `2+0+2 = 4` · 4. `√(36+64) = 10` · 5. `√(3²+4²) = 5` ·
6. `1/(1·√2) = 1/√2 ≈ 0.707` · 7. `[[1,3,5],[2,4,6]]`, shape `2×3` · 8. `[50, 110]` ·
9. `[[2,8],[1,19]]` (inner `2=2` → `2×2`) · 10. `7·[1,0] + (-2)·[0,1]` · 11. **dependent**
(`[2,4]=2·[1,2]`); span = the line through `[1,2]`, not the plane · 12. unchanged `[[1,2],[3,4]]`.

---

## Part 3 · Capstone reference notes — CLI contact book
Full spec/rubric in [`HOMEWORK.md`](./HOMEWORK.md). Key shapes (don't peek until you've built it):

```python
# contactbook/models.py
from dataclasses import dataclass
@dataclass
class Contact:
    name: str
    phone: str
    email: str = ""

# contactbook/errors.py  (the fuse box — D2 inheritance + D5 exceptions)
class ContactBookError(Exception): ...
class ContactNotFoundError(ContactBookError): ...
class DuplicateContactError(ContactBookError): ...

# contactbook/book.py  (encapsulation D1 + dunders D3 + persistence D5)
import json
from dataclasses import asdict
from .models import Contact
from .errors import ContactNotFoundError, DuplicateContactError

class ContactBook:
    def __init__(self):
        self._contacts: dict[str, Contact] = {}
    def add(self, c: Contact):
        if c.name in self._contacts:
            raise DuplicateContactError(c.name)
        self._contacts[c.name] = c
    def find(self, name: str) -> Contact:
        try: return self._contacts[name]
        except KeyError: raise ContactNotFoundError(name)   # EAFP, re-raise as domain error
    def delete(self, name: str):
        if name not in self._contacts:
            raise ContactNotFoundError(name)
        del self._contacts[name]
    def all(self) -> list[Contact]:
        return sorted(self._contacts.values(), key=lambda c: c.name)   # sorted COPY (D1)
    def __len__(self): return len(self._contacts)                      # D3
    def __iter__(self): return iter(self.all())                        # D3
    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:                   # context manager (D5)
            json.dump([asdict(c) for c in self.all()], f, indent=2)
    def load(self, path):
        try:
            with open(path, encoding="utf-8") as f:
                for d in json.load(f):
                    self.add(Contact(**d))
        except FileNotFoundError:
            pass                                                       # missing file → start empty (EAFP)
```
**Rubric self-check:** `Contact` is a `@dataclass` (D4) · custom exception hierarchy raised in the
book and **caught in the CLI loop** (D2+D5) · `_contacts` encapsulated, CRUD validated (D1) ·
`__len__`/`__iter__` (D3) · JSON save/load via `with` (D5) · clean package + `__init__.py` (D5) ·
tests incl. **save→load round-trip** · README + concept checks · pushed.

### Capstone concept-check answers
1. The context manager (`with open(...)`) guarantees the file is flushed/closed on every path in
   `save`/`load`; without it a mid-write error could leave a truncated or locked file.
2. Catch `ContactBookError` (the base) in the outer CLI loop so *any* domain error becomes a
   friendly message — you raise specific subclasses but the loop handles the whole category
   (raise early, catch late).
3. `all()` returning a sorted **copy** protects the Day-1 encapsulation lesson: callers iterating
   or sorting the result can't mutate the live `_contacts` store.

> 📝 When done, tell me **"Week 1 done"** (or send the repo link). I'll grade against the rubric,
> write the Week-1 retro, mark Week 1 ✅, update your ability boundary, and open **Week 2 — NumPy**.
