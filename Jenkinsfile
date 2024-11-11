pipeline {
    agent any

    environment {
        TRIVIA_DIR = 'TRIVIA'
        PEDIDOS_DIR = 'PEDIDOS'
        USQL_DIR = 'USQL'
    }

    stages {

        stage('Construir Trivia') {
            steps {
                dir("${TRIVIA_DIR}") {
                    echo 'Construyendo módulo Trivia...'
                    bat 'mvn clean install -DskipTests'
                }
            }
        }

        stage('Construir Pedidos') {
            steps {
                dir("${PEDIDOS_DIR}") {
                    echo 'Construyendo módulo Pedidos...'
                    bat 'mvn clean install -DskipTests'
                }
            }
        }

        stage('Construir USQL') {
            steps {
                dir("${USQL_DIR}") {
                    echo 'Construyendo módulo USQL...'
                    bat 'mvn clean install -DskipTests'
                }
            }
        }
    }

    post {
        always {
            echo 'Enviando notificación...'
            emailext(
                subject: "Pipeline Finalizado",
                body: "El pipeline ha finalizado con éxito.",
                to: 'jheredero@correo.um.edu.uy'
            )
        }
    }
}
