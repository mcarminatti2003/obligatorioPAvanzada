pipeline {
    agent any

    environment {
        TRIVIA_DIR = 'TRIVIA'
        PEDIDOS_DIR = 'PEDIDOS'
        USQL_DIR = 'USQL'
    }

    stages {
        stage('Git Config') {
            steps {
                script {
                    try {
                        bat 'git config --global core.autocrlf true'
                        bat 'git config --global --list'
                    } catch (Exception e) {
                        echo "Warning: Git configuration failed: ${e.getMessage()}"
                        // Continue pipeline execution even if Git config fails
                    }
                }
            }
        }

        stage('Compilar') {
            steps {
                script {
                    try {
                        echo 'Compilando...'
                        bat './gradlew clean build'
                    } catch (Exception e) {
                        error "Error en compilación: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Construir Trivia') {
            steps {
                script {
                    try {
                        dir("${TRIVIA_DIR}") {
                            echo 'Construyendo módulo Trivia...'
                            bat './gradlew clean build -x test'
                        }
                    } catch (Exception e) {
                        error "Error en construcción de Trivia: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Construir Pedidos') {
            steps {
                script {
                    try {
                        dir("${PEDIDOS_DIR}") {
                            echo 'Construyendo módulo Pedidos...'
                            bat './gradlew clean build -x test'
                        }
                    } catch (Exception e) {
                        error "Error en construcción de Pedidos: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Construir USQL') {
            steps {
                script {
                    try {
                        dir("${USQL_DIR}") {
                            echo 'Construyendo módulo USQL...'
                            bat './gradlew clean build -x test'
                        }
                    } catch (Exception e) {
                        error "Error en construcción de USQL: ${e.getMessage()}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Limpiando workspace...'
            cleanWs()
        }
        success {
            echo 'Pipeline ejecutado exitosamente'
        }
        failure {
            echo 'Pipeline falló'
        }
    }
    //time to push
}