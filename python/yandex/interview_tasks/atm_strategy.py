from abc import ABC, abstractmethod


# SDK (без изменений)
class SDK(ABC):
    @abstractmethod
    def count_banknotes(self, banknote: int) -> int:
        pass

    @abstractmethod
    def move_banknote_to_dispenser(self, banknote: int, count: int) -> None:
        pass

    @abstractmethod
    def open_dispenser(self) -> None:
        pass


class SDK_ATM(SDK):

    def __init__(self, banknotes_cassettes: dict[int, int]):
        self._banknotes_cassettes = banknotes_cassettes

    def count_banknotes(self, banknote: int) -> int:
        return self._banknotes_cassettes.get(banknote, 0)

    def move_banknote_to_dispenser(self, banknote: int, count: int) -> None:
        self._banknotes_cassettes[banknote] = self._banknotes_cassettes.get(banknote, 0) - count

    def open_dispenser(self) -> None:
        pass


# === Strategy Pattern ===

class CashoutStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: int, available: dict[int, int]) -> dict[int, int]:
        """Рассчитать набор купюр для выдачи. Raises ArithmeticError если невозможно."""
        pass


class GreedyStrategy(CashoutStrategy):
    """Жадный алгоритм: берём максимальный номинал, потом следующий."""

    def calculate(self, amount: int, available: dict[int, int]) -> dict[int, int]:
        result = {}
        remaining = amount

        for banknote in sorted(available.keys(), reverse=True):
            if banknote > remaining:
                continue
            count_need = remaining // banknote
            count_have = available.get(banknote, 0)
            count_take = min(count_need, count_have)
            if not count_take:
                continue
            result[banknote] = count_take
            remaining -= count_take * banknote
            if remaining == 0:
                break

        if remaining != 0:
            raise ArithmeticError(f"Not enough banknotes: failed to fill {remaining}")

        return result


class MinBanknotesStrategy(CashoutStrategy):
    """Динамическое программирование: минимальное количество купюр."""

    def calculate(self, amount: int, available: dict[int, int]) -> dict[int, int]:
        denominations = sorted(available.keys())

        # dp[i] = (min_count, banknotes_used) для суммы i
        dp = {0: (0, {})}

        for i in range(1, amount + 1):
            best = None
            for d in denominations:
                if d > i:
                    break
                prev = i - d
                if prev not in dp:
                    continue
                prev_count, prev_used = dp[prev]
                used_of_d = prev_used.get(d, 0)
                if used_of_d >= available.get(d, 0):
                    continue
                candidate_count = prev_count + 1
                if best is None or candidate_count < best[0]:
                    new_used = dict(prev_used)
                    new_used[d] = used_of_d + 1
                    best = (candidate_count, new_used)
            if best is not None:
                dp[i] = best

        if amount not in dp:
            raise ArithmeticError(f"Not enough banknotes: cannot make {amount}")

        return dp[amount][1]


class ATM:

    def __init__(self, banknotes_cassettes: dict[int, int], strategy: CashoutStrategy | None = None):
        self._banknotes = [50, 100, 500, 1000, 5000]
        self._sdk = SDK_ATM(banknotes_cassettes)
        self._strategy = strategy or GreedyStrategy()

    def cashout(self, amount_requested: int) -> dict[int, int]:
        current_banknotes = {b: self._sdk.count_banknotes(b) for b in self._banknotes}
        current_amount = sum(b * c for b, c in current_banknotes.items())

        if amount_requested > current_amount:
            raise Exception(f"Not enough money: {amount_requested} > {current_amount}")

        banknotes_to_give = self._strategy.calculate(amount_requested, current_banknotes)

        for b, c in banknotes_to_give.items():
            if c:
                self._sdk.move_banknote_to_dispenser(b, c)
        self._sdk.open_dispenser()

        return banknotes_to_give



atm = ATM({50: 100, 5000: 1})
assert str(atm.cashout(5000)) == str({5000: 1})

atm = ATM({50: 100, 5000: 1})
assert str(atm.cashout(4500)) == str({50: 90})

atm = ATM({50: 100, 5000: 1})
try:
    atm.cashout(56)
except Exception as ex:
    print(ex)
    assert isinstance(ex, ArithmeticError)

print("All tests passed!")
