# Suíte de Avaliação do Cosmetic Bot (Desafio de Estágio)

Este repositório contém a suíte completa de avaliação automatizada para o **Cosmetic Bot**, utilizando **DeepEval** e **Ollama local** (ou Gemini via API).

---

## ⚡ Como Rodar Tudo (Apenas 2 Passos)

### 1. Instalar as dependências:
```bash
pip install -r requirements.txt
```

### 2. Rodar a avaliação completa:
```bash
python main.py
```

*(Se quiser conversar interativamente com o bot no terminal, basta rodar `python main.py --chat`).*

---

## 📁 Estrutura do Projeto

```text
DesafioAir/
├── requirements.txt            # Arquivo de dependências do projeto
├── main.py                     # Ponto de entrada único para rodar a suíte completa
├── prompt.txt                  # Instruções de sistema do bot (otimizado)
├── catalogo.json               # Fonte da verdade com os 25 produtos fictícios
├── chatbot.py                  # Módulo principal do bot
├── juiz.py                     # Módulo de integração do modelo juiz (Ollama/Gemini)
├── golden_dataset.py           # Golden Dataset com 12 casos (4 categorias)
├── test_suite.py               # Suíte Pytest/DeepEval
├── RELATORIO_DESAFIO.md        # Relatório Final detalhado (3 a 5 páginas)
└── exemplo/                    # Pasta original do desafio (mantida intacta)
```

---

## 📝 Documento Principal

- [RELATORIO_DESAFIO.md](RELATORIO_DESAFIO.md): Relatório acadêmico/corporativo completo.
