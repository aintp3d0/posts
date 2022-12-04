import datetime as dt


def jp_date(date: dt.date) -> str:
    # SEE
    # https://www.japanesewithanime.com/2017/03/weekdays-in-japanese.html
    # http://www.rikai.com/library/kanjitables/kanji_codes.unicode.shtml
    """ Returns `2014, month 11, day 28, (WED).` -> `１４年１１月２８日（水）`
    """
    result = []
    jp_digits = ('０', '１', '２', '３', '４', '５', '６', '７', '８', '９')
    jp_weekdays = ('日', '月', '火', '水', '木', '金', '土')

    def get_digits(digit: int) -> str:
        return ''.join(jp_digits[int(d)] for d in str(digit)[-2:])

    # NOTE: 04 -> 4
    result.extend(
        (
            get_digits(date.year), '年',
            get_digits(date.month), '月',
            get_digits(date.day), '日',
            f"（{jp_weekdays[date.weekday()-1]}）"
        )
    )
    return ''.join(result)
