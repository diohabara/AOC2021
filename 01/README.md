# Day01

## deps

- opam
- Core library
- dune

## How to run

### part1

```bash
dune exec -- ./part1.exe
```

### part2

```bash
dune exec -- ./part1.exe
```

## 解説

### part1

各行の数字を前の行の数字を比べれば良い。
その際に`prev`と`cur`という変数を使い、それぞれ整数の最大値に初期化しておく。

### part2

3 行ごとの和の数列を作る。それを part1 と同じように比べる。
