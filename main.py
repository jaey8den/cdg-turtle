import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse

import turtle
import math
from mods import clean_string, patterns
from wand.image import Image

class Instructions(BaseModel):
    instructions: str

app = FastAPI()

origins = [
    "http://localhost:8000",
    "https://your-production-domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/instructions")
async def process_instructions(instructions: Instructions):

    # Initialize the turtle graphics
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)
    pen = turtle.Turtle()
    pen.up()
    pen.hideturtle()
    pen.speed(10)

    # Initialize variables
    pi = math.pi
    layerWidth = 100
    mrRadius = 0.2 * layerWidth

    # Clean and process the input string
    res = clean_string.CleanString(instructions)

    # Determine the reps in each layer
    reps = []
    for i in range(len(res)):
        reps.append(len(res[i]))

    # Draw MR and remove it from list
    if res[0][0] == "MR":       
        res[0].pop(0)
        reps[0] -= 1
        patterns.MR(pen, layerWidth)

    # Draw main pattern
    for j in range(len(res)):
        for i, p in enumerate(res[j]):
            pen.up()        
            pen.goto((layerWidth * (j + 1) + mrRadius) * math.cos(((2 * pi * i))/reps[j]), (layerWidth * (j + 1) + mrRadius) * math.sin(((2 * pi * i))/reps[j]))
            pen.setheading(pen.towards(0,0))
            # Multiple chains
            if len(p.split(" ")) > 1:
                temp = p.split(" ")
                patterns.pattern[temp[1]](pen, int(temp[0]), layerWidth)
            # Single chain
            elif p == "CH":
                patterns.pattern[p](pen, 1, layerWidth)
            # Slip stitch
            elif p == "SLST":
                patterns.pattern[p](pen, layerWidth)
            # Everything else
            else:
                patterns.pattern[p](pen, layerWidth, reps[j], j + 1)
    
    # Extract canvas as eps file
    screen.getcanvas().postscript(file="venv/diagrams/output.eps")

    # Convert diagram to PNG
    with Image(filename="venv/diagrams/output.eps") as img:
        img.format = "jpeg"
        img.save(filename="venv/diagrams/output.jpg")

@app.get("/get_diagram")
async def get_diagram():
    return FileResponse(f"venv/diagrams/output.jpg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)