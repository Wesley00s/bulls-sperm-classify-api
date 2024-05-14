from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import warnings

from DataModel import Data
from PredictiveCalculation import calc_classify
from Transactions import add_data

# from RFClassifier import classify

warnings.filterwarnings('ignore')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)


@app.post("/api/bulls")
async def bulls(data: Data):

    print(data)

    d = calc_classify(data)
    add_data(d)

    message = ""
    if d["alvo"] == 0:
        message = "Animal totalmente apto à reprodução."
    elif d["alvo"] == 1:
        message = "Animal apto à reprodução, porém com restrições."
    elif d["alvo"] == 2:
        message = "Animal não apto à reprodução."
    else:
        print("Erro no processamento de dados.")

    return {"class": d["alvo"], "message": message}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
