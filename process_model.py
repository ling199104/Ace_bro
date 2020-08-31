
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import tensorflow as tf
from ms_translator import get_trans


gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

MAX_SEQUENCE_LENGTH = 30 # max length of text (words) including padding

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

classes = ["neutral", "happy", "sad", "hate","anger"]

model = load_model('checkpoint-0.912.h5')
model._make_predict_function()

def response(text):
    text = get_trans(text) #zh-tw to en-us
    text = [text]
    sequences_test = tokenizer.texts_to_sequences(text)
    data_int_t = pad_sequences(sequences_test, padding='pre', maxlen=(MAX_SEQUENCE_LENGTH-5))
    data_test = pad_sequences(data_int_t, padding='post', maxlen=(MAX_SEQUENCE_LENGTH))
    y_prob = model.predict(data_test)
    for n, prediction in enumerate(y_prob):
        pred = y_prob.argmax(axis=-1)[n]
        prediction = classes[pred]
    return prediction
