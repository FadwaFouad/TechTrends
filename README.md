## Background

TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

The web application is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database to store the submitted articles. 

Below you can examine the main components of the firsts prototype of the application:
![image](https://user-images.githubusercontent.com/24944117/148274846-8b5d2736-4489-45e1-8937-5938c0abee48.png)


# TechTreds Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.

## Run 

To run this application there are 2 steps required:

1. Initialize the database by using the `python init_db.py` command. This will create or overwrite the `database.db` file that is used by the web application.
2.  Run the TechTrends application by using the `python app.py` command. The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.

## Project Steps 

1. develop the status and health check endpoints for the TechTrends application.
2. Package the TechTrends application by creating a Dockefile and Docker image.
3. Implement the Continuous Integration practices, by using GitHub Actions to automate the build and push of the Docker image to DockerHub.
4. Construct the Kubernetes declarative manifests to deploy TechTrends to a sandbox namespace within a Kubernetes cluster.
The cluster should be provisioned using k3s in a vagrant box.

5.Template the Kubernetes manifests using a Helm chart and provide the input configuration files for staging and production environments.

6.Implement the Continuous Delivery practices, by deploying the TechTrends application to staging and production environments using ArgoCD and the Helm chart.
    

# Application deploy using ArgoCD and Helm chart
![argocd-techtrends-prod](https://user-images.githubusercontent.com/24944117/148275629-73bc97b1-79c0-4ae4-a183-8dfa9445a1b3.png)

    
    
