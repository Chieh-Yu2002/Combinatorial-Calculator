# Combinatorial-Calculator
# Programming Assignment 1 - 109261035 劉倢瑜

### Overview
This project is a Streamlit-based web application that provides various discrete mathematics calculations and visualizations. The app is containerized with Docker for easy setup and execution.

---

## **Project Structure**
```
streamlit_math_app/
├── Dockerfile          # Docker configuration to build the app
├── app.py              # Main Streamlit application
├── formulas.py         # Supporting formulas and utility functions
└── requirements.txt    # Python dependencies
```

---

## **How to Use**

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop) on your machine.

---

### Steps to Run the App

1. **Navigate to the Project Folder**
   Open your terminal and navigate to the folder containing the project:
   ```bash
   cd streamlit_math_app
   ```

2. **Build the Docker Image**
   Build the Docker image using the `Dockerfile`:
   ```bash
   docker build -t streamlit-math-app .
   ```

3. **Run the Docker Container**
   Start the container and map the app to your local machine's port 8501:
   ```bash
   docker run -p 8501:8501 streamlit-math-app
   ```

4. **Access the Application**
   ![CleanShot 2024-12-25 at 22.52.04@2x](https://hackmd.io/_uploads/HyfE29KHyl.png)

   
   Open your browser and navigate to:
   ```
   http://0.0.0.0:8501
   ```

---

### Updating the Application
If the code is updated (`app.py` or `formulas.py`):
1. Stop the current container:
   ```bash
   docker ps
   docker stop <CONTAINER_ID>
   ```
2. Rebuild the Docker image:
   ```bash
   docker build -t streamlit-math-app .
   ```
3. Rerun the container:
   ```bash
   docker run -p 8501:8501 streamlit-math-app
   ```

---

## **Customization**
To modify or extend the app:
1. Edit `app.py` or `formulas.py` locally.
2. Follow the update steps above to see your changes in the app.
