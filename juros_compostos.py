import random
import math

def calculate_compound_interest(capital, taxa_percentual, tempo_meses):
    # Converte tempo de meses para anos e arredonda para o número inteiro mais próximo
    tempo_anos = round(tempo_meses / 12)
    # Calcula o montante acumulado arredondando o resultado da potência para um número inteiro
    montante = capital * round((1 + taxa_percentual / 100)**tempo_anos)
    # Calcula o juro composto
    juro = montante - capital
    return montante, juro

def insert_compound_interest(editor):
    # Gerando números aleatórios para o exemplo de juros compostos
    capital = random.randint(100, 10000)
    taxa_percentual = random.randint(1, 99)
    tempo_meses = random.randint(12, 100)  # Entre 12 e 100 meses (1 a 8 anos e 4 meses)
    
    montante, juro = calculate_compound_interest(capital, taxa_percentual, tempo_meses)
    
    # Arredonda o tempo para o número inteiro mais próximo
    tempo_arredondado = round(tempo_meses / 12)
    
    # Arredonda o resultado da potência para um número inteiro
    taxa_tempo = round((1 + taxa_percentual / 100)**tempo_arredondado)
    
    front_text = (
        f"<b>Juros Compostos</b><br>"
        f"<font color='blue'>Exemplo: Um capital de R$ {capital},00 foi aplicado a juros compostos a uma taxa de {taxa_percentual}% a.a. "
        f"Qual será o montante acumulado após {tempo_meses} meses?</font>"
    )

    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"C = R$ {capital},00; i = {taxa_percentual}% a.a.; t = {tempo_meses} meses.<br><br>"
                 f"Note que o tempo e a taxa estão em unidades diferentes, mas sabemos que {tempo_meses} meses é igual a "
                 f"{tempo_meses / 12:.2f} anos, então arredondamos t = {tempo_arredondado} anos, e que a taxa precisa ser escrita na forma decimal, "
                 f"i = {taxa_percentual / 100:.2f}.<br><br>"
                 f"M = C ((1+i)^t)<br>"
                 f"M = {capital} ((1+{taxa_percentual / 100:.2f})^{tempo_arredondado})<br>"
                 f"M = {capital} . ({taxa_tempo})<br>"
                 f"M = R$ {montante:.0f}<br><br>"
                 f"Para encontrar o juro temos que:<br>"
                 f"J = M – C<br>"
                 f"J = {montante:.0f} – {capital}<br>"
                 f"J = R$ {juro:.0f}")
    
    #note = editor.note
    #note["Frente"] = front_text
    #note["Verso"] = back_text
    #editor.loadNote()




    # Atualizar os campos na nota do editor
    note = editor.note
    
    # Obter os nomes dos campos
    field_names = list(note.keys())
    
    # Atualizar o primeiro campo com front_text
    if field_names:
        note[field_names[0]] = front_text
    
    # Atualizar o segundo campo com back_text
    if len(field_names) > 1:
        note[field_names[1]] = back_text
    
    # Iterar sobre os campos e atualizar cada um deles com valores genéricos
    for i, field_name in enumerate(field_names):
        if i not in [0, 1]:
            note[field_name] = f"Valor do campo {field_name}"
    
    editor.loadNote()