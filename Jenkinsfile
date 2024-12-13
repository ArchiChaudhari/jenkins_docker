pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "python-docker-cont"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out the code"
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building the Docker image"
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run Container') {
            steps {
                echo "Running the Docker container"
                script {
                    sh "docker run -d -p 5000:5000 --name ${DOCKER_IMAGE}-container ${DOCKER_IMAGE}"
                }
            }
        }

       

    }

    post {
        always {
            echo "Pipeline completed"
        }
        success {
            echo "Pipeline succeeded"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
