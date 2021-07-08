import tensorflow.keras as keras
import tensorflowjs as tfjs

model = keras.models.load_model("mask_detector.model")
tfjs.converters.save_keras_model(model, "tfjs_model")
