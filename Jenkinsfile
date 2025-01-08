pipeline {
    agent any

    environment {
        VENV_DIR = ".venv" // Директория виртуального окружения
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo "Creating virtual environment..."
                    sh 'python3 -m venv $VENV_DIR'
                    echo "Installing dependencies..."
                    sh '$VENV_DIR/bin/pip install --upgrade pip'
                    sh '$VENV_DIR/bin/pip install -r requirements.txt'
                    echo "Installed packages:"
                    sh '$VENV_DIR/bin/pip list'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    try {
                        sh '$VENV_DIR/bin/python -m pytest --maxfail=5 --disable-warnings'
                    } catch (Exception e) {
                        echo "Test execution failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping the pipeline due to test failure.")
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh 'docker-compose build'
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                script {
                    echo "Starting Docker containers..."
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up resources..."
            sh 'docker-compose down || true' // Останавливает контейнеры после выполнения
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs for more details."
        }
    }
}
