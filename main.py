from fastapi import FastAPI, Query,Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
from typing import List
from fastapi import FastAPI 
from inferenceManager import inferenceManager
import os
os.environ["CUDA_VISIBLE_DEVICES"]=""


tags_metadata = [
    {
        "name": "translation",
        "description": "Translate text to target language",
    }
]

app = FastAPI(
    title="Translation API",
    version="1.01",
    openapi_tags=tags_metadata

)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startupEvent():
    global infer
    print('---start startupEvent---')
    infer = inferenceManager()
    infer.start_up()
    print('---end startupEvent---')

@app.get("/")
def read_root():
    return RedirectResponse("/docs")

def response_generator(status,message):
    


    
    return Response(content = f'{{"message": "{message}"}}', status_code=status, media_type="application/json")
@app.get("/translate/",tags=["translation"])
async def single_line_transcription(text: List[str] = Query(None),lang: str = 'en'):


    status, res = infer.translate_sentences(text,lang)


    return response_generator(status,res)

    





	
if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=7795, timeout_keep_alive=20, reload=True)