# 📘 Day 5 — Errors, Context Managers & Modules
> 🇨🇳 **📘 第5天 — 错误处理、上下文管理器与模块**

> **Week 1 · Fri 2026-06-20** · Curriculum: Python OOP · Math: linear combinations & span
> Today is about **robustness** — code that survives contact with the real world (files fail,
> users type nonsense). Amateur code assumes success; professional code plans for failure.
> 🇨🇳 **第1周 · 2026年6月20日 周五** · 课程：Python面向对象编程 · 数学：线性组合与张成空间
> 🇨🇳 今天关注**健壮性**——代码在面对现实世界（文件失败、用户输入荒谬内容）时仍能存活。业余代码假设一切顺利；专业代码为失败做准备。

## 🎯 Objectives & mastery bar
> 🇨🇳 **目标与掌握标准**

| Objective | Bloom | Mastered when… |
|-----------|-------|----------------|
| Build a custom **exception hierarchy** | Create | a caller can catch by category or specifics |
| Write a context manager (`__enter__`/`__exit__`) | Apply | the resource releases even when the block raises |
| Organize code into modules/packages | Understand | you explain `__init__.py` and the `__name__` guard |
| Math: linear combinations & span | Understand | you decide if a vector is reachable / independent |

| 目标 | Bloom层级 | 掌握标准 |
|------|-----------|----------|
| 构建自定义**异常层次结构** | 创建 | 调用者可按类别或具体类型捕获 |
| 编写上下文管理器（`__enter__`/`__exit__`） | 应用 | 即使代码块抛出异常，资源也能释放 |
| 将代码组织为模块/包 | 理解 | 你能解释 `__init__.py` 和 `__name__` 守卫 |
| 数学：线性组合与张成空间 | 理解 | 你能判断向量是否可到达/独立 |

## 🔁 Spaced callbacks (cold, first — re-tests D1, D3, D4)
> 🇨🇳 **间隔回调（冷启动，首次 — 重测 D1、D3、D4）**

C1 (D1) why raise `ValueError` on bad input *immediately*? C2 (D3) the data model — what fires on
`for x in obj`? C3 (D4) the mutable-default trap — what's shared and when is it created?
> 🇨🇳 C1 (D1) 为什么在输入错误时*立即*抛出 `ValueError`？C2 (D3) 数据模型——`for x in obj` 时会触发什么？C3 (D4) 可变默认值陷阱——共享的是什么，何时创建？

"""
Spaced callbacks Answer:
C1:because program catch the error by Error Words,such as "try ... except ...","if ... raise ..."
C2:first creat a generator it1 = iter(obj),then it1 outputs items one by one through the method " __iter__ __next__","__iter__ yield func" or "__getitem__"
C3:mutable default value shares a common address which all instance point to it.its created when instant first time  
"""

---

## S1 — Exceptions
> 🇨🇳 **S1 — 异常**

### LBYL vs EAFP (the mindset before the syntax)
> 🇨🇳 **LBYL vs EAFP（语法前的思维方式）**

| Style | Shape | Example |
|-------|-------|---------|
| **LBYL** "look before you leap" | check first, then act | `if k in d: use(d[k])` |
| **EAFP** "easier to ask forgiveness" | act, handle failure | `try: use(d[k]) except KeyError: ...` |

| 风格 | 形状 | 示例 |
|------|------|------|
| **LBYL** "三思而后行" | 先检查，再行动 | `if k in d: use(d[k])` |
| **EAFP** "道歉比请求许可更容易" | 行动，处理失败 | `try: use(d[k]) except KeyError: ...` |

> 🍳 LBYL inspects every egg in a separate bowl; EAFP cracks straight in and deals with a bad one.
> **Python favors EAFP** — cleaner, and no race condition between check and use.
> 🇨🇳 🍳 LBYL 像把每个鸡蛋分别打在碗里检查；EAFP 直接敲开处理坏的。
> 🇨🇳 **Python 偏好 EAFP**——更简洁，且检查与使用之间没有竞态条件。

