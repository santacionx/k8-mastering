Certainly! Here’s a consolidated list of Kubernetes commands to manage your resources and verify data persistence. These commands will help you with various tasks related to port forwarding, stopping services, and checking data.

### **Port Forwarding Commands**

- **Start Port Forwarding:**
  ```bash
  kubectl port-forward <pod-name> <local-port>:<container-port>
  ```

  Example:
  ```bash
  kubectl port-forward flask-deployment-56dd5c5d75-2cr5p 5000:5000
  ```

- **Stop Port Forwarding:**
  - Simply press `Ctrl+C` in the terminal where the port forwarding command is running.

### **Service and Deployment Commands**

- **List All Pods:**
  ```bash
  kubectl get pods
  ```

- **Describe a Service:**
  ```bash
  kubectl describe svc <service-name>
  ```

  Example:
  ```bash
  kubectl describe svc flask-service
  ```

- **Delete a Deployment:**
  ```bash
  kubectl delete -f k8s/deployment.yaml
  ```

- **Delete a Service:**
  ```bash
  kubectl delete -f k8s/service.yaml
  ```

- **Delete a Persistent Volume Claim (PVC):**
  ```bash
  kubectl delete -f k8s/persistent-volume-claim.yaml
  ```

- **Delete a Persistent Volume (PV):**
  ```bash
  kubectl delete pv <persistent-volume-name>
  ```

- **Delete a Storage Class:**
  ```bash
  kubectl delete -f k8s/storage-class.yaml
  ```

### **Verification and Troubleshooting Commands**

- **Check Logs of a Pod:**
  ```bash
  kubectl logs <pod-name>
  ```

- **Execute a Command Inside a Pod:**
  ```bash
  kubectl exec -it <pod-name> -- <command>
  ```

  Example (to list files):
  ```bash
  kubectl exec -it flask-deployment-56dd5c5d75-2cr5p -- ls /data/uploads
  ```

- **Get the Status of Persistent Volume Claims (PVCs):**
  ```bash
  kubectl get pvc
  ```

- **Get the Status of Persistent Volumes (PVs):**
  ```bash
  kubectl get pv
  ```

- **Get the Status of Services:**
  ```bash
  kubectl get svc
  ```

- **Get the Status of Deployments:**
  ```bash
  kubectl get deployments
  ```

### **Example Workflow**

1. **Start Port Forwarding:**
   ```bash
   kubectl port-forward flask-deployment-56dd5c5d75-2cr5p 5000:5000
   ```

2. **Delete the Deployment and Service:**
   ```bash
   kubectl delete -f k8s/deployment.yaml
   kubectl delete -f k8s/service.yaml
   ```

3. **Verify Data Persistence:**

   - **Reapply Deployment and Service:**
     ```bash
     kubectl apply -f k8s/deployment.yaml
     kubectl apply -f k8s/service.yaml
     ```

   - **List Files in the PVC Directory:**
     ```bash
     kubectl exec -it flask-deployment-<pod-id> -- ls /data/uploads
     ```

This set of commands will help you manage and troubleshoot your Kubernetes setup, including port forwarding, service management, and verifying data persistence. If you have more specific needs or run into issues, let me know!


### **Project Overview**

This project is a Flask web application deployed on a Kubernetes cluster with persistent storage. The main features and components of the project are:

### **1. Flask Application**

**Functionality:**
- **File Upload:** Users can upload files via a web interface.
- **File Viewing:** Users can view a list of uploaded files.
- **File Download:** Users can download any uploaded file.

**Implementation Details:**
- **`app.py`:** This is the main Flask application script. It includes routes to handle file uploads, list files, and download files.
- **Templates:** HTML files (`index.html` and `files.html`) are used for rendering the web pages for file upload and file listing.

### **2. Kubernetes Deployment**

**Functionality:**
- **Deployment:** The Flask application is containerized using Docker and deployed on Kubernetes. The deployment ensures that the Flask application runs in a containerized environment, which can be managed and scaled as needed.
- **Service:** A Kubernetes Service is used to expose the Flask application, making it accessible from outside the Kubernetes cluster.

**Implementation Details:**
- **`deployment.yaml`:** Defines the Kubernetes Deployment configuration. It specifies how many replicas of the Flask application should run, the container image to use, and the ports to expose.
- **`service.yaml`:** Defines the Kubernetes Service configuration. It maps an external port to the port used by the Flask application inside the container, allowing external access to the application.

### **3. Persistent Storage**

**Functionality:**
- **Storage:** Uploaded files are stored in a Kubernetes Persistent Volume (PV). This ensures that the files persist across container restarts and pod recreations.
  
**Implementation Details:**
- **`storage-class.yaml`:** Defines the Storage Class for dynamic provisioning of storage.
- **`persistent-volume-claim.yaml`:** Defines the Persistent Volume Claim (PVC) used by the Flask application to request storage resources.
- **`persistent-volume.yaml` (if applicable):** Defines the Persistent Volume itself, though it might be dynamically created based on the Storage Class.

### **4. Docker Container**

**Functionality:**
- **Containerization:** The Flask application is containerized using Docker, which allows it to run in an isolated environment with all its dependencies.

**Implementation Details:**
- **`Dockerfile`:** Defines the instructions to build the Docker image for the Flask application. It sets up the base image, installs dependencies, and specifies the command to run the Flask app.

### **5. Project Workflow**

1. **Containerize the Application:**
   - Build a Docker image for the Flask app.
   - Push the Docker image to a container registry (if necessary).

2. **Deploy on Kubernetes:**
   - Apply Kubernetes configurations to create the deployment, service, and persistent storage.
   - Kubernetes handles the orchestration, scaling, and management of the containerized Flask application.

3. **Access the Application:**
   - Use the Kubernetes Service to expose the application.
   - Port forward to access the application locally, or use the service's external IP or NodePort for external access.

4. **Data Persistence:**
   - Uploaded files are saved in the Persistent Volume.
   - Data remains available even if the application or pod is restarted, due to the persistent nature of the volume.

### **Summary**

The project sets up a Flask web application with file upload and management features, containerized with Docker and deployed on Kubernetes. It ensures that user-uploaded files are stored persistently using Kubernetes Persistent Volumes, allowing the application to handle file uploads and downloads reliably across restarts and scaling events.