pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                dir('backend'){
                    script{
                        try {
                            sh 'docker stop testdjango'
                            sh 'docker rm testdjango'
                            sh 'docker rmi remudjango'
                            sh 'docker build -t remudjango .'
                        }catch(e){
                            mattermostSend color: '#439FE0', icon: "https://jenkins.io/images/logos/jenkins/jenkins.png", message: "Back 빌드 실패: ${env.JOB_NAME} ${env.BUILD_NUMBER} ${e}"
                        }
                    }
                }
                dir('backend/ReMu'){
                    sh 'docker run -d -p 8000:8000 --name testdjango remudjango:latest'
                    sh 'docker logs testdjango'
                }
                mattermostSend color: '#439FE0', icon: "https://jenkins.io/images/logos/jenkins/jenkins.png", message: "빌드 성공: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
            }
        }
    }  
}
