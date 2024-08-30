import random

def insert_quadrado_soma(editor):
    # Gerar coeficientes aleatórios para a expressão
    coef_a = random.randint(1, 10)
    coef_b = random.randint(1, 10)
    
   # Montando a expressão para a frente da carta
    front_text = (f"<b>Produtos Notaveis - Quadrado da Soma</b><br><font color='blue'>Desenvolva a seguinte expressão: ({coef_a}a + {coef_b}b)^2</font>")
    
    # Calculando o desenvolvimento passo a passo
    term1 = f"({coef_a}a)^2"
    term2 = f"2 . {coef_a}a . {coef_b}b"
    term3 = f"({coef_b}b)^2"
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"quadrado do primeiro termo, mais duas vezes o primeiro termo vezes o segundo mais, o quadrado do segundo termo.<br><br>"
                 f"{term1} + {term2} + {term3}<br>"
                 f"{coef_a**2}a^2 + {2 * coef_a * coef_b}ab + {coef_b**2}b^2")
    
    # Atualizando os campos na nota do editor
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