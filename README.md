# mgrep

```
usage: mgrep.py [-h] --pattern PATTERN --sentence SENTENCE

Сравнение набора слов и шаблона, описывающего эти слова с помощью граммем

optional arguments:
  -h, --help           show this help message and exit
  --pattern PATTERN    Шаблон
  --sentence SENTENCE  Фраза
```

## Примеры использования:

Простейший пример - убедиться что переданное слово описывает животное.

``` shell
mgrep --sentence 'Ящерица' --pattern 'anim'
```

Пример с несколькими словами - убедиться что первое слово - женское животное, второе - мужское животное.

``` shell
mgrep --sentence 'Ящерица Ящер' --pattern='NOUN,anim,femn NOUN,anim,masc'
```

Пример, в котором второе слово нам не важно:

```
mgrep --sentence 'Ящерица хотькакоеслово' --pattern='NOUN *'
```
