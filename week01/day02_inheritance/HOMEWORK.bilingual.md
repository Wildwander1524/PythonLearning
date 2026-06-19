# 📝 Day 2 Homework — Animal hierarchy + Shape ABC (calibrated rebuild) / 第二天作业 — 动物层次结构 + 形状抽象基类（校准重构）

> **Goal:** prove inheritance, `super()`, the **MRO**, override flavours, polymorphism, and ABCs by building two class families + tests.
> 🇨🇳 **目标：** 通过构建两个类族及测试，验证继承、`super()`、**MRO (方法解析顺序)**、覆盖方式、多态以及 ABC (抽象基类) 的使用。
> **Time:** 3 h · **Read first:** [`LESSON.md`](./LESSON.md)
> 🇨🇳 **时间：** 3 小时 · **先读：** [`LESSON.md`](./LESSON.md)
> **Calibration:** your prior version was 18/22. The four fails (Heron, circle `/2`, `fetch` ignoring `item`, `super(Bird,self)`) are now *baseline* — and there's a new **MRO-prediction** requirement targeting edge E3.
> 🇨🇳 **校准说明：** 你之前的版本得了 18/22 分。四个失败点（Heron 公式、圆的面积错误地除以 2、`fetch` 忽略了 `item`、`super(Bird,self)`）现在作为*基线*——并且新增了一项针对边界情况 E3 的 **MRO 预测**要求。

## 📖 Before you code / 开始编码前
Re-read the spec **twice** (E1). For each override, decide **extend vs replace** and label it. For each `__init__`, the rule is `super().__init__(...)` with **no args** unless you can state exactly why not.
> 🇨🇳 将规范**读两遍** (E1)。每一次覆盖都要判断是**扩展 (extend)** 还是**替换 (replace)** 并标注。对于每个 `__init__`，规则是使用 `super().__init__(...)` 并**不传多余参数**，除非你能说出确切的原因。

## Part A — `animals.py` / A 部分 — `animals.py`
```text
Animal
├── Dog     "Woof",  fetch(item)
├── Cat     "Meow",  purr()
└── Bird    "Tweet", fly(altitude)
    └── Parrot  "Squawk", learn(phrase) → repeat it
```
> 🇨🇳 动物类的层次结构示意：Animal 是基类，下分 Dog（“Woof”，有 fetch(item) 方法）、Cat（“Meow”，有 purr() 方法）、Bird（“Tweet”，有 fly(altitude) 方法），Bird 下再有 Parrot（“Squawk”，有 learn(phrase) 方法并重复它）。

- [ ] `Animal.__init__(self, name, sound)`; **every** subclass calls `super().__init__(...)`.
> 🇨🇳 `Animal.__init__(self, name, sound)`；**每个**子类都要调用 `super().__init__(...)`。
- [ ] Override `speak()` in ≥3 subclasses; ≥1 must be **EXTEND** and labelled `# EXTEND`.
> 🇨🇳 在至少 3 个子类中覆盖 `speak()` 方法；至少一个是**扩展 (EXTEND)** 类型的覆盖并标注 `# EXTEND`。
- [ ] `Dog.fetch(item)` output **must contain `item`**. *(E1)*
> 🇨🇳 `Dog.fetch(item)` 的输出**必须包含 `item`**。*(E1)*
- [ ] `Parrot.__init__(self, name)` uses **`super().__init__(name)`** then `self.sound = "Squawk"` — **not** `super(Bird, self)`. *(E3 — the exact fix.)*
> 🇨🇳 `Parrot.__init__(self, name)` 应使用 **`super().__init__(name)`**，然后设置 `self.sound = "Squawk"` —— **不要**使用 `super(Bird, self)`。*(E3 — 准确的修复方式。)*
- [ ] **MRO requirement (E3):** in a comment, **write your predicted `Parrot.__mro__` first**, then print it and confirm.
> 🇨🇳 **MRO (方法解析顺序) 要求 (E3)：** 在注释中**首先写出你预测的 `Parrot.__mro__`**，然后实际打印并确认。

