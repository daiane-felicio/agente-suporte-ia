def analisar_portabilidade(
    chip_entregue,
    linha_ativa,
    cobranca_gerada,
    status_portabilidade
):
    alertas = []
    sugestoes = []

    if not chip_entregue and linha_ativa:
        alertas.append({
            "tipo": "atencao",
            "mensagem": "A linha está ativa, mas o chip ainda não foi entregue ao cliente."
        })

        sugestoes.append(
            "Validar a situação da entrega do chip."
        )

        sugestoes.append(
            "Evitar orientar uso antes da confirmação da entrega."
        )

        if cobranca_gerada:
            alertas.append({
                "tipo": "critico",
                "mensagem": "Existe cobrança gerada antes da entrega do chip."
            })

    if status_portabilidade == "Falha":
        alertas.append({
            "tipo": "critico",
            "mensagem": "A portabilidade apresenta falha."
        })

        sugestoes.append(
            "Verificar os dados cadastrados e identificar o motivo da falha."
        )

    if (
        chip_entregue
        and linha_ativa
        and not cobranca_gerada
        and status_portabilidade == "Concluída"
    ):
        alertas.append({
            "tipo": "ok",
            "mensagem": "O cenário não apresenta inconsistências visíveis."
        })
        
        
    nivel = "ok"

    if any(alerta["tipo"] == "critico" for alerta in alertas):
        nivel = "critico"
    elif any(alerta["tipo"] == "atencao" for alerta in alertas):
        nivel = "atencao"

    problemas_detectados = sum(
        1 for alerta in alertas
        if alerta["tipo"] in ["critico", "atencao"] 
    )

    diagnostico = {
        "nivel": nivel,
        "problemas_detectados": problemas_detectados
    }

    return alertas, sugestoes, diagnostico
    