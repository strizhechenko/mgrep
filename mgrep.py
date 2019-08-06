# coding: utf-8
from argparse import ArgumentParser
from pymorphy2 import MorphAnalyzer

analyzer = MorphAnalyzer()


def parse_args():
    parser = ArgumentParser()
    parser.description = "Сравнение набора слов и шаблона, описывающего эти слова с помощью граммем"
    parser.epilog = """Примеры использования:
    -------------------------------------------------------------------------
    mgrep --sentence 'Ящерица' --pattern 'anim'
    -------------------------------------------------------------------------
    mgrep --sentence 'Ящерица Ящер' --pattern='NOUN,anim,femn NOUN,anim,masc'
    -------------------------------------------------------------------------
    mgrep --sentence 'Ящерица хотькакоеслово' --pattern='NOUN *'
    """
    parser.add_argument("--pattern", type=str, required=True, help="Шаблон")
    parser.add_argument("--sentence", type=str, required=True, help="Фраза")
    return parser.parse_args()


def match_word(pattern, word):
    for result in analyzer.parse(word):
        if all(tag in result.tag for tag in pattern):
            return True


def match(pattern, sentence):
    assert len(pattern) == len(sentence), "Разная длина предложения и шаблона"
    while sentence:
        word = sentence.pop()
        word_pattern = pattern.pop()
        if pattern == '*':
            continue
        if not match_word(word_pattern, word):
            raise ValueError("Слово {0} не совпало с шаблоном {1}, его граммемы {2}".format(
                word, word_pattern, [", ".join(tag.tag.grammemes) for tag in analyzer.parse(word)]))


def main():
    args = parse_args()
    pattern = [word_tags.split(',') for word_tags in args.pattern.split()]
    sentence = args.sentence.split()
    match(pattern, sentence)


if __name__ == '__main__':
    main()
