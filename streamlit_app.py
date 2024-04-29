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
