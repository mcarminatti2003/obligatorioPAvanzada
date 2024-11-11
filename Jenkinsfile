pipeline {
    agent any

    environment {
        // Directorios de los módulos
        TRIVIA_DIR = 'TRIVIA'
        PEDIDOS_DIR = 'PEDIDOS'
        USQL_DIR = 'USQL'
    }

    stages {
        stage('Clonar Repositorio') {
            steps {
                echo 'Clonando repositorio principal...'
                git url: 'https://github.com/joaco0o0/obligatorioPAvanzada.git', branch: 'main'
            }
        }

        stage('Construir Trivia') {
            steps {
                dir("${TRIVIA_DIR}") {
                    echo 'Construyendo módulo Trivia...'
                    sh 'mvn clean install -DskipTests'
                }
            }
        }

        stage('Construir Pedidos') {
            steps {
                dir("${PEDIDOS_DIR}") {
                    echo 'Construyendo módulo Pedidos...'
                    sh 'mvn clean install -DskipTests'
                }
            }
        }

        stage('Construir USQL') {
            steps {
                dir("${USQL_DIR}") {
                    echo 'Construyendo módulo USQL...'
                    sh 'mvn clean install -DskipTests'
                }
            }
        }
    }

    post {
        always {
            echo 'Enviando notificación...'
            slackSend channel: '#pipeline', color: 'good', message: 'Pipeline ejecutado correctamente.'
        }
    }
}
