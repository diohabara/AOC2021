# Day01

## deps

- gcc

## How to run

### part1

```bash
g++ part1.cc
./a.out  < input.txt
```

### part2

```bash
g++ part1.cc
./a.out  < input.txt
```

## 解説

### part1

各命令(`forward`, `up`, `down`)に合わせて、`depth`と`horizontal_position`を変更し、最後にそれらを掛ける。

### part2

新しく定義されたように命令によって(`depth`, `horizontal_position`, `aim`)を変更する。最後にそれらを掛ける。
