pipeline {
    agent { node { label ''; customWorkspace '/workspace/devsecops-lab' } }
    options { skipDefaultCheckout(true); disableConcurrentBuilds() }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git rev-parse HEAD'
            }
        }
        stage('Verify Docker') {
            steps { sh 'docker version' }
        }
    }
}
