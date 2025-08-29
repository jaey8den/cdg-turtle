# Crochet Diagram Generator (Discontinued)

The purpose of this project was to receive text input from the user and translate it into its corresponding diagram.

## Method

The method used for drawing the diagram was turtle, python's built in library. Turtle requires a digital canvas for it to 'draw' on, which can then be saved as an eps file and later converted to jpeg.

## Why is it discontinued

The cloud server I was using to deploy the API is "headless", meaning it does not have GUI. Without the GUI, turtle is unable to generate a canvas and thus the program fails from there. There was a method which involves generating a virtual display, but it only worked in a linux environment. I attempted to run it in WSL but was met with permission and connections errors. Without being able to test it locally, I did not want to risk deploying to the cloud server and have it not work. It was then I decided that it was prohibitively difficult to continue with turtle and started looking for another way.

## What I've learnt

Not all is wasted. This was my first project where I designed an API and actually deployed to a cloud server for use over the internet. I had to call the API from within WordPress (WP) and figured out how to use the plugin to specify endpoints and parameter types. I had to encode the image to base64 and decode it on WP to display the generated image as WP only takes JSON or PHP, which I believe is the standard? All in all it was still a good experience.

## What's next

I have started looking for another method to complete this project and will update here when I do.

### 2025-09-28

Update: I have completed the project using konva, you can find it [here](https://github.com/jaey8den/cdg-konva).
