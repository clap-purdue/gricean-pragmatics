# gricean-pragmatics

A library of five metrics evaluating large language models' pragmatic competence:

- **Naturalness**: LLMs will generate surprisal scores as a proxy to text naturalness for each sentence in a minimal pair, which reflect how unexpected a sentence is, given the preceding context. We hypothesize that if LLMs show pragmatic sensitivity, LLMs should assign a lower surprisal score to the intended implied meaning in an appropriate context. For example, for Utterance: “Anna rolls her eyes and says, he’s a real genius. What does Anna intend to mean?” (a) He is very smart (b) He is not smart at all, a LLM’s success means that surprisals difference between Utterance and (b) should be smaller than Utterance and (a).

    \[
    	Δ _S_ = _S_(_U_a_, _C_) - _S_(_U_b_, _C_)
    \]
    
    A positive \( Δ S \) (i.e., \( Δ S > 0 \)) indicates that the model assigns a lower surprisal score to the implied meaning, reflecting sensitivity to the pragmatic context. This suggests the model successfully recognizes the intended implication.
  
- **Sensitivity to different Shades of Meaning (SSM)**
- **Pragmatic Reasoning Chains (PRC)**
- **Implicature Recovery Rate (IRR)**
- **Pragmatic Sensitivity Index (PSI)**
