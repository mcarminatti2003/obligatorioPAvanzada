pipeline {
    agent any

    environment {
        // Directorios de los módulos
        TRIVIA_DIR = 'CarminattiHeredero'
        PEDIDOS_DIR = 'EN2PA-main'
        USQL_DIR = 'Entregable3'
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

        stage('Ejecutar Tests') {
            steps {
                echo 'Ejecutando pruebas unitarias para todos los módulos...'
                sh 'mvn test'
            }
        }

        stage('Análisis de Código') {
            steps {
                echo 'Ejecutando análisis de código estático...'
                sh 'mvn sonar:sonar'
            }
        }

        stage('Empaquetar Aplicación') {
            steps {
                echo 'Empaquetando la aplicación completa...'
                sh 'mvn package'
            }
        }
    }

    post {
        always {
            echo 'Enviando notificación por correo electrónico...'
            emailext(
                subject: "Resultado del Pipeline: ${currentBuild.fullDisplayName}",
                body: """<p>El pipeline ha finalizado con el estado: ${currentBuild.currentResult}</p>
                         <p>Revisa los detalles en: <a href="${env.BUILD_URL}">Jenkins Build</a></p>""",
                to: 'tu-email@example.com'
            )
        }
    }
}
