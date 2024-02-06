from typing import Union

from fastapi import FastAPI, File, UploadFile

from .lib import most_common

app = FastAPI()


@app.get("/")
def read_root():
    return {"Staus": "ok"}
    
@app.post('/upload')
def get_file(top_word_count: int, file: bytes = File(...)):
    content = file.decode('utf-8')
    return {"most_common": most_common.mostcommon(content, top_word_count)}