```python
try:
    risky()
except ValueError as e:           # SPECIFIC (most specific first); never bare except:
    handle(e)
else:                             # runs only if try raised nothing
    on_success()
finally:                         # ALWAYS runs — cleanup on every path
    cleanup()
```
> 🇨🇳 *[展示 `try-except-else-finally` 的完整结构：优先捕获具体异常，`else` 在无异常时运行，`finally` 始终执行]*

> 🪂 **`finally` = the auto-deploy parachute** — runs whether you succeeded, failed, or bailed
> with a `return`. Close files / release locks here.
> 🎣 **Never bare `except:`** — it scoops up `KeyboardInterrupt` and real bugs. Catch the specific
> thing you can handle; let the rest propagate.
> 🇨🇳 🪂 **`finally` = 自动部署的降落伞**——无论成功、失败还是通过 `return` 跳出，都会运行。在这里关闭文件/释放锁。
> 🇨🇳 🎣 **绝不要使用裸 `except:`** ——它会捕获 `KeyboardInterrupt` 和真正的错误。只捕获你能处理的具体异常；让其他异常继续传播。

### Exception hierarchy — exceptions are objects in an inheritance tree (Day 2 pays off)
> 🇨🇳 **异常层次结构——异常是继承树上的对象（第2天知识兑现）**

```text
BaseException → Exception → LookupError → {KeyError, IndexError}
```
> 🇨🇳 *[异常继承层次：`BaseException` 是所有异常的根，`LookupError` 下包含 `KeyError` 和 `IndexError`]*

`except LookupError:` catches both children — polymorphism applied to errors.
> 🇨🇳 `except LookupError:` 会捕获两个子类——将多态用于错误处理。

### Custom exceptions — your own error vocabulary
> 🇨🇳 **自定义异常——属于你自己的错误词汇表**

```python
class BankError(Exception): ...                  # base for ALL banking errors
class InsufficientFundsError(BankError):
    def __init__(self, balance, requested):
        self.balance, self.requested = balance, requested      # carry DATA, not just a message
        super().__init__(f"need {requested}, have {balance}")
```
> 🇨🇳 *[自定义异常继承自 `Exception`，携带余额与请求金额等数据，而非仅消息文本]*

```python
try: account.withdraw(1000)
except InsufficientFundsError as e: offer_overdraft(e.balance, e.requested)   # specific
except BankError: log_and_alert()                                            # OR broad
```
> 🇨🇳 *[捕获具体 `InsufficientFundsError` 时提供透支建议；捕获更宽泛的 `BankError` 则记录并报警]*

> 🏷️ **Labeled fuse box.** A bare `Exception` is one master breaker ("something tripped"). A
> hierarchy is a labeled panel — catch *exactly* the circuit, or the whole "banking" section.
> **Two pro habits:** *raise early, catch late* (raise at the cause; handle where you know what to
> do); *let exceptions carry data* so handlers decide from structure, not string-parsing.
> 🇨🇳 🏷️ **贴了标签的保险丝盒。** 一个裸 `Exception` 就像主断路器（"有东西跳闸了"）。而层次结构是一个贴了标签的面板——你可以*精准*捕获某个电路，或者整个"银行"区域。
> 🇨🇳 **两个专业习惯：** *早抛出，晚捕获*（在原因发生处抛出；在知道如何处理的地方捕获）；*让异常携带数据*，这样处理器基于结构做决策，而不是解析字符串。

> ✍️ **Self-explain (interleave D2):** why is `class InsufficientFundsError(BankError)` a
> *correct* use of inheritance, when Day 4 warned against `Stack(list)`? *(It's genuine is-a — an
> `InsufficientFundsError` **is a** `BankError`, usable anywhere the base is caught. `Stack` is
> not a `list`.)*
> 🇨🇳 ✍️ **自我解释（穿插第2天）：** 为什么在第4天警告不要使用 `Stack(list)` 时，`class InsufficientFundsError(BankError)` 却是正确的继承用法？*(这是真正的"是一个"关系——`InsufficientFundsError` **是一个** `BankError`，可在任何捕获基类的地方使用。`Stack` 不是一个 `list`。)*

