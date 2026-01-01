import typer
app = typer.Typer()

@app.command()
def install(name: str):
    print(f"Installing {name} (mock)")

@app.command()
def run(workflow: str):
    print(f"Running workflow {workflow}")

if __name__ == "__main__":
    app()
