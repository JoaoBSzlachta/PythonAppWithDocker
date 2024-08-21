# PythonAppWithDocker

# Python Flask App with Docker

This project demonstrates how to containerize a Python Flask application using Docker. The Flask application generates a simple graph using Matplotlib and serves it on a web page.

## Project Overview

This repository contains a Python Flask application that:

- Creates a simple x/y graph using Matplotlib.
- Displays the graph on a web page.

The application is containerized using Docker and can be deployed on an AWS Virtual Machine (VM).

## Building and Running

```bash
sudo docker build -t graficoapp .
```

```bash
sudo docker run -p 5000:5000 graficoapp
```
- note: "graficoapp" is the directory where the files are saved

## Reference ##
This project is a work for a DevOps class in my Computer Science course.

## Contact
joao.szlachta@edu.unifil.br
