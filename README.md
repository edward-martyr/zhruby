# Zaonhe Ruby (zhruby) <ruby>上海話吳語協會式注音<rt>Zaonhegho Wunyu–Yahwe-Seh Tsyin</ruby>

Converts Traditional Chinese passage to TeX-flavoured ruby and outputs PDF. Requires `xelatex` and [`ctex`](https://github.com/CTeX-org/ctex-kit).

輸入中文文本文檔，輸出上海話注音的 LaTeX 文檔及 PDF。需要 `xelatex` 和 [`ctex`](https://github.com/CTeX-org/ctex-kit)。

## Installation

```bash
python3 -m pip install zhruby==2.0.3
```

## Usage

```bash
python3 -m zhruby [list of text files]
```

Append `-s` to output simplified documents.
