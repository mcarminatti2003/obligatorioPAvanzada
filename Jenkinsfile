pipeline {
    agent any

    environment {
        TRIVIA_DIR = 'TRIVIA'
        PEDIDOS_DIR = 'PEDIDOS'
        USQL_DIR = 'USQL'
    }

    stages {
        stage('Compilar') {
            steps {
                echo 'Compilando...'
                bat './gradlew clean build'
            }
        }

        stage('Construir Trivia') {
            steps {
                dir("${TRIVIA_DIR}") {
                    echo 'Construyendo módulo Trivia...'
                    bat './gradlew clean build -x test'
                }
            }
        }

        stage('Construir Pedidos') {
            steps {
                dir("${PEDIDOS_DIR}") {
                    echo 'Construyendo módulo Pedidos...'
                    bat './gradlew clean build -x test'
                }
            }
        }

        stage('Construir USQL') {
            steps {
                dir("${USQL_DIR}") {
                    echo 'Construyendo módulo USQL...'
                    bat './gradlew clean build -x test'
                }
            }
        }
    }
}