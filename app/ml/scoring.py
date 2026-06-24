import numpy as np


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1)
        * np.linalg.norm(vec2)
    )


def calculate_scores(
    before_features,
    after_features
):
    similarity = cosine_similarity(
        before_features,
        after_features
    )

    cleanliness_score = float(
        round(
            (1 - similarity) * 100,
            2
        )
    )

    confidence_score = float(
        round(
            min(
                0.95,
                abs(similarity)
            ),
            2
        )
    )

    return (
        cleanliness_score,
        confidence_score
    )