---

## S2 — Context managers & modules
> 🇨🇳 **S2 — 上下文管理器与模块**

### Context managers — guaranteed setup *and* teardown
> 🇨🇳 **上下文管理器——确保初始化*和*清理**

Some resources *must* be released (files, locks, connections). A context manager guarantees it,
even if the block explodes.
> 🇨🇳 有些资源*必须*释放（文件、锁、连接）。上下文管理器即使在代码块崩溃时也能保证这一点。

```python
class Timer:
    def __enter__(self):
        self.t = time.perf_counter(); return self      # bound to the `as` variable
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{time.perf_counter()-self.t:.4f}s")
        return False                                    # False = don't suppress exceptions (default)
with Timer():
    work()
```
> 🇨🇳 *[自定义计时器上下文管理器：`__enter__` 记录开始时间并返回自身给 `as`；`__exit__` 打印耗时并返回 `False` 以传播异常]*

> 🚗 **A rental car that returns itself.** `__enter__` = pick up keys; the block = your trip;
> `__exit__` = the car drives *itself* back and settles the bill — even after a breakdown.
> 🇨🇳 🚗 **一辆会自己归还的租车。** `__enter__` = 取钥匙；代码块 = 你的旅程；`__exit__` = 车*自己*开回来并结账——即使途中出了故障。

| `__exit__` param | block succeeded | block raised |
|------------------|-----------------|--------------|
| `exc_type/val/tb` | all `None` | the class / instance / traceback |
| **returns** `False`/`None` | — | exception **propagates** (right default) |
| **returns** `True` | — | exception **suppressed** (rare, deliberate) |

| `__exit__` 参数 | 模块成功 | 模块抛出异常 |
|-----------------|---------|-------------|
| `exc_type/val/tb` | 全部为 `None` | 异常类/实例/回溯 |
| **返回** `False`/`None` | — | 异常**传播**（正确默认值） |
| **返回** `True` | — | 异常**被抑制**（罕见，有意为之） |

