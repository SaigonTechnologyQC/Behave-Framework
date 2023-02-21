pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                // Select testing environment
                sh 'export env=qa'
                // Set client_id
                sh 'export client_id='
                // Set client_secret
                sh 'export client_secret='
            }
        }
        stage('Test Execution') {
            steps {
                // Generate Allure report after executing smoke test
                sh 'python3 -m behave --tags=Smoke-testing -f allure_behave.formatter:AllureFormatter -o reports'
            }
        }
    }
}