from fastapi import FastAPI
app = FastAPI(title="ActLang Registry")

@app.get("/health")
def health():
    return {"status": "ok"}
