import urllib.request
from os import path
from pathlib import Path
from typing import Optional


class Yolov10TestConstants:
    YOLOV10N_MODEL_URL = "https://huggingface.co/kadirnar/Yolov10/blob/main/yolov10n.pt"
    yolov10N_MODEL_PATH = "Yolov10/yolov10n.pt"

    yolov10S_MODEL_URL = "https://huggingface.co/kadirnar/Yolov10/blob/main/yolov10s.pt"
    yolov10S_MODEL_PATH = "Yolov10/yolov10s.pt"

    yolov10M_MODEL_URL = "https://huggingface.co/kadirnar/Yolov10/blob/main/yolov10m.pt"
    yolov10M_MODEL_PATH = "Yolov10/yolov10m.pt"

    yolov10L_MODEL_URL = "https://huggingface.co/kadirnar/Yolov10/blob/main/yolov10l.pt"
    yolov10L_MODEL_PATH = "Yolov10/yolov10l.pt"

    yolov10X_MODEL_URL = "https://huggingface.co/kadirnar/Yolov10/blob/main/yolov10x.pt"
    yolov10X_MODEL_PATH = "Yolov10/yolov10x.pt"

    yolov10B_MODEL_URL = "https://huggingface.co/kadirnar/Yolov10/blob/main/yolov10b.pt"
    yolov10B_MODEL_PATH = "Yolov10/yolov10b.pt"




def download_yolov10n_model(destination_path: Optional[str] = None):
    if destination_path is None:
        destination_path = Yolov10TestConstants.yolov10N_MODEL_PATH

    Path(destination_path).parent.mkdir(parents=True, exist_ok=True)

    if not path.exists(destination_path):
        urllib.request.urlretrieve(
            Yolov10TestConstants.yolov10N_MODEL_URL,
            destination_path,
        )


def download_yolov10s_model(destination_path: Optional[str] = None):
    if destination_path is None:
        destination_path = Yolov10TestConstants.yolov10S_MODEL_PATH

    Path(destination_path).parent.mkdir(parents=True, exist_ok=True)

    if not path.exists(destination_path):
        urllib.request.urlretrieve(
            Yolov10TestConstants.yolov10S_MODEL_URL,
            destination_path,
        )


def download_yolov10m_model(destination_path: Optional[str] = None):
    if destination_path is None:
        destination_path = Yolov10TestConstants.yolov10M_MODEL_PATH

    Path(destination_path).parent.mkdir(parents=True, exist_ok=True)

    if not path.exists(destination_path):
        urllib.request.urlretrieve(
            Yolov10TestConstants.yolov10M_MODEL_URL,
            destination_path,
        )


def download_yolov10l_model(destination_path: Optional[str] = None):
    if destination_path is None:
        destination_path = Yolov10TestConstants.yolov10L_MODEL_PATH

    Path(destination_path).parent.mkdir(parents=True, exist_ok=True)

    if not path.exists(destination_path):
        urllib.request.urlretrieve(
            Yolov10TestConstants.yolov10L_MODEL_URL,
            destination_path,
        )


def download_yolov10x_model(destination_path: Optional[str] = None):
    if destination_path is None:
        destination_path = Yolov10TestConstants.yolov10X_MODEL_PATH

    Path(destination_path).parent.mkdir(parents=True, exist_ok=True)

    if not path.exists(destination_path):
        urllib.request.urlretrieve(
            Yolov10TestConstants.yolov10X_MODEL_URL,
            destination_path,
        )

def download_yolov10b_model(destination_path: Optional[str] = None):
    if destination_path is None:
        destination_path = Yolov10TestConstants.yolov10B_MODEL_PATH

    Path(destination_path).parent.mkdir(parents=True, exist_ok=True)

    if not path.exists(destination_path):
        urllib.request.urlretrieve(
            Yolov10TestConstants.yolov10X_MODEL_URL,
            destination_path,
        )
