
from easynmt import EasyNMT
import os
from constant import languages
os.environ["CUDA_VISIBLE_DEVICES"]=""
class inferenceManager:
    def __init__(self):
        os.environ['MKL_THREADING_LAYER'] = 'GNU'
        self.model="m2m_100_1.2B"
        self.nmt_model = None


    def start_up(self):
        global nmt_model
        
        self.nmt_model = EasyNMT(self.model,device="cpu")
                    



    def translate_sentences(self,sentences,lang):
        if lang not in languages:
            return 400, "Language not supported"
        try:
            result = self.nmt_model.translate(sentences,target_lang=lang)
            return 200, result
        except Exception as e:
            return 500, e
    


    
        
   
