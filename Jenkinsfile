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
                    sh "docker build -t flask-app ."
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
