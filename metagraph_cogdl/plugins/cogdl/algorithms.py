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
        NumpyMatrixType,
        NumpyNodeMap,
    )

    @concrete_algorithm("embedding.train.hope.katz")
    def cogdl_hope_katz_train(
        graph: NetworkXGraph, embedding_size: int, beta: float
    ) -> Tuple[NumpyMatrixType, NumpyNodeMap]:
        model = cogdl.models.emb.hope.HOPE(embedding_size, beta)
        np_embedding_matrix = model.train(
            graph.value
        )  # performs NetworkX -> SciPy adjacency matrix underneath
        node2index = NumpyNodeMap(
            np.arange(len(graph.value.nodes())),
            nodes=np.array(list(graph.value.nodes())),
        )
        return (np_embedding_matrix, node2index)

    @concrete_algorithm("embedding.train.line")
    def cog_dl_line_train(
        graph: NetworkXGraph,
        walks_per_node: int,
        negative_sample_count: int,
        embedding_size: int,
        epochs: int,
        learning_rate: float,
        batch_size: int,
    ) -> Tuple[NumpyMatrixType, NumpyNodeMap]:
        # walk_length is a poorly named parameter ; in the underlying code, we have
        # num_total_training_examples = walk_length * walks_per_node * len(graph.value.nodes)
        # Thus, walk_length can be used to specify the number of epochs
        model = cogdl.models.emb.line.LINE(
            dimension=embedding_size,
            walk_length=epochs,
            walk_num=walks_per_node,
            negative=negative_sample_count,
            batch_size=batch_size,
            alpha=learning_rate,
            order=3,
        )
        np_embedding_matrix = model.train(graph.value)
        node2index = NumpyNodeMap(
            np.arange(len(graph.value.nodes())),
            nodes=np.array(list(graph.value.nodes())),
        )
        return (np_embedding_matrix, node2index)
