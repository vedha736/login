 I’ll guide you like a step-by-step lab manual so you can literally follow and complete everything (GitHub → VS Code → Docker → Jenkins → Kubernetes). No confusion, just do along 


---

 PART 1 — Create Resume Web Page (HTML)

 Step 1: Create Project Structure

Create this folder structure:

resume-app/
 ├── index.html
 ├── style.css


---

 Step 2: HTML Code (index.html)

<!DOCTYPE html>
<html>
<head>
    <title>My Resume</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
    <h1>Your Name</h1>
    <p>Email: your@email.com</p>
    <p>Phone: 1234567890</p>

    <h2>Objective</h2>
    <p>To build a successful career in software development.</p>

    <h2>Education</h2>
    <ul>
        <li>B.Tech / B.Sc / Degree - Your College</li>
    </ul>

    <h2>Skills</h2>
    <ul>
        <li>Java</li>
        <li>Python</li>
        <li>Web Development</li>
    </ul>

    <h2>Projects</h2>
    <ul>
        <li>Resume Website</li>
    </ul>
</div>

</body>
</html>


---

 Step 3: CSS (style.css)

body {
    font-family: Arial;
    background-color: #f4f4f4;
}

.container {
    width: 60%;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
}


---

 PART 2 — GitHub Setup

 Step 4: Create Repository

Go to GitHub → New Repo
Name: resume-app


---

 Step 5: Initialize Git Locally

Open VS Code terminal:

cd resume-app
git init
git add .
git commit -m "Initial resume webpage"


---

 Step 6: Connect to GitHub

git remote add origin https://github.com/YOUR_USERNAME/resume-app.git
git branch -M main
git push -u origin main


---

 PART 3 — Clone + Modify

 Step 7: Clone Repo

git clone https://github.com/YOUR_USERNAME/resume-app.git
cd resume-app
code .


---

 Step 8: Modify Code

Edit anything → save

git add .
git commit -m "Updated resume"
git push


---

 PART 4 — Dockerize Application

 Step 9: Create Dockerfile

Create file: Dockerfile

FROM nginx:alpine
COPY . /usr/share/nginx/html


---

 Step 10: Build Docker Image

docker build -t resume-app .


---

 Step 11: Run Container

docker run -d -p 8080:80 resume-app

 Open browser:
http://localhost:8080


---

 PART 5 — Kubernetes Deployment

 Step 12: Create deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: resume-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: resume
  template:
    metadata:
      labels:
        app: resume
    spec:
      containers:
      - name: resume-container
        image: resume-app
        ports:
        - containerPort: 80


---

 Step 13: Create Service

apiVersion: v1
kind: Service
metadata:
  name: resume-service
spec:
  type: NodePort
  selector:
    app: resume
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007


---

 Step 14: Apply Kubernetes

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml


---

 PART 6 — Jenkins Pipeline

 Step 15: Install Jenkins Plugins

Go to Jenkins → Manage Plugins:

Install:

Git Plugin

Docker Pipeline

Kubernetes Plugin



---

 Step 16: Create Pipeline Project

Jenkins → New Item → Pipeline


---

 Step 17: Pipeline Script

pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/YOUR_USERNAME/resume-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t resume-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8081:80 resume-app'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}


---

 PART 7 — Docker Desktop Visualization

 Step 18: View Deployment

Open Docker Desktop → Containers

You will see:

Running containers

Kubernetes pods



---

 FINAL OUTPUT

You now have:

 Resume website
 GitHub repo
 Docker container
 Kubernetes deployment
 Jenkins CI/CD pipeline


---

 Pro Tip (Important for Viva)

If they ask:

 Why Docker?
→ For containerization & portability

 Why Jenkins?
→ Automation (CI/CD)

 Why Kubernetes?
→ Scaling & orchestration


---

If you want, I can also:  Give diagram for this (for record)
 Give viva questions + answers
 Help debug if anything fails

Just tell me 
[4/2, 2:09 PM] Tamilarasi Mis Vit: Got you  — I’ll give you exact step-by-step with commands + code only (no confusion) so you can literally follow and complete your lab.


---

 STEP 1: Create Maven Project (Standard Structure)

 Option A (FAST – using command line)

mvn archetype:generate -DgroupId=com.example.app \
-DartifactId=my-app \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DinteractiveMode=false

 Folder structure (auto-created)

my-app/
 ├── pom.xml
 └── src/
     ├── main/java/com/example/app/App.java
     └── test/java/com/example/app/AppTest.java


---

 STEP 2: Initialize Git & Push to GitHub

cd my-app

git init
git add .
git commit -m "Initial Maven project"

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/my-app.git
git push -u origin main


---

 STEP 3: Clone into VS Code

git clone https://github.com/YOUR_USERNAME/my-app.git
cd my-app
code .


---

 STEP 4: Modify Program (Sample Java Code)

 src/main/java/com/example/app/App.java

package com.example.app;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello Jenkins CI/CD ");
    }
}


---

 STEP 5: Update pom.xml

<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example.app</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <!-- JUnit -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

</project>


---

 STEP 6: Build Project in VS Code

mvn clean install

 Output should end with:

BUILD SUCCESS


---

 STEP 7: Commit Changes

git add .
git commit -m "Updated Java program"
git push origin main


---

 STEP 8: Jenkins Setup (Pipeline Project)

 Install Plugins

Git Plugin

Pipeline Plugin

Maven Integration Plugin



---

 Create New Job

1. Open Jenkins


2. Click New Item


3. Name: my-app-pipeline


4. Select: Pipeline




---

 STEP 9: Pipeline Script (IMPORTANT )

 Paste this in Jenkins Pipeline Script

pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'JDK'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/my-app.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Package') {
            steps {
                sh 'mvn package'
            }
        }

    }

    post {
        success {
            echo 'Build Successful '
        }
        failure {
            echo 'Build Failed '
        }
    }
}


---

 STEP 10: Configure Tools in Jenkins

Go to:  Manage Jenkins → Global Tool Configuration

Add:

JDK → name: JDK

Maven → name: Maven



---

 STEP 11: Run Pipeline

1. Click Build Now


2. Check Console Output




---

 FINAL FLOW (EXAM POINTS )

1. Create Maven project


2. Push to GitHub


3. Clone in VS Code


4. Modify code


5. Build using Maven


6. Commit changes


7. Create Jenkins Pipeline


8. Write pipeline script


9. Run CI/CD




---

If you want, I can also give:  Viva answers
 Diagram for CI/CD flow
 OR make this into record-ready lab writeup (AIM, Procedure, Result)
