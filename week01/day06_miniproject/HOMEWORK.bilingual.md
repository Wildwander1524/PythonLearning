# 📝 Day 6 Mini-Project — CLI Contact Book
> 🇨🇳 **[第6天迷你项目 — 命令行通讯录]**

> **Goal:** Build a small but *complete* command-line app that uses **everything** from Week 1 — classes, encapsulation, a `@dataclass`, a custom exception hierarchy, JSON persistence, context managers, and a clean package. Your Week-1 capstone and first portfolio piece.
> **Time:** 3 h  ·  **Read first:** [`LESSON.md`](./LESSON.md)
> 🇨🇳 **目标：** 构建一个虽小但*完整*的命令行应用，它用到了第一周的全部知识点 — 类、封装、`@dataclass`、自定义异常层次、JSON持久化、上下文管理器以及一个整洁的包。这是你第一周的顶石项目，也是你的第一个作品集作品。
> 🇨🇳 **时间：** 3小时 · **先读：** [`LESSON.md`](./LESSON.md)

---

## 📖 Why this project (the interleaving payoff)
> 🇨🇳 **📖 为什么做这个项目（交错练习的回报）**

All week you drilled skills in isolation. This project **mixes them in one task** — which is harder, and exactly why it works: real software (and real jobs) demand combining skills under one roof, not one at a time. Each requirement below maps to a day:
> 🇨🇳 整个星期你都在孤立地练习技能。这个项目把它们**融合在一个任务里** — 这难度更大，但正是它有效的原因：真正的软件（和真实的工作）要求把多种技能结合起来运用，而不是一次只处理一种。下面的每个需求都对应着某一天的内容：

| You'll use… | …from |
|-------------|-------|
| `@dataclass` for `Contact` | D4 |
| custom exception hierarchy (caught in the CLI) | D2 inheritance + D5 exceptions |
| encapsulated `_contacts`, validated CRUD | D1 encapsulation |
| `__len__` / `__iter__` on the book | D3 data model |
| JSON save/load via `with` (context manager) | D5 |
| clean package + `__init__.py` | D5 |

| 你将用到… | 来自… |
|------------|-------|
| `@dataclass` 用于 `Contact` | D4 |
| 自定义异常层次（在CLI中捕获） | D2 继承 + D5 异常 |
| 封装的 `_contacts`，带验证的CRUD | D1 封装 |
| 通讯录上的 `__len__` / `__iter__` | D3 数据模型 |
| 通过 `with`（上下文管理器）进行JSON保存/加载 | D5 |
| 整洁的包 + `__init__.py` | D5 |

> 🎯 Don't peek at the day folders unless stuck — reproducing from memory (the **blank-file test**) is the real proof you own Week 1.
> 🇨🇳 🎯 除非卡住了，否则别看每天的文件夹——凭记忆重现（**空白文件测试**）才是你掌握第一周内容的真正证明。

---

## ⏱️ Suggested time budget
> 🇨🇳 **⏱️ 建议时间预算**

| Block | Time | What you do |
|-------|------|-------------|
| **A** | 45 min | `Contact` (dataclass) + `ContactBookError` hierarchy |
| **B** | 60 min | `ContactBook` — add / find / delete / list (in-memory) |
| **C** | 45 min | JSON **persistence** — save/load to disk via `with` |
| **D** | 45 min | CLI loop + tests + README + push |

| 阶段 | 时间 | 任务 |
|------|------|------|
| **A** | 45 分钟 | `Contact`（dataclass）+ `ContactBookError` 异常层次 |
| **B** | 60 分钟 | `ContactBook` — 添加/查找/删除/列表（内存操作） |
| **C** | 45 分钟 | JSON **持久化** — 通过 `with` 保存/加载到磁盘 |
| **D** | 45 分钟 | CLI循环 + 测试 + README + 推送 |

## 📁 Files
> 🇨🇳 **📁 文件结构**

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
> 🇨🇳 *[项目目录树，列出了所有需要创建的文件]*

---

## Requirements by block
> 🇨🇳 **按阶段划分的需求**

