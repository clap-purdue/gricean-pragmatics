# gricean-pragmatics

Metrics evaluating large language models' pragmatic competence:

- **Naturalness**: LLMs will generate surprisal scores as a proxy to text naturalness for each sentence in a minimal pair, which reflect how unexpected a sentence is, given the preceding context. We hypothesize that if LLMs show pragmatic sensitivity, LLMs should assign a lower surprisal score to the intended implied meaning in an appropriate context. For example, for Utterance: “Anna rolls her eyes and says, he’s a real genius. What does Anna intend to mean?” (a) He is very smart (b) He is not smart at all, a LLM’s success means that surprisals difference between Utterance and (b) should be smaller than Utterance and (a).

Let:
- \( S(U, C) \) be the surprisal score of an utterance \( U \) given the preceding context \( C \).
- \( U_a \) represent the literal meaning ("He is very smart").
- \( U_b \) represent the intended implied meaning ("He is not smart at all").

We hypothesize that the surprisal score for the intended implied meaning \( U_b \) should be lower than the surprisal score for the literal meaning \( U_a \) in the given context \( C \).

The naturalness metric is computed as:

\[
\Delta S = S(U_a, C) - S(U_b, C)
\]

Where:
- \( \Delta S \) is the difference in surprisal scores between the literal and implied meanings.
- If \( \Delta S > 0 \), it indicates that the LLM is sensitive to the pragmatic context, assigning a lower surprisal score to the implied meaning.

A smaller surprisal score for \( U_b \) (i.e., \( \Delta S > 0 \)) suggests that the LLM successfully recognizes the intended implied meaning.

  
- **Sensitivity to different Shades of Meaning (SSM)**: The (cosine) similarity will be calculated to examine the extent to which LLMs can tease apart pragmatically enriched (implied) meaning from the entailed meaning and other layers of meanings. Similarities between Alex was not unaware of the issue and Alex was slightly aware of the issue would be compared to the similarity score between Alex was aware of the issue and Alex was slightly aware of the issue. We hypothesize that pragmatic relations are not as strong as entailment but still stronger than neutral relations, leading to the following rank of similarity: entailment > implication > neutral. We are aware that cosine similarity is symmetric, whereas the utterance relations here are not. We plan to calculate weighted cosine similarity, in combination with prompt engineering techniques to directly probe LLMs’ labels for relations.
- **Pragmatic Reasoning Chains (PRC)**: PRC involves evaluating the LLM's ability to follow multi-step pragmatic reasoning. For example, given a conversational context that requires understanding a scalar implicature ("some" implying "not all"), an LLM is probed using prompt engineering to generate the reasoning steps of how the “not all” inference is derived. LLM is assessed for its ability to generate the appropriate reasoning steps that align with formal pragmatics’ proposal (c.f., REASONING STEPS).
- **Implicature Recovery Rate (IRR)**: successful_recoveries: The number of implicature errors that were successfully recovered by the LLM after introducing noise or ambiguity. total_errors: The total number of implicature errors introduced during the evaluation. The IRR metric calculates the ratio of successful_recoveries to total_errors. The output is a percentage of implicatures that were successfully recovered. This metric concerns the robustness of LLMs in handling and resolving implicature-related ambiguities by measuring how well they can recover from initial errors.
- **Pragmatic Sensitivity Index (PSI)**: The PSI would measure the model’s sensitivity to subtle changes in context that should trigger different implicatures. For instance, changing a single word in a context could alter the expected implicature. PSI would assess whether the LLM correctly adjusts its output based on these subtle contextual shifts. For example, we plan to scramble nouns and replace key words with nonsense words, to examine the extent to which LLMs’ pragmatic sensitivity varies. 
