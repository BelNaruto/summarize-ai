FROM python:3.9

RUN pip install gunicorn

COPY . app/

# Exclude files and directories listed in .dockerignore
COPY .dockerignore /app/.dockerignore
RUN cat .dockerignore | xargs rm -rf

WORKDIR /app

RUN pip install -r requirements.txt

# Install uvicorn
RUN pip install uvicorn

# Install TensorFlow 2.0 # or specific version if required
RUN pip install tensorflow~=2.10.0

# Install PyTorch # or specific version if required
RUN pip install torch torchvision  


# Make port 8080 available to the world outside this container
ENV PORT 8080

#CMD uvicorn main:app --port=8000 --host=0.0.0.0
#CMD ["exec", "gunicorn", "--bind", ":$PORT", "main:app"]
CMD ["python", "main.py"]