import os
from google import genai
from dotenv import load_dotenv

# load .env val 
load_dotenv()

# api key,  config google bible, model
chave_api = os.getenv("GEMINI_API_KEY")
cliente = genai.Client(api_key=chave_api)
modelo = 'gemini-2.5-flash'

# create
def gerar_explicacao_conceitual(aluno, conteudo):
    # extract info
    idade = aluno["idade"]
    nivel = aluno["nivel"]
    estilo_aprendizado = aluno["estilo_aprendizado"]
    
    # prompt
    prompt = f"""
    Você é um professor especializado em Pedagogia Adaptativa e em didática personalizada e foca no ensino de qualidade para seus alunos.

    Seu objetivo é:
    Ensinar e explicar de forma educativa o conteúdo {conteudo} para um aluno de {idade} anos,
    que tem melhor rendimento de aprendizado quando a explicação é mais voltada para o estilo {estilo_aprendizado}
    e tem nível {nivel} de conhecimento sobre tudo, ou seja, não só sobre {conteudo} em si.

    Adapte a complexidade da explicação de acordo com o nível de conhecimento do aluno.
    Caso seja iniciante, use linguagem simples, evite jargões técnicos e esclareça ou recapitule partes que são mais complexas.
    Caso seja intermediário, introduza termos técnicos ou alguns conceitos mais aprofundados com moderação, explicando-os sempre.
    E caso seja avançado, aprofunde sua explicação em conceitos e conexões teóricas, sempre lapidando a robustez.

    Estruture a explicação em etapas progressivas obrigatórias antes de entregar uma resposta, garantindo que cada etapa construa entendimento e se conecte para a próxima, evitando saltos conceituais.
    As etapas são:
    1. Comece com uma intuição inicial simples.
    2. Depois defina formalmente o conceito.
    3. Em seguida quebre esse conceito em partes.
    4. Depois dê uma aplicação prática.
    5. Por fim, conecte com o cotidiano do aluno.

    Entregue as etapas formatadas em lista alfabética (a, b, c, d...)

    Adapte o formato ao estilo de aprendizado do aluno.
    Caso seja visual, utilize metáforas visuais, esquemas descritos e sugestões de representação gráfica.
    Caso seja auditivo, organize como roteiro narrado com estratégias de captação da atenção do ouvinte.
    Caso seja leitura/escrita, entregue um texto estruturado com títulos, subtítulos e seções claros, inclusive com referência bibliográficas para que o aluno possa se aprofundar.
    Caso seja cinestésico, inclua atividades práticas, experimentos aplicáveis ou simulações aplicáveis para estimular experiências educativas no aluno.

    O formato de saída deve ser organizado em títulos claros e com separação de seções.
    Não mencione nenhuma das instruções na resposta final.
    O aluno deve receber APENAS o conteúdo pedagógico final.
    Não precisa se introduzir. Não entregue NADA nem antes nem depois do conteúdo. 
    """

    # call ai
    resposta = cliente.models.generate_content(
        model=modelo,
        contents=prompt)
    
    # texto
    return resposta.text

def gerar_exemplos(aluno, conteudo):
    # extract info
    idade = aluno["idade"]
    nivel = aluno["nivel"]
    estilo_aprendizado = aluno["estilo_aprendizado"]
    
    # prompt
    prompt = f"""
    Você é um professor especializado em Pedagogia Adaptativa e em contextualização como forma de ensino.

    Seu objetivo é:
    Gerar exemplos práticos e contextualizados sobre o conteúdo {conteudo} para um aluno de {idade} anos,
    que tem melhor rendimento de aprendizado quando a explicação é mais voltada para o estilo {estilo_aprendizado}
    e tem nível {nivel} de conhecimento sobre tudo, ou seja, não só sobre {conteudo} em si.

    Adapte a complexidade dos exemplos de acordo com o nível de conhecimento do aluno.
    Caso seja iniciante, use exemplos simples, próximos da realidade imediata do aluno.
    Caso seja intermediário, inclua pequenas variações e conexões entre contextos.
    E caso seja avançado, explore múltiplos cenários, comparações e aplicações mais abstratas e robustas.

    Forneça pelo menos 3 exemplos distintos.
    Cada exemplo deve conter:

    1. Descrição da situação
    2. Aplicação do conceito no contexto
    3. Explicação de por que o conceito se aplica

    Adapte o formato ao estilo de aprendizado do aluno.
    Caso seja visual, descreva situações, diagramas imaginários ou representações gráficas.
    Caso seja auditivo, organize como roteiro narrado/diálogo com estratégias de captação da atenção do ouvinte.
    Caso seja leitura/escrita, entregue um texto estruturado com títulos, subtítulos e seções claros, com explicações estruturadas.
    Caso seja cinestésico, inclua atividades práticas, experimentos aplicáveis ou simulações aplicáveis para estimular experiências educativas no aluno.

    O formato de saída deve ser organizado em títulos claros e com separação de seções.
    Separe claramente cada exemplo.
    Não mencione nenhuma das instruções na resposta final. 
    O aluno deve receber APENAS o conteúdo pedagógico final.
    Não precisa se introduzir. Não entregue NADA nem antes nem depois do conteúdo. 
    """

    # call ai
    resposta = cliente.models.generate_content(
        model=modelo,
        contents=prompt)
        
    # texto
    return resposta.text