> 🔬 PyTorch's `with torch.no_grad():` is exactly this — disables gradient tracking on enter,
> restores it on exit even if inference errors. You'll recognize it in Week 8.
> 💡 Shortcut: `@contextlib.contextmanager` + a generator (`yield` splits enter/exit). Learn the
> class form first (you'll *see* `__enter__`/`__exit__` in libraries).
> 🇨🇳 🔬 PyTorch 的 `with torch.no_grad():` 正是如此——进入时禁用梯度跟踪，退出时恢复，即使推理出错。你会在第8周认出它。
> 🇨🇳 💡 捷径：`@contextlib.contextmanager` + 生成器（`yield` 分隔进入/退出）。先学类形式（你会在库中*看到* `__enter__`/`__exit__`）。

### Modules & packages
> 🇨🇳 **模块与包**

| Thing | What | Analogy |
|-------|------|---------|
| module | one `.py` file | a labeled tool |
| package | a folder + `__init__.py` | a labeled drawer |

| 事物 | 是什么 | 类比 |
|------|--------|------|
| 模块 | 一个 `.py` 文件 | 贴了标签的工具 |
| 包   | 一个文件夹 + `__init__.py` | 贴了标签的抽屉 |

```python
# mypackage/__init__.py — the "front desk": curate the public API
from .core import MainClass
# elsewhere:  from mypackage import MainClass
```
> 🇨🇳 *[包的 `__init__.py` 充当"前台"：整理公共 API，`from .core import MainClass` 然后外部 `from mypackage import MainClass`]*

> 🍞 **Import runs once, then caches** (`sys.modules`): the first import executes the file
> top-to-bottom; later imports take a slice of the same loaf. Side effects happen once.
> 🎭 **`if __name__ == "__main__":`** runs a block only when the file is *executed directly*
> (`__name__ == "__main__"`), not when imported (`__name__ == "core"`). One file = reusable
> module *and* runnable script.
> 🇨🇳 🍞 **导入只运行一次，然后缓存**（`sys.modules`）：第一次导入会从头到尾执行文件；之后的导入会从同一块面包上切下薄片。副作用只发生一次。
> 🇨🇳 🎭 **`if __name__ == "__main__":`** 只在文件*直接执行*时运行代码块（`__name__ == "__main__"`），导入时不会运行（`__name__ == "core"`）。一个文件 = 可重用模块*又*是可运行脚本。

---

## S3 — Math: linear combinations & span
> 🇨🇳 **S3 — 数学：线性组合与张成空间**

**Linear combination** = scale each vector, add: `a·v₁ + b·v₂`. e.g. `2·[1,0]+3·[0,1]=[2,3]`.
🎨 Mixing paint: `[1,0]`=red, `[0,1]`=blue; dial `a`,`b` to mix any purple.
> 🇨🇳 **线性组合** = 缩放每个向量，再加起来：`a·v₁ + b·v₂`。例如 `2·[1,0]+3·[0,1]=[2,3]`。
> 🇨🇳 🎨 调色盘：`[1,0]`=红色，`[0,1]`=蓝色；调节 `a`、`b` 可混合出任何紫色。

**Span** = every point reachable by *some* linear combination.
- `span([1,0],[0,1])` = the whole plane (a **basis**).
- `span([1,1])` = just the diagonal line.
- `span([1,0],[2,0])` = only the x-axis — `[2,0]` adds no new direction (**linearly dependent**).
> 🇨🇳 **张成空间** = 通过*某种*线性组合可以到达的所有点。
> - `span([1,0],[0,1])` = 整个平面（一个**基**）。
> - `span([1,1])` = 仅对角线。
> - `span([1,0],[2,0])` = 仅 x 轴——`[2,0]` 没有增加新方向（**线性相关**）。

> 🗺️ Two roads pointing genuinely different ways reach anywhere; a "second" road parallel to the
> first adds nothing. **Span = all destinations; independence = does each vector open a new
> direction.**
> 🚀 Embeddings (Week 10) live in high-D spaces — "what can these vectors represent?" is a *span*
> question; "are these features redundant?" is *linear dependence* — the seed of **PCA** (Week 6),
> which keeps the informative directions and drops the redundant ones.
> 🇨🇳 🗺️ 两条指向真正不同方向的路，可以到达任何地方；一条与第一条平行的"第二条"路毫无用处。**张成空间 = 所有目的地；独立性 = 每个向量是否开辟了新方向。**
> 🇨🇳 🚀 嵌入（第10周）存在于高维空间——"这些向量能表示什么？"是一个*张成*问题；"这些特征是否冗余？"是*线性相关性*问题——这正是**PCA**（第6周）的种子，它保留信息丰富的方向，丢弃冗余的方向。

> 🔮 ① write `[5,7]` as a combo of `[1,0]`,`[0,1]`. ② is `[3,4]` in `span([1,1])`? ③ do `[1,1]`
> and `[2,2]` span the plane? *(① `5·[1,0]+7·[0,1]`. ② no — not on the diagonal. ③ no — dependent,
> they span only the diagonal line.)*
> 🇨🇳 🔮 ① 将 `[5,7]` 表示为 `[1,0]` 和 `[0,1]` 的组合。② `[3,4]` 是否在 `span([1,1])` 中？③ `[1,1]` 和 `[2,2]` 能否张成整个平面？*(① `5·[1,0]+7·[0,1]`。② 不在——不在对角线上。③ 不能——线性相关，它们仅张成对角线。)*

---

## S4 — 📰 Weekly AI Industry Digest #1 (condensed)
> 🇨🇳 **S4 — 📰 每周 AI 行业摘要 #1（精简版）**

> Your Friday frontier slot trains *staying oriented* — read like a trader skims the morning
> market summary: fast, deciding "does this change what I'm building?" *(A cloud routine
> auto-posts the canonical Digest #N to the study plan every Friday 09:00 CST; treat that as
> authoritative when it lands. Full version: study-plan §"Weekly AI Industry Digests".)*
> 🇨🇳 每周五的前沿时段训练你*保持方向感*——就像交易员快速浏览早间市场摘要：迅速判断"这会影响我正在构建的东西吗？"*（云端例程会在每周五上午09:00 CST自动将官方摘要#N发布到学习计划上；当它出现时，将其视为权威版本。完整版：学习计划 §"每周AI行业摘要"。）*

**Macro pattern (mid-2026):** multimodal is now *default*; reasoning models trade speed for
accuracy; **efficiency** (same quality, far less compute) is the relentless theme — which is
*precisely why your 3 directions exist*.
> 🇨🇳 **宏观模式（2026年中）：** 多模态现在是*默认设置*；推理模型以速度换精度；**效率**（相同质量，少得多的计算）是无情的主题——这*正是你三个方向存在的原因*。

| Your direction | 2026 snapshot | Takeaway |
|----------------|---------------|----------|
| 🥇 **Inference accel** | vLLM = flexible default (PagedAttention); TensorRT-LLM = peak NVIDIA throughput (~15–30% faster on H100, ~28-min compile); SGLang rising | Week-9 plan (vLLM → TensorRT-LLM) matches industry; you're aimed right |
| 📱 **Edge multimodal** | small VLMs (<10B) a defined trend; Apple FastVLM/MobileCLIP the latency reference | your industrial/Germany differentiator; hands-on Week 11 |
| 🎬 **Video understanding** | long-video models (token-merge, memory-streaming); still emerging | correct as your *elective* (one Week-12 project) |

| 你的方向 | 2026年快照 | 关键启示 |
|----------|------------|----------|
| 🥇 **推理加速** | vLLM = 灵活默认（PagedAttention）；TensorRT-LLM = 峰值NVIDIA吞吐（H100上快约15–30%，编译约28分钟）；SGLang 在崛起 | 第9周计划（vLLM → TensorRT-LLM）与行业吻合；你瞄准正确 |
| 📱 **边缘多模态** | 小型 VLM（<10B）是明确趋势；Apple FastVLM/MobileCLIP 是延迟参考 | 你的工业/德国差异化方向；第11周动手实践 |
| 🎬 **视频理解** | 长视频模型（token合并、内存流式处理）；仍在兴起 | 作为你的*选修*（一个第12周项目）是正确的 |

> ✍️ **Reflection (write it):** ① which direction excites you most, and does it still fit your
> industrial/Germany goal? ② in 2–3 sentences, how does the *efficiency* theme strengthen your
> inference+edge focus? ③ one sentence: what would your Week-13 capstone demo?
> 🇨🇳 ✍️ **反思（写下来）：** ① 哪个方向最让你兴奋，并且它仍然符合你的工业/德国目标吗？② 用2-3句话，*效率*主题如何增强你对推理+边缘的关注？③ 一句话：你的第13周毕业项目演示会是什么？

---

## 🧠 Cheat-sheet
> 🇨🇳 **🧠 速查表**

```python
try: ...
except ValueError as e: ...     # specific; never bare except:
else: ...                       # only if no exception
finally: ...                    # always (the parachute)
class MyError(Exception): ...   # custom = inheritance; build a hierarchy, carry data
class Resource:
    def __enter__(self): return self
    def __exit__(self, et, ev, tb): return False   # don't suppress
if __name__ == "__main__": ...  # runs only when executed directly
# linear combo: a·v₁+b·v₂ ;  span = all reachable combos ;  dependent = adds no new direction
```
> 🇨🇳 *[Python错误处理、上下文管理器、模块入口、线性代数核心速查]*

| Term | One-liner | Analogy |
|------|-----------|---------|
| EAFP | try first, catch failure | crack the egg, handle a bad one |
| `finally` | always-run cleanup | auto-deploy parachute |
| exception hierarchy | catch parent → catch children | labeled fuse box |
| context manager | guaranteed setup/teardown | self-returning rental car |
| `__exit__` → True | suppress the exception (rare) | — |
| package | folder + `__init__.py` | labeled drawer + index card |
| import cache | module runs once | one loaf, many slices |
| span | all reachable combinations | all destinations your roads reach |

| 术语 | 一句话概括 | 类比 |
|------|-----------|------|
| EAFP | 先尝试，失败则捕获 | 敲开鸡蛋，处理坏的那个 |
| `finally` | 总要运行的清理 | 自动部署的降落伞 |
| 异常层次结构 | 捕获父类 → 捕获子类 | 贴了标签的保险丝盒 |
| 上下文管理器 | 保证的初始化/拆卸 | 会自己归还的租车 |
| `__exit__` 返回 True | 抑制异常（罕见） | — |
| 包 | 文件夹 + `__init__.py` | 贴了标签的抽屉 + 索引卡 |
| 导入缓存 | 模块只运行一次 | 一块面包，很多薄片 |
| 张成空间 | 所有可达组合 | 你的道路可到达的所有目的地 |

## ⚠️ Common pitfalls
> 🇨🇳 **⚠️ 常见陷阱**

1. **Bare `except:`** → swallows Ctrl-C and bugs. Be specific.
2. **Exceptions for normal control flow** → they're for the *exceptional*.
3. **Cleanup in the `try` body** → leaks if it raises first. Use `finally` or `with`.
4. **Missing `__init__.py`** → folder isn't a package; imports fail.
5. **Accidental `return True` from `__exit__`** → silently hides every error.
6. **"linearly dependent" = "useless"** → it adds no new *direction*, but redundancy is exactly what PCA exploits.
> 🇨🇳 1. **裸 `except:`** → 吞掉 Ctrl-C 和错误。请具体捕获。
> 🇨🇳 2. **将异常用于正常控制流程** → 异常是为*异常情况*准备的。
> 🇨🇳 3. **在 `try` 主体中进行清理** → 如果它先引发异常，会造成泄漏。请使用 `finally` 或 `with`。
> 🇨🇳 4. **缺少 `__init__.py`** → 文件夹不算包；导入会失败。
> 🇨🇳 5. **意外在 `__exit__` 中返回 `True`** → 会静默隐藏每个错误。
> 🇨🇳 6. **"线性相关" = "无用"** → 它没有增加新*方向*，但冗余正是 PCA 利用的东西。

## ✅ Storage-strength check (cold, tomorrow)
> 🇨🇳 ✅ **存储强度检查（冷启动，明天）**

Write a 3-level exception hierarchy + a `with`-managed resource that closes on error; explain the
`__name__` guard; decide if `[1,2]`,`[2,4]` span the plane. Shaky → log it.
> 🇨🇳 编写一个3层异常层次结构 + 一个 `with` 托管的资源，在出错时关闭；解释 `__name__` 守卫；判断 `[1,2]`、`[2,4]` 是否能张成平面。摇晃 → 记录下来。

➡️ **Build it:** [`HOMEWORK.md`](./HOMEWORK.md) — a context-managed `FileLogger` (prove it closes
the file *even on error*) shipped as an importable `logkit` package. Connect each piece:
custom exceptions = D2 inheritance; `__enter__`/`__exit__` = the rental car; `__init__.py` = the
drawer's index card.
> 🇨🇳 ➡️ **动手构建：** [`HOMEWORK.md`](./HOMEWORK.md) — 一个上下文托管的 `FileLogger`（证明即使在出错时也能关闭文件），作为一个可导入的 `logkit` 包发布。连接每个部分：自定义异常 = D2 继承；`__enter__`/`__exit__` = 租车；`__init__.py` = 抽屉的索引卡。
