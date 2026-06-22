from app.ml.feature_extractor import extract_features

print("Loading model...")

features = extract_features(
    "data/uploads/inspection_1/before.jpg"
)

print(features.shape)