import torch
from torchvision import models
from torchvision import transforms
from PIL import Image


weights = models.ResNet50_Weights.DEFAULT

model = models.resnet50(weights=weights)

model.fc = torch.nn.Identity()

model.eval()


transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ]
)


def extract_features(image_path):
    image = Image.open(image_path).convert("RGB")

    tensor = transform(image)

    tensor = tensor.unsqueeze(0)

    with torch.no_grad():
        features = model(tensor)

    return features.squeeze().numpy()