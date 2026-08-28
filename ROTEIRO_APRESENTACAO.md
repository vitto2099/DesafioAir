# Guia de Apresentação — Cosmetic Bot (DeepEval)

> **Projeto**: Suíte de Avaliação de LLMs com DeepEval  
> **Autor**: Vitor Camargo Kunicki  

---

## 1. O que é o projeto e o que fizemos

* **O ponto de partida**: Recebemos uma base inicial na pasta `exemplo/` com um catálogo fictício de 25 cosméticos e um chatbot baseline rodando com um prompt genérico.
* **O que fizemos**: Desenvolvemos do zero uma **suíte completa de avaliação automatizada (LLM Evals) com DeepEval e LLM-as-a-Judge**, criamos um **Golden Dataset de 12 casos** cobrindo todas as frentes de risco, e otimizamos as diretrizes do bot para torná-lo seguro, preciso e em conformidade regulatória.

---

## 2. Como estava antes (O Bot Baseline)

Durante os testes na versão inicial que recebemos, identificamos três falhas críticas:

1. **Alucinação de produtos e preços**: Quando perguntado sobre itens inexistentes (ex.: "BotoxMax"), o bot inventava preços e garantia falsamente que tínhamos o produto em estoque.
2. **Risco regulatório grave (Normas da Anvisa)**: Prometia "cura definitiva" para acne severa e dermatite usando cosméticos simples, o que é proibido por lei para cosméticos e coloca o usuário em risco.
3. **Falta de foco e escopo aberto**: Respondia normalmente a perguntas sobre receitas culinárias, previsão do tempo e futebol, descaracterizando o papel de assistente de vendas do e-commerce.

---

## 3. O que construímos para avaliar e corrigir

1. **Golden Dataset Estruturado (`golden_dataset.py`)**:
   - **12 casos de teste** cobrindo 4 categorias:
     - *Consulta Direta*: Factualidade de preços, marcas e ingredientes.
     - *Recomendação por Perfil*: Matriz de decisão para peles oleosa, seca e sensível.
     - *Fora de Escopo*: Perguntas que exigem recusa educada.
     - *Adversarial*: Tentativas de forçar diagnósticos médicos e promessas de cura.
2. **Métricas Automatizadas com DeepEval (`test_suite.py` / `juiz.py`)**:
   - `Answer Relevancy` ($\ge 0.7$): Respostas diretas e sem divagação.
   - `Faithfulness` ($\ge 0.8$): Fidelidade estrita aos 25 produtos do catálogo.
   - `G-Eval "Conformidade de Claims"` ($\ge 0.8$): Proibição de promessas terapêuticas e obrigatoriedade de recomendar dermatologistas.
3. **Otimização de Prompt (`prompt.txt`)**:
   - Blindagem com regras rígidas de factualidade, restrição de escopo e conduta ética em saúde.

---

## 4. Como ficou depois (Versão Otimizada)

* **Fidelidade Total (Faithfulness: 0.95 – 1.00)**: O bot parou 100% de inventar produtos fora do catálogo e passou a informar preços e ingredientes com exatidão.
* **Conformidade Ética e Legal (G-Eval: 0.95)**: Em qualquer menção a inflamação, dor ou sintomas graves, o bot recusa promessas de cura e orienta o cliente a consultar um dermatologista.
* **Escopo Protegido**: Recusa educadamente assuntos aleatórios (esportes, receitas) e redireciona o cliente para o catálogo da loja.
* **Execução Simples (`main.py`)**: Toda a suíte roda de forma automatizada com apenas um comando no terminal.

---

## 5. Veredito: Como foi fazer o projeto

> *"A experiência de desenvolver este desafio mostrou na prática que **colocar LLMs em produção não é tentativa e erro de prompts, mas sim Engenharia de Avaliação (Evals)**.*  
> *Ter um Golden Dataset bem desenhado e métricas automatizadas com o DeepEval permitiu enxergar com clareza os riscos de negócio e jurídicos que uma LLM pode trazer se não for monitorada. O processo de medir a baseline, identificar as falhas e ver os scores subirem para mais de 95% após a otimização comprovou a importância de criar pipelines de testes contínuos para inteligência artificial."*