### Block A — model + errors (45 min)
> 🇨🇳 **阶段A — 模型与异常（45分钟）**

- [ ] `Contact` as a `@dataclass`: `name: str`, `phone: str`, `email: str = ""`.
- [ ] Exception hierarchy (the labeled fuse box):
  - `ContactBookError(Exception)` — base
  - `ContactNotFoundError(ContactBookError)`
  - `DuplicateContactError(ContactBookError)`
- [ ] 将 `Contact` 设为 `@dataclass`：`name: str`、`phone: str`、`email: str = ""`。
- [ ] 异常层次（标注的保险丝盒）：
  - `ContactBookError(Exception)` — 基类
  - `ContactNotFoundError(ContactBookError)`
  - `DuplicateContactError(ContactBookError)`

### Block B — `ContactBook` CRUD (60 min)
> 🇨🇳 **阶段B — `ContactBook` CRUD（60分钟）**

- [ ] Storage: `dict[str, Contact]` keyed by name, encapsulated as `self._contacts`.
- [ ] `add(contact)` — raise `DuplicateContactError` if the name exists.
- [ ] `find(name) -> Contact` — raise `ContactNotFoundError` if missing.
- [ ] `delete(name)` — raise `ContactNotFoundError` if missing.
- [ ] `all() -> list[Contact]` — return a **sorted copy** (by name).
- [ ] `__len__` and `__iter__` so `len(book)` and `for c in book:` work (Day-3 dunders).
- [ ] 存储：`dict[str, Contact]` 以名字为键，封装为 `self._contacts`。
- [ ] `add(contact)` — 若名字已存在则抛出 `DuplicateContactError`。
- [ ] `find(name) -> Contact` — 若缺失则抛出 `ContactNotFoundError`。
- [ ] `delete(name)` — 若缺失则抛出 `ContactNotFoundError`。
- [ ] `all() -> list[Contact]` — 返回一份**已排序的副本**（按名字排序）。
- [ ] `__len__` 和 `__iter__`，以便 `len(book)` 和 `for c in book:` 可以正常使用（第三天的魔法方法）。

### Block C — JSON persistence (45 min)
> 🇨🇳 **阶段C — JSON持久化（45分钟）**

- [ ] `save(path)` — write all contacts to JSON, using `with open(...)` (Day-5 context manager).
- [ ] `load(path)` — read JSON back into `Contact` objects; if the file is missing, start empty (catch `FileNotFoundError` — EAFP).
- [ ] Use `dataclasses.asdict(contact)` to serialize; `Contact(**d)` to deserialize.
- [ ] `save(path)` — 使用 `with open(...)`（第5天的上下文管理器）将所有联系人写入JSON文件。
- [ ] `load(path)` — 从JSON读回 `Contact` 对象；如果文件缺失，则从空开始（捕获 `FileNotFoundError` — EAFP风格）。
- [ ] 使用 `dataclasses.asdict(contact)` 序列化；使用 `Contact(**d)` 反序列化。

### Block D — CLI + tests + ship (45 min)
> 🇨🇳 **阶段D — CLI + 测试 + 交付（45分钟）**

- [ ] `cli.py` — a menu loop:
  ```text
  1) Add   2) Find   3) Delete   4) List all   5) Quit
  ```
  Call the `ContactBook`, **catch your custom exceptions**, and print friendly messages — *never* let a raw traceback reach the user (raise early, catch late). Auto-save on change or on quit.
- [ ] `test_contactbook.py` — cover: add; duplicate raises; find-missing raises; delete; **save→load round-trip preserves contacts**.
- [ ] `README.md` — what it is + how to run (`python cli.py`).
- [ ] `cli.py` — 一个菜单循环：
  ```text
  1) 添加   2) 查找   3) 删除   4) 列出全部   5) 退出
  ```
  > 🇨🇳 *[命令行菜单的选项文字]*

  调用 `ContactBook`，**捕获自定义异常**，并打印友好的提示信息 — *决不能让原始的回溯信息暴露给用户*（早早抛出，晚晚捕获）。每次修改后或退出时自动保存。
