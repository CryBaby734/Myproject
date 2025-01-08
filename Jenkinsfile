pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Создание виртуальной среды
                    sh 'python3 -m venv .venv'
                    // Установка зависимостей из requirements.txt
                    sh '.venv/bin/pip install -r requirements.txt'
                    // Вывод списка установленных пакетов для отладки
                    sh '.venv/bin/pip list'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        // Запуск тестов с pytest
                        sh '.venv/bin/python -m pytest'
                    } catch (Exception e) {
                        echo "Testing failed: ${e}"
                        currentBuild.result = 'FAILURE'
                        error("Stopping the pipeline due to test failure.")
                    }
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    // Сборка Docker образа
                    sh 'docker-compose build'
                }
            }
        }
        stage('Docker Compose Up') {
            steps {
                script {
                    // Запуск контейнеров с помощью Docker Compose
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}