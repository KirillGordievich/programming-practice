from abc import ABC, abstractmethod



# API для взаимодействия с аппаратурой банкомата.
# Краткий ликбез по устройству банкомата:
# - деньги расположены в кассетах, кассеты устанавливаются инкассацией;
# - в каждой кассете лежат свои купюры, количество известно инкассатору при установке
# - банкомат может подсчитать оставшиеся в кассетах банкноты, но эта операция занимает около 10 секунд, и шумная, её стоит вызывать как можно реже.
# - интерфейс SDK может быть изменён/расширен по договорённости сторон, если это необходимо

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


# Банкомат.
# Инициализируется набором купюр и умеет выдавать купюры для заданной суммы, либо отвечать отказом.
# При выдаче купюры списываются с баланса банкомата.
# Допустимые номиналы: 50₽, 100₽, 500₽, 1000₽, 5000₽.
class ATM:

    def __init__(self, banknotes_cassettes: dict[int, int]):
        self._banknotes = [50, 100, 500, 1000, 5000]
        self._sdk = SDK_ATM(banknotes_cassettes)

    def cashout(self, amount_requested: int) -> dict[int, int]:
        current_banknotes = { b: self._sdk.count_banknotes(b) for b in self._banknotes }
        print(f"current_banknotes: {current_banknotes}")
        current_amount = sum([b * c for b, c in current_banknotes.items()])
        if amount_requested > current_amount:
            raise Exception(f"Not enough money: {amount_requested} > {current_amount}")

        # 1. Выбираем наибольшую по номиналу купюру для выдачи
        # 2. Вычитаем её пока не получим 0 или отрицательное значение
        # 3. Если ноль, то возращаем амаунт
        # 4. Если отрицательное, то выбираем банкноту на один номинал меньше

        amount_to_fill = amount_requested
        banknotes_to_give = {}
        for banknote in self._banknotes[::-1]:
            if banknote > amount_to_fill:
                continue
            banknote_count_need = amount_requested // banknote
            print(f"{banknote} banknote_count_need: {banknote_count_need}")
            if not banknote_count_need:
                continue
            banknote_count_have = current_banknotes.get(banknote, 0)
            print(f"{banknote} banknote_count_have: {banknote_count_have}")

            banknote_count_take = banknote_count_need if banknote_count_need < banknote_count_have else banknote_count_have
            if not banknote_count_take:
                continue
            banknotes_to_give[banknote] = banknote_count_take
            amount_to_fill -= banknote_count_take * banknote

            if amount_to_fill == 0:
                break

        if amount_to_fill != 0:
            raise ArithmeticError(f"Not enough banknotes: failed to fill {amount_to_fill}")

        for b, c in banknotes_to_give.items():
            if not c:
                continue
            self._sdk.move_banknote_to_dispenser(b, c)

        self._sdk.open_dispenser()

        return banknotes_to_give

dataset_banknotes = {
    50: 100,
    5000: 1,
}
atm = ATM(dataset_banknotes)
assert str(atm.cashout(5000)) == str({ 5000: 1})

dataset_banknotes = {
    50: 100,
    5000: 1,
}
atm = ATM(dataset_banknotes)
assert str(atm.cashout(4500)) == str({ 50: 90 })


dataset_banknotes = {
    50: 100,
    5000: 1,
}
atm = ATM(dataset_banknotes)
try:
    atm.cashout(56)
except Exception as ex:
    print(ex)
    assert isinstance(ex, ArithmeticError) is True
