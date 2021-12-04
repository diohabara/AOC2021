# Day03

## deps

- python3.9.7

## How to run

### part1

```bash
./main.py
```

### part2

```bash
./main.py
```

## 解説

### part1

各列ごとの値の総和を取り、それが行数の半分より大きい場合は`gamma_rate`の末尾に`1`を追加し、`epsilon_rate`の末尾に`0`を追加する。小さい場合は逆をする。

### part2

各列の先頭から数字を数えていき、`"1"`と`"0"`のビット数を数えて値を計算して行く。
