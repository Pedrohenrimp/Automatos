_EPSILON = 'e'

def verificaCadeiaAPND(cadeia, estadoAtual, simboloPilha, pilha, transicoes, simboloTerminal, estadosFinais):
    global _EPSILON
    if cadeia == "" and estadoAtual in estadosFinais:
        return pilha.upper() == simboloTerminal
    else:
        if len(cadeia) > 0:
            caractere = cadeia[0]
        else:
            caractere =  ""
        for transicao in transicoes:
            if transicao[0] == (estadoAtual, caractere, simboloPilha):
                pilhaAux = desempilha(pilha)
                pilhaAux = empilha(pilhaAux, transicao[1][1])
                if verificaCadeiaAPND(cadeia[1 :], transicao[1][0], pilhaAux[-1], pilhaAux, transicoes, simboloTerminal, estadosFinais):
                    return True
            if transicao[0] == (estadoAtual, _EPSILON, simboloPilha):
                    pilhaAux = desempilha(pilha)
                    pilhaAux = empilha(pilhaAux, transicao[1][1])
                    if verificaCadeiaAPND(cadeia, transicao[1][0], pilhaAux[-1], pilhaAux, transicoes, simboloTerminal, estadosFinais):
                        return True
        return False


def empilha(pilha, string):
    if(string == _EPSILON):
        return pilha

    for i in range (1, len(string) + 1):
        pilha += string[-i];
    return pilha


def desempilha(pilha):
    return pilha[: -1]



# L = { a(n)b(n) | n > 0 }
transicoes = [ [(1, 'a', 'I'), [1, "AI"]], [(1, 'a', 'A'), [1, "AA"]], [(1, 'b', 'A'), [2, "e"]], [(2, 'b', 'A'), [2, 'e']], [(2, 'e', 'I'), [3, 'I']] ]
estadosFinais = [3]
cadeia1 = "aaabbb"
cadeia2 = ""

print(verificaCadeiaAPND(cadeia1, 1, 'I', 'I', transicoes, 'I', estadosFinais))
print(verificaCadeiaAPND(cadeia2, 1, 'I', 'I', transicoes, 'I', estadosFinais))

# L = { a(2n)b(n) | n > 0 }
transicoes = [ [(1, 'a', 'I'), [2, "AI"]], [(2, 'a', 'A'), [1, "A"]], [(1, 'a', 'A'), [2, "AA"]], [(1, 'b', 'A'), [3, 'e']], [(3, 'b', 'A'), [3, 'e']], [(3, 'e', 'I'), [4, 'I']] ]
estadosFinais = [4]
cadeia1 = "aaaabb"
cadeia2 = "aaaaaabbbbbbbb"

print(verificaCadeiaAPND(cadeia1, 1, 'I', 'I', transicoes, 'I', estadosFinais))
print(verificaCadeiaAPND(cadeia2, 1, 'I', 'I', transicoes, 'I', estadosFinais))
