def longest_palindrome_recursive(s: str, computed_substring=None) -> str:
    computed_substring = computed_substring or dict()

    def _is_palindrome(substring: str) -> bool:
        for i in range(len(substring) // 2):
            end = len(substring) - i - 1
            if substring[i] != substring[end]:
                computed_substring[substring] = False
                return False

        computed_substring[substring] = True
        return True

    if s in computed_substring:
        return s if computed_substring[s] else ''

    if len(s) == 0:
        return ''

    if _is_palindrome(s):
        return s

    c1 = longest_palindrome_recursive(s=s[:-1], computed_substring=computed_substring)
    c2 = longest_palindrome_recursive(s=s[1:], computed_substring=computed_substring)
    if len(c1) >= len(c2):
        return c1
    else:
        return c2


def longest_palindrome_brute_force(s: str) -> str:
    # Nesse for externo vamos iterar por todos os diferentes tamanhos de substring
    # Começando do maior tamanho que é a própria string s
    # - Procuramos por uma palindromo de tamanho 6, no próximo round, procuraremos por
    # uma substring de tamanho 5 e assim por diante
    for length_substring in range(len(s), 0, -1):
        for start in range(0, len(s) - length_substring + 1):
            curr_word = s[start: start + length_substring]
            if is_palindrome(s=curr_word):
                return curr_word

    return ""

def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        end = len(s) - i - 1
        if s[i] != s[end]:
            return False
    return True


def longest_palindrome_dp(s: str) -> str:
    n = len(s)
    # dp é uma matriz que irá conter valores True para grupos palíndromos que encontrarmos
    # ao longo da string S
    # Aqui inicializamos toda a matrix com False
    dp = [[False] * n for _ in range(n)]

    ans = [0, 0]

    # Nesse for adicionamos True na célula [i][i] da matriz porque consideramos que uma string
    # de tamanho 1 é sempre um palindromo
    for i in range(n):
        dp[i][i] = True

    # Aqui iteramos por i e comparamos com o valor em i+1. Se iguais, sabemos que nossa
    # substring palindroma aumentou em 1. Guardamos em ans os índices de início e fim da substring
    # Como partimos do começo e vamos para o final, cada novo palíndromo é o maior, assim só
    # substituímos o valor em ans
    # Aqui sempre comparamos em duplas, caractere i com i + 1, segue para a explicação no for abaixo
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans = [i, i + 1]

    # É por isso que aqui iniciamos em 2, para compararmos em grupos de substrings iniciando com 2 em 2, depois, 3 em 3
    for diff in range(2, n):
        for i in range(0, n - diff):
            j = i + diff
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                ans = [i, j]

    start, end = ans
    return s[start: end + 1]
