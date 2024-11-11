pipeline {
    agent any

    environment {
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
    }

    stage('Compilar') {
        steps {
            echo 'Compilando...'
            sh 'mvn clean package'
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