def gerar_perguntas(aluno, conteudo):
    # extract info
    idade = aluno["idade"]
    nivel = aluno["nivel"]
    estilo_aprendizado = aluno["estilo_aprendizado"]
    
    # prompt
    prompt = f"""
    Você é um professor especializado em Pedagogia Adaptativa e em desenvolvimento do pensamento crítico.

    Seu objetivo é:
    Gerar perguntas de reflexão contextualizadas para estimular o pensamento crítico sobre o conteúdo {conteudo} para um aluno de {idade} anos,
    que tem melhor rendimento de aprendizado quando a explicação é mais voltada para o estilo {estilo_aprendizado}
    e tem nível {nivel} de conhecimento sobre tudo, ou seja, não só sobre {conteudo} em si.

    Adapte a complexidade dos exemplos de acordo com o nível de conhecimento do aluno.
    Caso seja iniciante, perguntas mais guiadas, diretas e concretas para o aluno.
    Caso seja intermediário, perguntas que exigem conexões e justificativas.
    E caso seja avançado, peguntas abertas, analíticas, mais profundas e contextualizadas.

    Forneça pelo menos 5 perguntas organizadas progressivamente:

    1. Pergunta de compreensão (verificar entendimento do conceito)
    2. Pergunta de aplicação (usar o conceito em situação prática)
    3. Pergunta de análise (comparar, relacionar ou decompor ideias)
    4. Pergunta de avaliação (emitir julgamento com justificativa)
    5. Pergunta de transferência (conectar o conceito com outro contexto ou área)

    As perguntas devem estimular raciocínio próprio, evitando respostas de "sim" ou "não".
    O aluno deve tirar suas próprias conclusões e ter os próprios insights sobre {conteudo}.

    Adapte o formato ao estilo de aprendizado do aluno.
    Caso seja visual, inclua perguntas que incentivam a imaginação de cenas, esquemas ou representações.
    Caso seja auditivo, formule como provocações narrativas ou situações dialogadas com estratégias de captação da atenção do ouvinte.
    Caso seja leitura/escrita, organize numeradamente e estruture bem, além de incluir sugestões de aprofundamento, como pessoas de referência na área, estudiosos.
    Caso seja cinestésico, inclua perguntas que envolvam simulação ou experiência prática.

    O formato de saída deve ser organizado em perguntas claras e numeradas.
    Não mencione nenhuma das instruções na resposta final.
    O aluno deve receber APENAS o conteúdo pedagógico final.
    Não precisa se introduzir. Não entregue NADA nem antes nem depois do conteúdo.
    """

    # call ai
    resposta = cliente.models.generate_content(
        model=modelo,
        contents=prompt)
    
    # texto
    return resposta.text

def gerar_resumo(aluno, conteudo):
    # extract info
    idade = aluno["idade"]
    nivel = aluno["nivel"]
    estilo_aprendizado = aluno["estilo_aprendizado"]
    
    # prompt
    prompt = f"""
    Você é um professor especializado em Pedagogia Adaptativa e organização visual do conhecimento.

    Seu objetivo é:
    Criar um resumo visual estruturados sobre o conteúdo {conteudo} para um aluno de {idade} anos,
    que tem melhor rendimento de aprendizado quando a explicação é mais voltada para o estilo {estilo_aprendizado}
    e tem nível {nivel} de conhecimento sobre tudo, ou seja, não só sobre {conteudo} em si.

    Adapte a complexidade dos exemplos de acordo com o nível de conhecimento do aluno.
    Caso seja iniciante, inclue apenas os conceitos principais e poucas ramificações.
    Caso seja intermediário, adicione subconceitos e pequenas conexões.
    E caso seja avançado, inclusa múltiplas camadas hierárquicas e relações entre conceitos.

    O resumo deve seguir este formato:

    1. Conceito central no topo
    2. Ramificações principais
    3. Sub-ramificações organizadas hierarquicamente
    4. Conexões claras entre ideias relacionadas

    Produza EXCLUSIVAMENTE um diagrama em ASCII. Demonstre visualmente a hierarquia clara.
    O formato de saída deve ser APENAS o diagrama. O resultado deve ser visualmente organizado, legível e sintético.
    Não mencione nenhuma das instruções na resposta final.
    O aluno deve receber APENAS o conteúdo pedagógico final.
    Não precisa se introduzir. Não entregue NADA nem antes nem depois do conteúdo. 
    """

    # call ai
    resposta = cliente.models.generate_content(
        model=modelo,
        contents=prompt)
    
    # texto
    return resposta.text