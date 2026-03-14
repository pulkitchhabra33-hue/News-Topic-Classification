import tensorflow as tf

model = tf.keras.models.load_model("news_classifier.keras")
print("Model loaded successfully")
model.summary()