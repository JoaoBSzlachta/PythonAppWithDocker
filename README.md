# PythonAppWithDocker

# Python Flask App with Docker

This project demonstrates how to containerize a Python Flask application using Docker. The Flask application generates a simple graph using Matplotlib and serves it on a web page.

## Project Overview

This repository contains a Python Flask application that:

- Creates a simple x/y graph using Matplotlib.
- Displays the graph on a web page.

The application is containerized using Docker and can be deployed on an AWS Virtual Machine (VM).

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (for deployment)

## Building and Running

```bash
sudo docker build -t graficoapp .
```

```bash
sudo docker run -p 5000:5000 graficoapp
```

## Reference ##
This project is a work for a DevOps class in my Computer Science course.

## Contact
joao.szlachta@edu.unifil.br
