import streamlit as st
from fpdf import FPDF
import io

# # Função para criar o PDF
def criar_pdf(dados):
    
    pdf = FPDF('P','mm',(58,250))
    pdf.add_page()
    pdf.set_font("Arial", size=6)
    
    # Define a margem direita como 45 mm
    pdf.set_right_margin(45)
    
    # Preenche os dados do pedido na tabela
    def preenche_dados(y_inicio, dados):
        pdf.set_xy(5, y_inicio + 5)
        for chave, valor in dados.items():
            pdf.multi_cell(45, 5, f"{chave}: {valor} \n", align='L')
       
    ## primeira imagem
    ajuste = 10
    pdf.image('logo_jani_ajuste_rapido.jpg',5,ajuste,30)
    
    # Primeiro pedido
    y_inicio = 20 + ajuste
    preenche_dados(y_inicio, dados)
    
    # Linha pontilhada
    pdf.set_xy(5, y_inicio + 70)
    pdf.cell(190, 10, "", 0, 1, 'C')
    pdf.dashed_line(5, y_inicio + 75, 200, y_inicio + 75, dash_length=1, space_length=1)
    
    ## primeira imagem
    pdf.image('logo_jani_ajuste_rapido.jpg', 5, y_inicio + 80, 30)
    
    # Segundo pedido
    y_inicio += 105
    preenche_dados(y_inicio, dados)

    # Salva o PDF em um buffer de memória e retorna como uma string
    return pdf.output(dest='S').encode('latin1')


# Interface do Streamlit
st.image('logo_jani_ajuste_rapido.jpg', width=200)
st.title("Emissão de Pedidos de Reformas de Roupas")

nome_cliente = st.text_input("Nome do Cliente")
telefone = st.text_input("Telefone")
pedido = st.text_input("Pedido")


# options = st.multiselect(
#     "Escolha as opções abaixo?",
#     ["Barra de calça simples", "Barra de calça jeans original", "Barra de vestido de festa", "Troca de zíper simples", "Troca de zíper de jeans", "Barra de calça simples", "Barra de calça jeans original", "Barra de vestido de festa", "Troca de zíper simples", "Troca de zíper de jeans", "Barra de calça simples", "Barra de calça jeans original", "Barra de vestido de festa", "Troca de zíper simples", "Troca de zíper de jeans"],
#     None)

# # Barra de calça 30 simples 
# # Barra de calça jeans original 40
# # Barra de vestido de festa 120

# # Troca de zíper de jeans 40
# # Troca de zíper simples 30


# st.write("Voce selecionou:", options)

# edited_df = st.data_editor(options)

# pedido = 

######################################
import streamlit as st
import pandas as pd

# Dicionário com os preços de cada serviço
precos = {
    "Barra de calça simples": 30,
    "Barra de calça jeans original": 40,
    "Barra de vestido de festa": 120,
    "Troca de zíper simples": 30,
    "Troca de zíper de jeans": 40
}

# # Função para calcular o preço total com base nas seleções e quantidades
# def calcular_preco_total(df):
#     total = 0
#     for index, row in df.iterrows():
#         preco_unitario = precos[row["Serviço"]]
#         quantidade = row["Quantidade"]
#         total += preco_unitario * quantidade
#     return total

# Função para calcular o preço total com base nas seleções e quantidades
def calcular_preco_total(df):
    total = 0
    for i in range(len(df)):
        servico = df.iloc[i]["Serviço"]
        quantidade = df.iloc[i]["Quantidade"]
        preco_unitario = precos[servico]
        total += preco_unitario * quantidade
    return total

# Seleção das opções
options = st.multiselect(
    "Escolha as opções abaixo:",
    list(precos.keys()),
    None
)

# Criando DataFrame com as opções selecionadas, quantidade padrão igual a 1 e o preço de cada serviço
df = pd.DataFrame({
    "Serviço": options,
    "Quantidade": [1] * len(options),
    "Preço": [precos[option] for option in options]
})

# Permitindo ao usuário editar as quantidades
edited_df = st.dataframe(df)

# Calculando o preço total
# preco_total = calcular_preco_total(edited_df.data)
# st.write("Preço Total:", preco_total)




data_pedido = st.date_input("Data do Pedido")
data_entrega = st.date_input("Data de Entrega")
valor_pedido = st.number_input("Valor do Pedido (R$)", format="%.2f")

dados_pedido = {
    "Cliente": nome_cliente,
    "Telefone": telefone,
    "Pedido": pedido,
    "Data do Pedido": data_pedido,
    "Data de Entrega": data_entrega,
    "Valor": f"R$ {valor_pedido}"
}

if st.button("Gerar Pedido em PDF"):
    pdf = criar_pdf(dados_pedido)
    st.download_button(
        label="Baixar Pedido em PDF",
        data=pdf,
        file_name="pedido.pdf",
        mime="application/pdf"
    )
