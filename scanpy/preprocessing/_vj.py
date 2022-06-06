from typing import Optional, Tuple, Collection, Union
from warnings import warn

import numba
import numpy as np
import pandas as pd
from scipy.sparse import issparse, isspmatrix_csr, isspmatrix_coo
from scipy.sparse import spmatrix, csr_matrix
from sklearn.utils.sparsefuncs import mean_variance_axis

from anndata import AnnData
from ._docs import (
    doc_expr_reps,
    doc_obs_qc_args,
    doc_qc_metric_naming,
    doc_obs_qc_returns,
    doc_var_qc_returns,
    doc_adata_basic,
)
from .._utils import _doc_params


def minmax(data):
    """
    Computes min max of values in the anndata X
    """
    print("min = " + str(np.min(data.X)))
    print("max = " + str(np.max(    data.X)))
