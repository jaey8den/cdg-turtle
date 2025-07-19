import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

import turtle
import math
from mods import clean_string, patterns
from wand.image import Image
import base64
import os

# Define the JSON passed into the post request
class Instructions(BaseModel):
    instructions: str

app = FastAPI()

# Limit which domain can access the api
origins = [
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
async def process_instructions(instr_obj: Instructions):

    # Initialize the turtle graphics
    try:
        screen = turtle.Screen()
        screen.setup(width=1000, height=1000)
        screen.tracer()
        pen = turtle.Turtle()
        pen.up()
        pen.hideturtle()
        pen.speed(0)
    except Exception as e:
        return f"init turtle graphics error: {e}"

    # Initialize variables
    pi = math.pi
    layerWidth = 100
    mrRadius = 0.2 * layerWidth

    # Clean and process the input string
    try:
        res = clean_string.CleanString(instr_obj.instructions)
    except:
        return f"clean string error: {e}"

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
    try:
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
    
        # Ensure all drawing is finished
        screen.update()

    except:
        return f"main pattern error: {e}"
    
    # Extract canvas as eps file
    epsPath = "diagrams/output.eps"
    screen.getcanvas().postscript(file=epsPath)

    try:
        # Convert diagram to JPG
        with Image(filename="diagrams/output.eps") as img:
            img.format = "jpeg"
            img.save(filename="diagrams/output.jpg")

        # Clean up temp eps file
        os.remove(epsPath)

        # Clean up turtle resources
        turtle.clearscreen()
        turtle.bye()

    except:
        return f"extracting and conversion error: {e}"

@app.get("/get_diagram")
async def get_diagram():
    image_path = "diagrams/output.jpg"
    
    if not os.path.exists(image_path):
        return JSONResponse(content={"error": "Image not found."}, status_code = 404)
    
    try:
        # Opens image in read binary mode
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return JSONResponse(content={"image_data": encoded_string})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)