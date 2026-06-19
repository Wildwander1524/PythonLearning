"""类 对象 属性 方法"""

from decimal import Decimal


# 可变性（Mutability）
# 可变（Mutable） —— 原地突变（mutate）
# 不可变（Immutable） —— 重新绑定（Rebinding）
class BankAccount:

    bank_name = "PythonLearning Bank"
    account_count = 0

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        # TODO: ROUND_HALF_EVEN
        self._balance = balance
        self._history = []
        BankAccount.account_count += 1
        # self.account_count += 1
        # 不会报错，实例化时类已经定义完了，此时实例对象可以通过self.attr访问类属性，然后作为实例对象自己的属性进行修改

    def __str__(self):
        return f"{self.owner}'s account — balance: {self._balance:.2f}"

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def history(self):
        return list(self._history)

    def statement(self):
        # 生成一个元素为 str({i}: {item}) 的生成器，然后作为可迭代对象逐个取元素用 '\n' 拼接
        return "\n".join(f"{i}: {item}" for i, item in enumerate(self._history))

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Invalid Amount")
        self._balance += amount
        self._history.append(
            f"type: deposit\tamount:  {amount:.2f}\tbalance: {self._balance:.2f}"
        )

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Invalid Amount")
        elif self._balance < amount:
            raise ValueError("Overdraft")
        self._balance -= amount
        self._history.append(
            f"type: withdraw\tamount: -{amount:.2f}\tbalance: {self._balance:.2f}"
        )

    def transfer(self, target: object, amount: float) -> None:
        # TODO: Inherit the validation by reusing
        self.withdraw(amount)
        target.deposit(amount)


if __name__ == "__main__":

    acct = BankAccount("Aen", 50)
    target = BankAccount("Ben", 150)
    print("expected: 50, 150")
    print(acct, target, sep="\n")

    acct.deposit(50)
    target.withdraw(50)
    print("expected: 100, 100")
    print(acct, target, sep="\n")

    acct.transfer(target, 50)
    print("expected: 50, 150")
    print(acct.balance, target.balance)

    print(acct.history)
    print(acct.statement())

    print(acct.balance)  # 100.0  (read-only property — no setter)
    acct.deposit(50)  # balance → 150.0
    acct.withdraw(30)  # balance → 120.0
    acct.balance = 999  # ❌ AttributeError (invariant protected)
    acct.deposit(-5)  # ❌ ValueError
    acct.withdraw(10000)  # ❌ ValueError (overdraft)
    print(acct.history)  # list of dict records; a COPY (caller can't mutate internals)
    print(str(acct))  # "Ben's account — balance: 120.00"   (2 decimals!)
    print(BankAccount.account_count)  # increments once per account created

"""
Concept checks
1.Why does transfer not re-check amount > 0? What principle is that? (One word.)
Answer: DRY.Dont Repeat Yourself.
2.What exactly makes balance read-only — what did you not write?
Answer: @balance.setter
3.If __init__ used self.account_count += 1, what would BankAccount.account_count be after 3 accounts, and why?
Answer: 0,because the instance attribute shadowed the class attribute

"""
