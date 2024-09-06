# gricean-pragmatics

A library of five metrics evaluating large language models' pragmatic competence:

1. **Naturalness**: LLMs will generate surprisal scores as a proxy to text naturalness for each sentence in a minimal pair, which reflect how unexpected a sentence is, given the preceding context. Hypothetically, if LLMs show pragmatic sensitivity, LLMs should assign a lower surprisal score to the intended implied meaning in an appropriate context.
2. **Sensitivity to different Shades of Meaning (SSM)**
3. **Pragmatic Reasoning Chains (PRC)**
4. **Implicature Recovery Rate (IRR)**
5. **Pragmatic Sensitivity Index (PSI)**
