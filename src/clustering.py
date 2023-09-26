from sklearn.base import ClusterMixin
from sklearn.cluster import (
    OPTICS,
    AffinityPropagation,
    AgglomerativeClustering,
    KMeans,
    MeanShift,
)
from sklearn.mixture import GaussianMixture

NB_CLUSTER_MIN = 2
NB_CLUSTER_MAX = 6  # non inclus


def initiate_cluster_models(
    nb_clusters_min: int,
    nb_clusters_max: int,
    seed: int,
) -> dict[str, ClusterMixin]:
    """
    Todo

    :param nb_clusters_min:
    :param nb_clusters_max:
    :param seed:
    :return:
    """
    dict_kmeans = {
        f"KMeans{i}": KMeans(n_clusters=i, random_state=seed)
        for i in range(nb_clusters_min, nb_clusters_max)
    }

    dict_gmm = {
        f"GMM{i}": GaussianMixture(
            n_components=i, covariance_type="full", random_state=seed
        )
        for i in range(nb_clusters_min, nb_clusters_max)
    }

    dict_cah_ward = {
        f"CAH (Ward) {i}": AgglomerativeClustering(n_clusters=i)
        for i in range(nb_clusters_min, nb_clusters_max)
    }

    dict_cah_average = {
        f"CAH (average linkage) {i}": AgglomerativeClustering(
            n_clusters=i, linkage="average"
        )
        for i in range(nb_clusters_min, nb_clusters_max)
    }

    dict_cah_simple = {
        f"CAH (single linkage) {i}": AgglomerativeClustering(
            n_clusters=i, linkage="single"
        )
        for i in range(nb_clusters_min, nb_clusters_max)
    }

    dict_cah_complete = {
        f"CAH (complete linkage) {i}": AgglomerativeClustering(
            n_clusters=i, linkage="complete"
        )
        for i in range(nb_clusters_min, nb_clusters_max)
    }

    model_clusters = {
        **dict_kmeans,
        **dict_gmm,
        **dict_cah_ward,
        **dict_cah_average,
        **dict_cah_simple,
        **dict_cah_complete,
        "OPTICS": OPTICS(),
        "MeanShift": MeanShift(),
        "AffinityPropagation": AffinityPropagation(random_state=seed),
    }

    return model_clusters
