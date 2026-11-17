import streamlit as st
from regras import analisar_portabilidade

st.title("🧙 Assistente Inteligente de Suporte")
st.write("Protótipo de apoio ao atendimento")
st.subheader("📱 Caso fictício: Portabilidade")

chip_entregue = st.checkbox("Chip entregue ao cliente")
linha_ativa = st.checkbox("Linha já está ativa")
cobranca_gerada = st.checkbox("Cobrança já foi gerada")

status_portabilidade = st.selectbox(
    "Status da portabilidade",
    ["Pendente", "Concluída", "Falha"]
)

alertas, sugestoes, diagnostico = analisar_portabilidade(
    chip_entregue,
    linha_ativa,
    cobranca_gerada,
    status_portabilidade
)

for alerta in alertas:
    if alerta["tipo"] == "critico":
        st.error(alerta["mensagem"])

    elif alerta["tipo"] == "atencao":
        st.warning(alerta["mensagem"])

    elif alerta["tipo"] == "ok":
        st.success(alerta["mensagem"])

if sugestoes:
    st.write("🧙 Sugestões do assistente:")

    for sugestao in sugestoes:
        st.write(f"- {sugestao}")
        

st.subheader("🧙 Diagnóstico do caso")

if diagnostico["nivel"] == "critico":
    st.error("Nível: CRÍTICO")
elif diagnostico["nivel"] == "atencao":
    st.warning("Nível: ATENÇÃO")
else:
    st.success("Nível: OK")

st.write(
    f"Problemas detectados: {diagnostico['problemas_detectados']}"
)        
    
    
    
