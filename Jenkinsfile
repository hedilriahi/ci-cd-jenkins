pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hedilriahi/ci-cd-jenkins.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh "virtualenv venv && . venv/bin/activate && pip install -r requirements.txt"
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
