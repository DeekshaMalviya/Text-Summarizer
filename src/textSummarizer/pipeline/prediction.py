from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline



class PredictionPipeline:
  def __init__(self):
    self.config = ConfigurationManager().get_model_evaluation_config() # here by this i can access my model and tokenizer presented inside artifacts 

     

# Predict method

  def predict(self,text):

    tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
    gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
#some arguments

    pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)
##calling the pipeline

##
    print("Dialogue: ")
    print(text)

    output = pipe(text, **gen_kwargs)[0]["summary_text"]

    print("\nModel Summary:")
    print(output)
## this is the prediction for the model

    return output