- [ ] `test_contactbook.py` — 覆盖：添加；重复添加抛出异常；查找缺失项抛出异常；删除；**保存→加载的往返过程能保留联系人**。
- [ ] `README.md` — 是什么 + 如何运行（`python cli.py`）。

---

## 🧠 Concept checks (in the README)
> 🇨🇳 **🧠 概念自查（写在README里）**

1. Where exactly does a context manager guarantee something in this app, and what would break without it?
2. Why catch `ContactBookError` (the base) in the CLI's outer loop, even though you raise the specific subclasses?
3. Which Day-1 lesson does `all()` returning a *sorted copy* (not the live dict's values) protect?
> 🇨🇳 1. 在这个应用里，上下文管理器究竟在哪个环节提供了保障？如果没有它，会出什么问题？
> 🇨🇳 2. 为什么在CLI的外层循环中捕获 `ContactBookError`（基类），尽管你抛出的是具体的子类？
> 🇨🇳 3. `all()` 返回一份*已排序的副本*（而非直接返回字典的实时值），这一设计保护了第一天的哪条原则？

## ✅ Definition of done (the rubric I'll grade against)
> 🇨🇳 **✅ 完成标准（我用来评分的条目）**

| Criterion | Week-1 skill it proves |
|-----------|------------------------|
| [ ] `Contact` is a `@dataclass` | D4 dataclasses |
| [ ] Custom exception hierarchy, raised + caught in the CLI | D2 inheritance, D5 exceptions |
| [ ] `ContactBook` encapsulates `_contacts`; CRUD validated | D1 encapsulation |
| [ ] `__len__` / `__iter__` implemented | D3 data model |
| [ ] JSON save/load via `with` | D5 context managers |
| [ ] Clean package + `__init__.py`; CLI imports it | D5 packages |
| [ ] Tests pass; README + concept checks written; pushed | whole-week discipline |

| 标准 | 证明的第一周技能 |
|------|----------------|
| [ ] `Contact` 是一个 `@dataclass` | D4 数据类 |
| [ ] 自定义异常层次，在CLI中抛出并捕获 | D2 继承，D5 异常 |
| [ ] `ContactBook` 封装了 `_contacts`；CRUD带有验证 | D1 封装 |
| [ ] 实现了 `__len__` / `__iter__` | D3 数据模型 |
| [ ] 通过 `with` 进行JSON保存/加载 | D5 上下文管理器 |
| [ ] 整洁的包 + `__init__.py`；CLI正确导入 | D5 包 |
| [ ] 测试通过；README和概念自查已编写；已推送 | 全周纪律 |

## 🌟 Stretch
> 🇨🇳 **🌟 扩展挑战**

- **Search** (partial name/phone match) and an **update/edit** command.
- Validate phone/email and raise a `ValidationError(ContactBookError)`.
- Wrap load/save in a `Timer` context manager (Day-5 stretch) and print I/O time.
- Add `__repr__`/`__str__` to `ContactBook` showing the count (Day-3).
- **搜索**（按姓名或电话的部分匹配）和**更新/编辑**命令。
- 验证电话和邮箱，并抛出 `ValidationError(ContactBookError)`。
- 用一个 `Timer` 上下文管理器（第5天扩展）包裹加载/保存操作，并打印I/O耗时。
- 为 `ContactBook` 添加 `__repr__`/`__str__`，使其显示联系人数量（第3天内容）。

---

## 🚀 Submit
> 🇨🇳 **🚀 提交**

```bash
git add week01/day06_miniproject
git commit -m "add: Week1 D6 CLI contact book mini-project"
git push
```
> 🇨🇳 *[用于提交项目的Git命令]*

Then tell me **"Week 1 done"** (or send the repo link). I'll review against the rubric, write your **Week-1 retro**, mark Week 1 ✅ in the study plan, and open **Week 2 — NumPy**. 🎉
> 🇨🇳 然后告诉我**"第一周完成"**（或发仓库链接）。我会对照评分标准进行审查，为你撰写**第一周回顾**，在学习计划中标记第一周 ✅，并开启**第二周 — NumPy**。🎉
