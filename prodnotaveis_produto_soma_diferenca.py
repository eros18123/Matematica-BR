import random

def insert_produto_soma_diferenca(editor):
    # Gerar coeficientes aleatórios para a expressão
    coef_a = random.randint(1, 10)
    coef_b = random.randint(1, 10)
    
    # Montando a expressão para a frente da carta
    front_text = (f"<b>Produtos Notaveis - Produto da Soma pela Diferença</b><br><font color='blue'>Desenvolva a seguinte expressão: ({coef_a}x + {coef_b}) . ({coef_a}x - {coef_b})</font>")
    
    # Calculando o desenvolvimento
    term1 = f"({coef_a}x)^2"
    term2 = f"({coef_b})^2"
    
    # Montando o texto para o verso da carta
    back_text = (f"<b>Desenvolvimento:</b><br>"
                 f"o primeiro termo elevado ao quadrado menos o segundo termo elevado ao quadrado.<br><br>"
                 f"{term1} - {term2}<br>"
                 f"{coef_a**2}x^2 - {coef_b**2}")
    
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