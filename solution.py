import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 82953459 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: 
    p_value = st.permutation_test((x, y), lambda x, y, axis: np.mean(x, axis=axis) - np.mean(y, axis=axis), 
                 vectorized=True, 
                 n_resamples=500,
                 alternative='greater').pvalue 
    alpha = 0.07
    return p_value < alpha
