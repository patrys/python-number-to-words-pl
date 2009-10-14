# - coding: utf-8 -

SUFFIXES = [
    None,
    u'jeden', u'dwa', u'trzy', u'cztery', u'pięć', u'sześć', u'siedem',
    u'osiem', u'dziewięć', u'dziesięć', u'jedenaście', u'dwanaście',
    u'trzynaście', u'czternaście', u'piętnaście', u'szesnaście',
    u'siedemnaście', u'osiemnaście', u'dziewiętnaście',
]

TENS = [
    None,
    u'dziesięć', u'dwadzieścia', u'trzydzieści', u'czterdzieści',
    u'pięćdziesiąt', u'sześćdziesiąt', u'siedemdziesiąt', u'osiemdziesiąt',
    u'dziewięćdziesiąt',
]

HUNDREDS = [
    None,
    u'sto', u'dwieście', u'trzysta', u'czterysta', u'pięćset', u'sześćset',
    u'siedemset', u'osiemset', u'dziewięćset',
]

THOUSAND_SUFFIXES = [
    None,
    (u'tysiąc', u'tysiące', u'tysięcy'),
    (u'milion', u'miliony', u'milionów'),
    (u'miliard', u'miliardy', u'miliardów'),
    (u'bilion', u'biliony', u'bilionów'),
    (u'biliard', u'biliardy', u'biliardów'),
]

def to_words(value, unit=None):
    result = []
    if not value:
        return u'zero 0/100'
    remainder = value % 1
    number = int(value)
    iteration = 0
    while number:
        sub_thousand = number % 1000
        thousands = number // 1000
        if sub_thousand:
            ret_parts = []
            suffix = THOUSAND_SUFFIXES[iteration]
            sub_hundred = sub_thousand % 100
            hundreds = sub_thousand // 100
            sub_ten = sub_hundred % 10
            tens = sub_hundred // 10
            if HUNDREDS[hundreds]:
                ret_parts.append(HUNDREDS[hundreds])
            if sub_thousand == 1:
                if iteration == 0:
                    if SUFFIXES[sub_thousand]:
                        ret_parts.append(SUFFIXES[sub_thousand])
                if suffix:
                    ret_parts.append(suffix[0])
            elif sub_hundred < 20:
                if SUFFIXES[sub_hundred]:
                    ret_parts.append(SUFFIXES[sub_hundred])
                if suffix:
                    if sub_hundred > 1 and sub_hundred < 5:
                        ret_parts.append(suffix[1])
                    else:
                        ret_parts.append(suffix[2])
            else:
                if TENS[tens]:
                    ret_parts.append(TENS[tens])
                if SUFFIXES[sub_ten]:
                    ret_parts.append(SUFFIXES[sub_ten])
                if suffix:
                    if sub_ten > 0 and sub_ten < 5:
                        if tens and sub_ten == 1:
                            ret_parts.append(suffix[2])
                        else:
                            ret_parts.append(suffix[1])
                    else:
                        ret_parts.append(suffix[2])
            result = ret_parts + result
            del ret_parts
        number = thousands
        iteration += 1
    if unit:
        result.append(unit)
    result.append(u'%d/100' % int(remainder * 100))
    result = ' '.join(result)
    return result

