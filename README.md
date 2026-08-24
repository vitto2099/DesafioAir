# Suíte de Avaliação do Cosmetic Bot (Desafio de Estágio)

Este repositório contém a suíte enxuta e automatizada de avaliação para o **Cosmetic Bot**, utilizando **DeepEval** e **Ollama local** (ou Gemini via API).

---

## 📁 Estrutura Enxuta do Projeto

```text
DesafioAir/
├── .venv/                      # Ambiente virtual Python
├── catalogo.json               # Fonte da verdade com os 25 produtos fictícios
├── prompt.txt                  # Arquivo único de prompt do sistema (otimizado)
├── chatbot.py                  # Módulo principal do bot (perguntar(pergunta))
├── juiz.py                     # Módulo de integração do modelo juiz (Ollama/Gemini)
├── golden_dataset.py           # Golden Dataset com 12 casos (4 categorias obrigatórias)
├── test_suite.py               # Suíte unificada de testes Pytest/DeepEval
├── executar_avaliacao.py       # Script de avaliação automatizada dos testes
├── RELATORIO_DESAFIO.md        # Relatório Final detalhado (3 a 5 páginas)
└── exemplo/                    # Pasta original fornecida (mantida intacta)
```

---

## 🚀 Como Executar

### 1. Ativação do Ambiente Virtual

Certifique-se de que o Ollama está rodando localmente (`ollama serve`).

```powershell
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

---

### 2. Conversar com o Bot no Terminal

```bash
python chatbot.py
```

---

### 3. Rodar a Avaliação Automatizada com DeepEval

**Via Pytest / DeepEval:**
```bash
deepeval test run test_suite.py
```

**Via Script de Avaliação:**
```bash
python executar_avaliacao.py
```

---

## 📊 Métricas

- **Answer Relevancy** ($\ge 0{,}7$)
- **Faithfulness** ($\ge 0{,}8$)
- **G-Eval Conformidade de Claims** ($\ge 0{,}8$)

---

## 📝 Documento Principal

- [RELATORIO_DESAFIO.md](RELATORIO_DESAFIO.md): Relatório acadêmico/corporativo completo.
