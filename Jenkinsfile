pipeline {
    agent any 
    environment { 
        GIT_CRED = credentials('Vamsi')
        DOCKER = credentials('DOCKER')
    }
    stages {
        stage('git clone') {
            steps {
              sh 'env'
              sh 'docker --version'
              git branch: 'main', url: 'https://github.com/vamsi434/my-ml-project.git'
            }
        }
        stage('docker build') {
            steps {
              sh 'docker build -t ${DOCKER_USR}/model:latest .'
            }
        }
        stage('docker push') {
            steps {
              sh 'docker login --username ${DOCKER_USR} --password ${DOCKER_PSW}'
              sh 'docker push ${DOCKER_USR}/model:latest'
            }
        }
        stage('docker container creation') {
            steps {
              sh 'docker rm -f python'
              sh 'docker run -p 8081:80 --name python ${DOCKER_USR}/model:latest'
              
            }
        }
    }
}
