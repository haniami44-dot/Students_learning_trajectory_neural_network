import os
from tensorflow.keras.models import load_model
from django.conf import settings

BASE_DIR = settings.BASE_DIR

MODEL_BASIC_PATH = os.path.join(BASE_DIR, "DL_models", "base_model.h5")

MODEL_ADVANCED_PATH = os.path.join(BASE_DIR, "DL_models", "advanced_model.h5")

MODEL_BASIC = load_model(MODEL_BASIC_PATH)

MODEL_ADVANCED = load_model(MODEL_ADVANCED_PATH)