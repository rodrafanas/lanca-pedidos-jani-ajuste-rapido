import streamlit as st
from fpdf import FPDF
import io

# Função para criar o PDF
def criar_pdf(dados):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    
    # Desenha a tabela para o pedido
    def desenha_tabela(y_inicio):
        pass
    
    # Preenche os dados do pedido na tabela
    def preenche_dados(y_inicio, dados):
        pdf.set_xy(10, y_inicio + 5)
        for chave, valor in dados.items():
            pdf.cell(40, 10, f"{chave}: {valor}", 0, ln=True)
    ## primeira imagem
    ajuste = 25
    pdf.image('logo_jani_ajuste_rapido.jpg',10,ajuste,30)
    
    # Primeiro pedido
    y_inicio = 20 + ajuste
    desenha_tabela(y_inicio)
    preenche_dados(y_inicio, dados)
    
    # Linha pontilhada
    pdf.set_xy(10, y_inicio + 70)
    pdf.cell(190, 10, "", 0, 1, 'C')
    pdf.dashed_line(10, y_inicio + 75, 200, y_inicio + 75, dash_length=1, space_length=1)
    
    ## primeira imagem
    pdf.image('logo_jani_ajuste_rapido.jpg', 10, y_inicio + 80, 30)
    
    # Segundo pedido
    y_inicio += 105
    desenha_tabela(y_inicio)
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
