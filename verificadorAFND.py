

def verificaCadeiaAFND(cadeia, estadoAtual, transicoes, estadosFinais):
    if cadeia == "":
        return estadoAtual in estadosFinais
    else:
        caractere = cadeia[0]
        if (estadoAtual, caractere) in transicoes:
            for estado in transicoes[(estadoAtual, caractere)]:
                if verificaCadeiaAFND(cadeia[1 :], estado, transicoes, estadosFinais):
                    return True
        if(estadoAtual, 'e') in transicoes:
            for estado in transicoes[(estadoAtual, 'e')]:
                if verificaCadeiaAFND(cadeia, estado, transicoes, estadosFinais):
                    return True
        return False



transicoes = {}
estadosFinais = []



transicoes = { (1, 'a') : [1], (1, 'b') : [1, 2], (2, 'a') : [3], (2, 'b') : [3]}
estadosFinais = [3]
cadeia1 = "baba"
cadeia2 = "abab"

print("\nAutomato 1:\n cadeia:", cadeia1, "=", verificaCadeiaAFND(cadeia1, 1, transicoes, estadosFinais))
print("\nAutomato 1:\n cadeia:", cadeia2, "=",verificaCadeiaAFND(cadeia2, 1, transicoes, estadosFinais))



transicoes = {(1, 'a') : [1, 2], (2, 'a') : [2], (2, 'b') : [2]}
estadosFinais = [2]
cadeia1 = 'abbbbaba'
cadeia2 = 'baaaaba'

print("\nAutomato 2:\n cadeia:", cadeia1, "=",verificaCadeiaAFND(cadeia1, 1, transicoes, estadosFinais))
print("\nAutomato 2:\n cadeia:", cadeia2, "=",verificaCadeiaAFND(cadeia2, 1, transicoes, estadosFinais))


transicoes = { (1, 'a') : [1], (1, 'b') : [1], (1, 'e') : [2], (2, 'b') : [3]}
estadosFinais = [3]
cadeia1 = "babab"
cadeia2 = "abab"

print("\nAutomato 3:\n cadeia:", cadeia1, "=", verificaCadeiaAFND(cadeia1, 1, transicoes, estadosFinais))
print("\nAutomato 3:\n cadeia:", cadeia2, "=",verificaCadeiaAFND(cadeia2, 1, transicoes, estadosFinais))