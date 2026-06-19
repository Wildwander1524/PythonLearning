# ✅ Day 6 — SOLUTIONS (cumulative answer key + capstone notes)
> 🇨🇳 **[Day 6 — 解决方案（累积答案要点 + 项目笔记）]**

> Open only after attempting [`RECALL.md`](./RECALL.md) and the capstone.
> 🇨🇳 仅限在尝试了 [`RECALL.md`](./RECALL.md) 和项目实践之后打开。

## Part 1 · Concept answers
> 🇨🇳 **第一部分 · 概念答案**

1. **Instance** = per-object state (`self.x`); **class** = one shared copy (`Cls.count`). Shared
   constants/counters → class; per-object data → instance.
> 🇨🇳 **实例** = 每个对象的状态（`self.x`）；**类** = 一份共享副本（`Cls.count`）。共享常量/计数器应使用类变量；每个对象的数据应使用实例变量。

2. Method exposed as a controlled attribute — encapsulation/validation *without* changing caller
   syntax (`obj.balance`, not `obj.get_balance()`). Omitting the setter makes it read-only.
> 🇨🇳 以受控属性的方式暴露方法——在不改变调用者语法的情况下实现封装/验证（`obj.balance`，而不是 `obj.get_balance()`）。省略 setter 可使其只读。

3. So callers can't mutate your internal list and silently corrupt state.
> 🇨🇳 这样调用者就无法修改你的内部列表并悄无声息地破坏状态。

4. Inheritance for genuine **is-a** subtypes (and ABCs/framework bases); composition for **has-a**
   and assembling behaviour. Default to composition.
> 🇨🇳 继承用于真正的 **is-a** 子类型（以及 ABC/框架基类）；组合用于 **has-a** 和组装行为。默认选择组合。

5. Runs the parent's initializer so inherited attributes exist; skip it → `AttributeError` later.
> 🇨🇳 运行父类的初始化器，使继承的属性得以存在；跳过它 → 后续出现 `AttributeError`。

6. A class that can't be instantiated and forces `@abstractmethod`s; a subclass skipping one
   **can't be instantiated** (`TypeError`) — fails early and loudly.
> 🇨🇳 一个无法实例化且强制要求实现 `@abstractmethod` 的类；子类若跳过任何一个抽象方法，**将无法实例化**（`TypeError`）——尽早并明显地失败。

7. `super()` → **the next class in the MRO** (possibly a *sibling* in multiple inheritance). MRO =
   the fixed, left-to-right, deduplicated ancestor order (`Cls.__mro__`), via C3 linearization.
   Bonus: `D.__mro__ = (D, B, C, A, object)`.
> 🇨🇳 `super()` → 指向 **MRO 中的下一个类**（多重继承时可能是*兄弟类*）。MRO = 固定的、从左到右、去重后的祖先顺序（`Cls.__mro__`），通过 C3 线性化得出。附加：`D.__mro__ = (D, B, C, A, object)`。

8. `__repr__` → REPL/debugger/containers (**always**); `__str__` → `print`/users (when it
   differs). `__str__` falls back to `__repr__`, not vice-versa.
> 🇨🇳 `__repr__` → 用于 REPL/调试器/容器（**始终**）；`__str__` → 用于 `print`/用户（当其不同时）。`__str__` 会回退到 `__repr__`，而不是相反。

9. `__iter__` (best a generator) **or** `__getitem__` indexed `0,1,2…` until `IndexError`.
> 🇨🇳 `__iter__`（最好是一个生成器）**或者** 通过 `__getitem__` 按索引 `0,1,2…` 取值直到 `IndexError`。

10. A **new** object — operators must not mutate operands.
> 🇨🇳 一个**新**对象——运算符不应改变操作数。

