pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {

                    sh 'python3 -m venv .venv'
                    sh '.venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {

                    sh '.venv/bin/python -m pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {

                    sh 'docker-compose build'
                }
            }
        }
        stage('Docker Compose Up') {
            steps {
                script {

                    sh 'docker-compose up -d'
                }
            }
        }
    }
}
