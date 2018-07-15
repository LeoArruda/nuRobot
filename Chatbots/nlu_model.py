from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import json

def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='Lambton')
    print(model_directory)

def run_nlu():
    interpreter = Interpreter.load('../Chatbots/projects/Lambton/models/nlu/default/current')
    print("\n===========================================\n")
    print(json.dumps(interpreter.parse("I am planning to visit Lambton College to check MADT classes."), indent=4))
    print("\n===========================================\n")
    print(json.dumps(interpreter.parse("You can call me Thomas."), indent=4))
    print("\n===========================================\n")
    print(json.dumps(interpreter.parse("I am Shakira."), indent=4))
    print("\n===========================================\n")
    print(json.dumps(interpreter.parse("Can you give me a hug?"), indent=4))
    print("\n===========================================\n")
    print(json.dumps(interpreter.parse("What is the weather in Toronto?"), indent=4))


if __name__ == '__main__':
    #train_nlu('../Chatbots/projects/Lambton/intents/',
    #'../Chatbots/projects/Lambton/config_mitie.yml',
    #'../Chatbots/projects/Lambton/models/nlu/default/current')
    run_nlu()
