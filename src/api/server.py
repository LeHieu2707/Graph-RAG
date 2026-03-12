from fastapi import FastAPI

app = FastAPI()

@app.get("/query")

def query(q: str):

    answer = graph_rag_pipeline(q)

    return {"answer": answer}