11. `__eq__` sets `__hash__ = None` (equal must hash equal; Python can't verify your logic).
    Immutable → add `__hash__`; mutable → leave unhashable.
> 🇨🇳 `__eq__` 会将 `__hash__` 设为 `None`（相等的对象必须拥有相等的哈希；Python 无法验证你的逻辑）。不可变对象 → 添加 `__hash__`；可变对象 → 保持不可哈希。

12. The default list is created **once at `def`-time** and shared across calls → accumulates. Fix:
    default `None`, create inside.
> 🇨🇳 默认列表在**函数定义时创建一次**，并在多次调用中共享 → 会不断累积。修正方法：默认值设为 `None`，在函数内部创建。

13. For data-holding classes (auto `__init__`/`__repr__`/`__eq__`). Mutable default →
    `field(default_factory=list)`, never `= []`.
> 🇨🇳 用于数据持有类（自动生成 `__init__`/`__repr__`/`__eq__`）。可变默认值 → 使用 `field(default_factory=list)`，绝不能 `= []`。

14. Trades dynamic attributes (no per-instance `__dict__`) for lower memory + slightly faster
    access; worth it only with very many instances + a profiler's say-so.
> 🇨🇳 以牺牲动态属性（没有每个实例的 `__dict__`）为代价，换取更低的内存占用和稍快的访问速度；只有在实例数量非常多且有性能分析结果支持时才值得。

15. `except` on a matching raise; `else` only if try raised nothing; `finally` always.
> 🇨🇳 `except` 在匹配的异常抛出时执行；`else` 仅当 try 块未引发任何异常时执行；`finally` 总是执行。

16. Guaranteed setup *and* teardown even on error; `__enter__` and `__exit__`.
> 🇨🇳 即使在出错时也能保证初始化和清理工作；即 `__enter__` 和 `__exit__`。

17. An `__init__.py` makes it a package; the `__main__` guard runs a block only when executed
    directly, not imported.
> 🇨🇳 `__init__.py` 使其成为一个包；`__main__` 保护块仅在直接执行时运行，导入时不运行。

## Part 2 · Math answers
> 🇨🇳 **第二部分 · 数学答案**

1. `[6, 4]` · 2. `[3, -6]` · 3. `2+0+2 = 4` · 4. `√(36+64) = 10` · 5. `√(3²+4²) = 5` ·
6. `1/(1·√2) = 1/√2 ≈ 0.707` · 7. `[[1,3,5],[2,4,6]]`, shape `2×3` · 8. `[50, 110]` ·
9. `[[2,8],[1,19]]` (inner `2=2` → `2×2`) · 10. `7·[1,0] + (-2)·[0,1]` · 11. **dependent**
(`[2,4]=2·[1,2]`); span = the line through `[1,2]`, not the plane · 12. unchanged `[[1,2],[3,4]]`.
> 🇨🇳 1. `[6, 4]` · 2. `[3, -6]` · 3. `2+0+2 = 4` · 4. `√(36+64) = 10` · 5. `√(3²+4²) = 5` · 6. `1/(1·√2) = 1/√2 ≈ 0.707` · 7. `[[1,3,5],[2,4,6]]`，形状 `2×3` · 8. `[50, 110]` · 9. `[[2,8],[1,19]]`（内层 `2=2` → `2×2`）· 10. `7·[1,0] + (-2)·[0,1]` · 11. **线性相关**（`[2,4]=2·[1,2]`）；张成的空间是穿过 `[1,2]` 的直线，而非平面 · 12. 不变，仍为 `[[1,2],[3,4]]`。

---

## Part 3 · Capstone reference notes — CLI contact book
> 🇨🇳 **第三部分 · 项目参考笔记——CLI 联系人簿**

Full spec/rubric in [`HOMEWORK.md`](./HOMEWORK.md). Key shapes (don't peek until you've built it):
> 🇨🇳 完整规范/评分标准见 [`HOMEWORK.md`](./HOMEWORK.md)。关键结构（搭建完成前不要偷看）：

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
> 🇨🇳 *[联系人簿核心模型、自定义异常层次结构及 CRUD 持久化实现]*

**Rubric self-check:** `Contact` is a `@dataclass` (D4) · custom exception hierarchy raised in the
book and **caught in the CLI loop** (D2+D5) · `_contacts` encapsulated, CRUD validated (D1) ·
`__len__`/`__iter__` (D3) · JSON save/load via `with` (D5) · clean package + `__init__.py` (D5) ·
tests incl. **save→load round-trip** · README + concept checks · pushed.
> 🇨🇳 **评分自查：** `Contact` 是 `@dataclass`（D4）· 自定义异常层次结构在簿子中引发，并在 **CLI 循环中被捕获**（D2+D5）· `_contacts` 封装，CRUD 验证（D1）· `__len__`/`__iter__`（D3）· 通过 `with` 进行 JSON 保存/加载（D5）· 整洁的包结构 + `__init__.py`（D5）· 测试包括 **保存→加载往返测试** · README + 概念检查 · 已推送。

### Capstone concept-check answers
> 🇨🇳 **项目概念检查答案**

1. The context manager (`with open(...)`) guarantees the file is flushed/closed on every path in
   `save`/`load`; without it a mid-write error could leave a truncated or locked file.
> 🇨🇳 上下文管理器（`with open(...)`）保证在 `save`/`load` 的每条路径上文件都会被刷新/关闭；若没有它，写入中途出错可能会留下不完整或被锁定的文件。

2. Catch `ContactBookError` (the base) in the outer CLI loop so *any* domain error becomes a
   friendly message — you raise specific subclasses but the loop handles the whole category
   (raise early, catch late).
> 🇨🇳 在外层 CLI 循环中捕获 `ContactBookError`（基类），这样*所有*领域错误都会变成友好的消息——你在具体位置抛出特定子类，而循环处理整个类别（尽早抛出，延迟捕获）。

3. `all()` returning a sorted **copy** protects the Day-1 encapsulation lesson: callers iterating
   or sorting the result can't mutate the live `_contacts` store.
> 🇨🇳 `all()` 返回一个排序后的**副本**，保护了 Day-1 的封装原则：调用者对结果进行迭代或排序时，无法改变实时的 `_contacts` 存储。

> 📝 When done, tell me **"Week 1 done"** (or send the repo link). I'll grade against the rubric,
> write the Week-1 retro, mark Week 1 ✅, update your ability boundary, and open **Week 2 — NumPy**.
> 🇨🇳 📝 完成后，告诉我 **"Week 1 done"**（或发送仓库链接）。我会根据评分标准评分，撰写 Week 1 回顾，标记 Week 1 ✅，更新你的能力边界，并开启 **Week 2 — NumPy**。
