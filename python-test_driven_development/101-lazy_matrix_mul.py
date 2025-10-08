#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError(e)
    except TypeError as e:
        raise TypeError(e)
