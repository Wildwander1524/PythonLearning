# 📝 Day 6 Mini-Project — CLI Contact Book

> **Goal:** Build a small but *complete* command-line app that uses **everything** from Week 1 — classes, encapsulation, a `@dataclass`, a custom exception hierarchy, JSON persistence, context managers, and a clean package. Your Week-1 capstone and first portfolio piece.
> **Time:** 3 h  ·  **Read first:** [`LESSON.md`](./LESSON.md)

---

## 📖 Why this project (the interleaving payoff)

All week you drilled skills in isolation. This project **mixes them in one task** — which is harder, and exactly why it works: real software (and real jobs) demand combining skills under one roof, not one at a time. Each requirement below maps to a day:

| You'll use… | …from |
|-------------|-------|
| `@dataclass` for `Contact` | D4 |
| custom exception hierarchy (caught in the CLI) | D2 inheritance + D5 exceptions |
| encapsulated `_contacts`, validated CRUD | D1 encapsulation |
| `__len__` / `__iter__` on the book | D3 data model |
| JSON save/load via `with` (context manager) | D5 |
| clean package + `__init__.py` | D5 |

> 🎯 Don't peek at the day folders unless stuck — reproducing from memory (the **blank-file test**) is the real proof you own Week 1.

---

## ⏱️ Suggested time budget

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 45 min | `Contact` (dataclass) + `ContactBookError` hierarchy |
| **B** | 60 min | `ContactBook` — add / find / delete / list (in-memory) |
| **C** | 45 min | JSON **persistence** — save/load to disk via `with` |
| **D** | 45 min | CLI loop + tests + README + push |

## 📁 Files

```text
week01/day06_miniproject/
├── contactbook/
│   ├── __init__.py        # exposes the public API
│   ├── models.py          # Contact (dataclass)
│   ├── errors.py          # ContactBookError, ContactNotFoundError, DuplicateContactError
│   └── book.py            # ContactBook (CRUD + JSON persistence)
├── cli.py                 # the runnable command-line app
├── test_contactbook.py
└── README.md
```

---

## Requirements by block

### Block A — model + errors (45 min)
- [ ] `Contact` as a `@dataclass`: `name: str`, `phone: str`, `email: str = ""`.
- [ ] Exception hierarchy (the labeled fuse box):
  - `ContactBookError(Exception)` — base
  - `ContactNotFoundError(ContactBookError)`
  - `DuplicateContactError(ContactBookError)`

### Block B — `ContactBook` CRUD (60 min)
- [ ] Storage: `dict[str, Contact]` keyed by name, encapsulated as `self._contacts`.
- [ ] `add(contact)` — raise `DuplicateContactError` if the name exists.
- [ ] `find(name) -> Contact` — raise `ContactNotFoundError` if missing.
- [ ] `delete(name)` — raise `ContactNotFoundError` if missing.
- [ ] `all() -> list[Contact]` — return a **sorted copy** (by name).
- [ ] `__len__` and `__iter__` so `len(book)` and `for c in book:` work (Day-3 dunders).

### Block C — JSON persistence (45 min)
- [ ] `save(path)` — write all contacts to JSON, using `with open(...)` (Day-5 context manager).
- [ ] `load(path)` — read JSON back into `Contact` objects; if the file is missing, start empty (catch `FileNotFoundError` — EAFP).
- [ ] Use `dataclasses.asdict(contact)` to serialize; `Contact(**d)` to deserialize.

### Block D — CLI + tests + ship (45 min)
- [ ] `cli.py` — a menu loop:
  ```text
  1) Add   2) Find   3) Delete   4) List all   5) Quit
  ```
  Call the `ContactBook`, **catch your custom exceptions**, and print friendly messages — *never* let a raw traceback reach the user (raise early, catch late). Auto-save on change or on quit.
- [ ] `test_contactbook.py` — cover: add; duplicate raises; find-missing raises; delete; **save→load round-trip preserves contacts**.
- [ ] `README.md` — what it is + how to run (`python cli.py`).

---

## 🧠 Concept checks (in the README)

1. Where exactly does a context manager guarantee something in this app, and what would break without it?
2. Why catch `ContactBookError` (the base) in the CLI's outer loop, even though you raise the specific subclasses?
3. Which Day-1 lesson does `all()` returning a *sorted copy* (not the live dict's values) protect?

## ✅ Definition of done (the rubric I'll grade against)

| Criterion | Week-1 skill it proves |
|-----------|------------------------|
| [ ] `Contact` is a `@dataclass` | D4 dataclasses |
| [ ] Custom exception hierarchy, raised + caught in the CLI | D2 inheritance, D5 exceptions |
| [ ] `ContactBook` encapsulates `_contacts`; CRUD validated | D1 encapsulation |
| [ ] `__len__` / `__iter__` implemented | D3 data model |
| [ ] JSON save/load via `with` | D5 context managers |
| [ ] Clean package + `__init__.py`; CLI imports it | D5 packages |
| [ ] Tests pass; README + concept checks written; pushed | whole-week discipline |

## 🌟 Stretch

- **Search** (partial name/phone match) and an **update/edit** command.
- Validate phone/email and raise a `ValidationError(ContactBookError)`.
- Wrap load/save in a `Timer` context manager (Day-5 stretch) and print I/O time.
- Add `__repr__`/`__str__` to `ContactBook` showing the count (Day-3).

---

## 🚀 Submit

```bash
git add week01/day06_miniproject
git commit -m "add: Week1 D6 CLI contact book mini-project"
git push
```

Then tell me **"Week 1 done"** (or send the repo link). I'll review against the rubric, write your **Week-1 retro**, mark Week 1 ✅ in the study plan, and open **Week 2 — NumPy**. 🎉
