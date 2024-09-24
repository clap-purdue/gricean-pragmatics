# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from minicons import scorer
from minicons import cwe
import torch

from gricean_pragmatics.config import Config, Language

__all__ = ["MiniconsScoring"]

"""
from gricean_pragmatics.config import Config
from gricean_pragmatics.scoring import MiniconsScoring
config = Config(model_name="bert-base-uncased", language="en")
x = MiniconsScoring(config)
x.score("get_surprisal")

from gricean_pragmatics.metrics import GPMetrics
# compute gricean metrics
"""

class MiniconsScoring(Language):
    def __init__(self, config: Config) -> None:
        super().__init__(config)
        self.config = config
        self.device = self.get_device()

    def get_device(self):
        if self.config.device == "cuda":
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            if device:
                print(f"Using {device}")
        elif self.config.device == "mps":
            device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
            if device:
                print(f"Using {device}")
        elif self.config.device is None:
            print("Using cpu")
    
    def response_surp_mean(self, response, len, model):
        if len > 1: # need at least two words to have a surp score
            # Sequence Surprisal, normalized by number of tokens - lambda x: -x.mean(0).item()
            score = model.sequence_score([response], reduction = lambda x: -x.mean(0).item())
            return round(score[0],2)
        else:
            return np.nan
        
    def get_surprisal(self):
        mlm_model = scorer.MaskedLMScorer(self.config.model_name)
        temp = self.response_surp_mean(self.config.response, self.config.length, mlm_model)
        return temp

    def score(self, function_name, *args):
        if hasattr(self, function_name):
            function = getattr(self, function_name)
            return function(*args)
        else:
            return f"Function '{function_name}' not found."
