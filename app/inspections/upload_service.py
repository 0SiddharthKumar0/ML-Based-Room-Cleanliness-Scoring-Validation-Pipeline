import os
import shutil

from fastapi import UploadFile


def save_image(
    inspection_id: int,
    image_type: str,
    file: UploadFile
):
    folder = f"data/uploads/inspection_{inspection_id}"

    os.makedirs(folder, exist_ok=True)

    extension = file.filename.split(".")[-1]

    filename = f"{image_type}.{extension}"

    file_path = os.path.join(
        folder,
        filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return file_path