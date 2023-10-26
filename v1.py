import pywhatkit as kit

mensagem = """
Prezado(a) usuário,

Espero que esteja bem. Somos da equipe de T.I do grupo Multi e estamos realizando uma verificação de rotina das linhas de telefone para garantir que nossos registros estejam atualizados.

Para confirmar se ainda está utilizando este número, por favor, responda a esta mensagem com seu nome completo, setor e gestor direto.

Sua colaboração é fundamental para mantermos nossos registros precisos e garantir que possamos atendê-lo da melhor maneira possível.

Agradecemos pela sua atenção e cooperação. Se tiver alguma dúvida ou precisar de assistência, não hesite em nos contatar.

Atenciosamente,
Frederico Almeida
Equipe de Tecnologia da Informação
Grupo Multi
"""

# Substitua "+seu_numero" pelo número de telefone do destinatário
# Defina o horário e minuto em que você deseja enviar a mensagem
hora = 15  # Substitua pelo horário desejado (horas)
minuto = 57  # Substitua pelos minutos desejados

kit.sendwhatmsg("+5535998888831", mensagem, hora, minuto)
