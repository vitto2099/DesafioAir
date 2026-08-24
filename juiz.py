"""
Configuração do modelo juiz do DeepEval.
Suporta Ollama local por padrão (ou Gemini via API).
"""

import os


def obter_juiz():
    provider = os.getenv("JUIZ_PROVIDER", "ollama").lower()

    if provider == "gemini":
        from deepeval.models import GeminiModel

        return GeminiModel(
            model=os.getenv("JUIZ_MODEL", "gemini-2.0-flash"),
            api_key=os.getenv("GEMINI_API_KEY"),
        )

    from deepeval.models import OllamaModel

    modelo = os.getenv("JUIZ_MODEL", os.getenv("LLM_MODEL", "llama3.2:3b"))
    url = os.getenv("OLLAMA_URL", "http://localhost:11434")

    return OllamaModel(
        model=modelo,
        base_url=url,
    )
