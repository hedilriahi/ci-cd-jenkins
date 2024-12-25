pipeline {
    agent any
    tools {
        dockerTool "docker"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hedilriahi/ci-cd-jenkins.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("hedilriahi/flask-app:latest")
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s . -p "tests/test_*.py"'
            }
        }
    }
}
