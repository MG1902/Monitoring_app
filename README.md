It's a monitoring app which will tell you the current utilization of CPU and Memory for  your system using python inbuilt Module PSUTIL

Learning:
 
1.Python and How to create Monitoring Application in Python using Flask and psutil

2.How to run a Python App locally.

3.Learn Docker and How to containerize a Python application

  Creating Dockerfile

  Building DockerImage

  Running Docker Container

  Docker Commands

4. How to deploy it as a deployment/pod  on minikube

✨Let’s Start the Project ✨

Part 1: Deploying the Flask application locally

Step 1: Clone the code

Clone the code from the repository:

git clone <repository_url>

Step 2: Install dependencies

The application uses the psutil and Flask, Plotly, boto3 libraries. Install them using pip:

pip3 install -r requirements.txt

Step 3: Run the application

To run the application, navigate to the root directory of the project and execute the following command:

python3 app.py

This will start the Flask server on localhost:5000. Navigate to http://localhost:5000/ on your browser to access the application.

Part 2: Dockerizing the Flask application

Step 1: Create a Dockerfile

Create a Dockerfile in the root directory of the project with the following contents:

# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the environment variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask app when the container is run
CMD ["flask", "run"]
Step 2: Build the Docker image
To build the Docker image, execute the following command:

docker build -t <image_name> .
Step 3: Run the Docker container
To run the Docker container, execute the following command:

docker run -p 5000:5000 <image_name>
This will start the Flask server in a Docker container on localhost:5000. Navigate to http://localhost:5000/ on your browser to access the application.

For pushing it to Docker Hub :

1. You can create a repo on docker  hub and can push  your image with the commmand docker push reponame:tagname

For deploying it you need minikube to be working on your system

Commands that can be used to deploy: create a deployment.yaml file and apply the changes with kubectl apply -f deployment.yaml

For checking  : Kubectl get pods / Kubectl get deployments:

Output:
![image](https://github.com/user-attachments/assets/f88f797f-a807-46e6-9436-46986a9eee69)
