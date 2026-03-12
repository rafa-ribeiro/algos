NUM_MAPS = {
    "0": "zero",
    "1": "um",
    "2": "dois",
    "3": "três",
    "4": "quatro",
    "5": "cinco",
    "6": "seis",
    "7": "sete",
    "8": "oito",
    "9": "nove",
    "10": "dez",
    "11": "onze",
    "12": "doze",
    "13": "treze",
    "14": "quatorze",
    "15": "quinze",
    "16": "dezesseis",
    "17": "dezessete",
    "18": "dezoito",
    "19": "dezenove",
    "20": "vinte",
    "30": "trinta",
    "40": "quarenta",
    "50": "cinquenta",
    "60": "sessenta",
    "70": "setenta",
    "80": "oitenta",
    "90": "noventa",
    "100": "cem",
    "200": "duzentos",
    "300": "trezentos",
    "400": "quatrocentos",
    "500": "quinhentos",
    "600": "seiscentos",
    "700": "setecentos",
    "800": "oitocentos",
    "900": "novecentos",
    "1000": "mil"
}


def spell(n: int):
    if str(n) in NUM_MAPS:
        return NUM_MAPS[str(n)]

    NUM_MAPS["100"] = "cento"

    if 10 < n < 100:
        return build_dec_part(n)

    if 100 < n < 1000:
        return build_cent_part(n)

    if 1000 < n < 10000:
        return build_thou_part(n)


def build_dec_part(n: int):
    if str(n) in NUM_MAPS:
        return NUM_MAPS[str(n)]

    unit = n % 10
    dec = n - unit
    result = NUM_MAPS[str(dec)]
    if unit:
        result += " e " + NUM_MAPS[str(unit)]

    return result.strip()


def build_cent_part(n: int):
    if n == 100:
        return "e cem"

    rest = n % 100
    cent = n - rest

    result = ""
    if cent:
        result = NUM_MAPS[str(cent)]

    if rest:
        result += " e " + build_dec_part(rest)

    return result.strip()


def build_thou_part(n: int):
    rest = n % 1000
    thou = n - rest

    unit_thou = thou // 1000
    result = NUM_MAPS[str(thou)] if thou == 1000 else NUM_MAPS[str(unit_thou)] + " " + NUM_MAPS["1000"]
    result += " " + build_cent_part(rest) if rest else ""

    return result.strip()
