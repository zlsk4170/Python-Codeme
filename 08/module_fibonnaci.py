# Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.

def generate_fibbonaci_seq(n):
    results = [0, 1, 1]

    for i in range(2, n):
        current_result = results[-1] + results[-2]
        results.append(current_result)

    for nr in range(len(results)):
        print(f'Fib od {nr} -> {results[nr]}')
