# gricean-pragmatics

A library of five metrics evaluating large language models' pragmatic competence:

1. **Naturalness**: LLMs will generate surprisal scores as a proxy to text naturalness for each sentence in a minimal pair, which reflect how unexpected a sentence is, given the preceding context. Hypothetically, if LLMs show pragmatic sensitivity, LLMs should assign a lower surprisal score to the intended implied meaning in an appropriate context. For example, for Utterance (_U_): “Anna rolls her eyes and says, he’s a real genius. What does Anna intend to mean?” (a) He is very smart (b) He is not smart at all, a LLM’s success means that surprisals difference between Utterance and (b) should be smaller than Utterance and (a).

    \[
    	Δ _S_ = _S_(_U_a_, _C_) - _S_(_U_b_, _C_)
    \]
    
    A positive \( Δ S \) (i.e., \( Δ S > 0 \)) indicates that the model assigns a lower surprisal score to the implied meaning, reflecting sensitivity to the pragmatic context. This suggests the model successfully recognizes the intended implication.

2. **Sensitivity to different Shades of Meaning (SSM)**
3. **Pragmatic Reasoning Chains (PRC)**
4. **Implicature Recovery Rate (IRR)**
5. **Pragmatic Sensitivity Index (PSI)**
