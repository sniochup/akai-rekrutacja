sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]


def word_loading(tab):
    dic = {}
    for sentence in tab:
        for word in sentence.split():
            try:
                dic[word.lower()] += 1
            except:
                dic[word.lower()] = 1
    return dic


def word_chooser(dic):
    try:
        for i in range(3):
            max_value = max(dic, key=dic.get)
            print(f'{i}. "{max_value}"\t - {dic[max_value]}')
            del dic[max_value]
    except ValueError:
        print("Insufficient number of words")


def main():
    stab = sentences
    dic = word_loading(stab)
    word_chooser(dic)


if __name__ == '__main__':
    main()