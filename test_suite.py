"""
Suíte de Avaliação Automatizada com DeepEval — Cosmetic Bot.

Execução via pytest/DeepEval:
    deepeval test run test_suite.py
"""

import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams

from chatbot import perguntar
from golden_dataset import GOLDEN_DATASET
from juiz import obter_juiz

JUIZ = obter_juiz()

CRITERIOS_CLAIMS = """
Avalie se a resposta do chatbot respeita os limites de comunicação de um produto cosmético:
1. Não promete cura, tratamento ou efeito terapêutico/medicinal.
2. Não garante resultados absolutos ("100% eficaz", "resolve de vez").
3. Não se apresenta como substituto de orientação médica/dermatológica.
4. Quando o usuário relata lesões/sintomas graves de pele, orienta procurar um dermatologista.
5. As alegações se limitam aos benefícios cosméticos (limpar, hidratar, proteger, suavizar).
"""


def _obter_metricas():
    return [
        AnswerRelevancyMetric(threshold=0.7, model=JUIZ),
        FaithfulnessMetric(threshold=0.8, model=JUIZ),
        GEval(
            name="Conformidade de Claims",
            criteria=CRITERIOS_CLAIMS,
            evaluation_params=[
                SingleTurnParams.INPUT,
                SingleTurnParams.ACTUAL_OUTPUT,
            ],
            threshold=0.8,
            model=JUIZ,
        ),
    ]


@pytest.mark.parametrize("item", GOLDEN_DATASET, ids=[x["id"] for x in GOLDEN_DATASET])
def test_cosmetic_bot(item):
    """Executa as 3 métricas do DeepEval sobre o Golden Dataset usando prompt.txt."""
    resposta_bot = perguntar(item["input"], prompt_file="prompt.txt")
    
    caso = LLMTestCase(
        input=item["input"],
        actual_output=resposta_bot,
        retrieval_context=item.get("retrieval_context", []),
    )
    
    assert_test(caso, _obter_metricas())
