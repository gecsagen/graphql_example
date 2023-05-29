from fastapi import FastAPI
from strawberry.asgi import GraphQL
import uvicorn
from schema import schema

app = FastAPI()
app.add_route("/graphql", GraphQL(schema))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