## Part B — `shapes.py` / B 部分 — `shapes.py`
- [ ] `Shape(ABC)` with `@abstractmethod area()` + `perimeter()`, concrete `describe()`.
> 🇨🇳 `Shape(ABC)` 需包含 `@abstractmethod area()` 和 `@abstractmethod perimeter()`，以及一个具体方法 `describe()`。
- [ ] `Circle(r)` — `area = πr²` (**no `/2`**). `Rectangle(w,h)`, `Triangle(a,b,c)`.
> 🇨🇳 `Circle(r)` — `area = πr²` (**不要除以 2**)。`Rectangle(w,h)`、`Triangle(a,b,c)`。
- [ ] `Triangle.area` uses **Heron's formula** — *not* `math.hypot`. For 3-4-5 it must give **6.0**. *(E2)*
> 🇨🇳 `Triangle.area` 使用**海伦公式 (Heron's formula)** —— *不要*用 `math.hypot`。对于 3-4-5 的三角形，结果必须是 **6.0**。*(E2)*
- [ ] `total_area(shapes)` summing via polymorphism — **zero `isinstance`**.
> 🇨🇳 `total_area(shapes)` 通过多态求和 —— **不允许使用 `isinstance`**。
- [ ] `Shape()` directly raises `TypeError`.
> 🇨🇳 直接实例化 `Shape()` 会触发 `TypeError`。

## Part C — `test_day02.py` / C 部分 — `test_day02.py`
Cover at least: `Dog("Rex").fetch("ball")` contains `"ball"` · **`Parrot.__mro__ == (Parrot, Bird, Animal, object)`** · `Circle(1).area()≈π` · `Triangle(3,4,5).area()==6.0` · `total_area([Circle(1),Rectangle(2,3)])≈9.1416` (tol `1e-6`) · `Shape()` raises `TypeError`.
> 🇨🇳 至少覆盖以下测试：`Dog("Rex").fetch("ball")` 包含 `"ball"` · **`Parrot.__mro__ == (Parrot, Bird, Animal, object)`** · `Circle(1).area()≈π` · `Triangle(3,4,5).area()==6.0` · `total_area([Circle(1),Rectangle(2,3)])≈9.1416`（容差 `1e-6`） · `Shape()` 引发 `TypeError`。

## 🧠 Concept checks (comment at bottom of `animals.py`) / 🧠 概念检查（写在 `animals.py` 底部的注释）
1. You used `super(Bird, self)` before and it "worked." Explain precisely *what it did to the MRO* and why it was wrong anyway.
> 🇨🇳 你之前用过 `super(Bird, self)` 并且它“能用”。请精确解释它*对 MRO 做了什么*以及为什么它终究是错误的。
2. Why does `Bird` come before `Animal` in `Parrot.__mro__`?
> 🇨🇳 为什么在 `Parrot.__mro__` 中 `Bird` 排在 `Animal` 前面？
3. Why is `total_area` better than an `isinstance` ladder?
> 🇨🇳 为什么 `total_area` 比 `isinstance` 阶梯式判断更好？

## ✅ Definition of done / ✅ 完成定义
- [ ] Both families built; **predicted MRO matched the printed MRO** · ≥1 labelled EXTEND · `total_area` has zero `isinstance` · 3-4-5 triangle = 6.0 · all tests green · pushed.
> 🇨🇳 两个类族已构建；**预测的 MRO 与打印的 MRO 相符** · 至少一个标注为 EXTEND · `total_area` 中无 `isinstance` · 3-4-5 三角形面积为 6.0 · 所有测试通过 · 已推送。

## 🚀 Submit / 🚀 提交
```bash
git add week01/day02_inheritance && git commit -m "update: Week1 D2 — Heron+MRO fixes, predicted MRO" && git push
```
> 🇨🇳 执行上述 Git 命令以提交代码：将文件夹加入暂存区，填写提交信息，并推送到远程仓库。
➡️ Then [`RECALL.md`](./RECALL.md), and again cold before Day 3.
> 🇨🇳 然后完成 [`RECALL.md`](./RECALL.md)，并在第三天之前再次冷回忆。
