import metagraph as mg
from metagraph import concrete_algorithm
from .. import has_cogdl
from typing import Tuple

if has_cogdl:
    import cogdl.models
    import numpy as np
    import networkx as nx
    from metagraph.plugins.networkx.types import NetworkXGraph
    from metagraph.plugins.numpy.types import (
        NumpyMatrix,
        NumpyNodeMap,
    )

    @concrete_algorithm("embedding.train.hope.katz")
    def cogdl_hope_katz_train(
        graph: NetworkXGraph, embedding_size: int, beta: float
    ) -> Tuple[NumpyMatrix, NumpyNodeMap]:
        model = cogdl.models.emb.hope.HOPE(embedding_size, beta)
        np_embedding_matrix = model.train(
            graph.value
        )  # performs NetworkX -> SciPy adjacency matrix underneath
        matrix = NumpyMatrix(np_embedding_matrix)
        node2index = NumpyNodeMap(
            np.arange(len(graph.value.nodes())),
            node_ids=dict(map(reversed, enumerate(sorted(graph.value.nodes())))),
        )
        return (matrix, node2index)
