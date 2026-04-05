# FastAPI RESTful Backend Service

A robust backend web application built with **Python** and **FastAPI**, focused on demonstrating modern **RESTful API** design and **DevOps** integration. This project serves as a practical implementation of containerized services deployment workflows.

## Project Objective
The goal of this project is to provide a scalable backend service that handles structured data via standard HTTP methods.

* **RESTful Architecture:** Supports `GET`, `POST`, `PUT`, and `DELETE` requests.
* **Data Exchange:** Returns structured **JSON** responses for seamless frontend integration.
* **Learning Focus:** Designed to bridge the gap between backend development and DevOps practices.

## Development & Testing Workflow
Code is written using **Python** and **FastAPI**. Initial testing is performed locally using:

### 1. Containerization
To ensure "it works on my machine" translates to the cloud, we use **Docker**:
* Build a **Docker image** containing the application and its dependencies.
* Run and test the API within the container to verify environment consistency.

### 2. Collaboration
We follow a structured **Git workflow**:
* **Feature Branching:** New features are developed on separate branches.
* **Pull Requests:** Code is reviewed and validated before merging into the main branch.
* **GitHub:** Serves as our central repository and cloud deployment trigger.

### 3. Automated Testing
We focus on code-based testing to verify:
* Correct **HTTP Status Codes** (e.g., `200 OK`, `201 Created`, `404 Not Found`).


### Before run the project
1. delete blog.db 
2. create your .env file
   * create your secret key: SECRET_KEY=your secret key


Test github actions