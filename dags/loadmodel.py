from transformers import DistilBertTokenizer
from transformers import TextClassificationPipeline
from transformers import TFDistilBertForSequenceClassification, TFTrainer, TFTrainingArguments
import tensorflow as tf

class ModelLoader:

    def __init__(self):
        self.tokenizer = DistilBertTokenizer.from_pretrained("/saved_models", verbose=False)
        self.model = TFDistilBertForSequenceClassification.from_pretrained("/saved_models")

    def load_model(self, test_texts):
        predict_input = self.tokenizer.encode(
            test_texts,
            truncation=True,
            padding=True,
            return_tensors='tf'
        )
        output = self.model(predict_input)[0]
        prediction_value = tf.argmax(output, axis=1).numpy()[0]
        return prediction_value, test_texts

if __name__ == '__main__':
    load_model(text)