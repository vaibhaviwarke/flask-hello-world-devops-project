pipeline {
    agent any
    
    environment {
        // DOCKER_HUB_REPO = "shivammitra/flask-hello-world"
        CONTAINER_NAME = "flask-hello-world"
        // DOCKERHUB_CREDENTIALS=credentials('dockerhub-credentials')
    }
    
    stages {
        /* We do not need a stage for checkout here since it is done by default when using "Pipeline script from SCM" option. */
        
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'docker image build -t $CONTAINER_NAME:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
                sh 'docker run -p 5000:5000 --name $CONTAINER_NAME $CONTAINER_NAME /bin/bash -c "pytest test.py && flake8"'
            }
        }
        // stage('Push') {
        //     steps {
        //         echo 'Pushing image..'
        //         sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        //         sh 'docker push $DOCKER_HUB_REPO:latest'
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //         sh 'minikube kubectl -- apply -f deployment.yaml'
        //         sh 'minikube kubectl -- apply -f service.yaml'
        //     }
        // }
    }
}
