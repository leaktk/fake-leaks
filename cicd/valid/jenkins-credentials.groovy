// Metadata: label=Jenkins API tokens, type=cicd_token, platform=jenkins, context=Jenkins Groovy script, generator=secret_generator.py

import jenkins.model.*
import com.cloudbees.plugins.credentials.*

// Jenkins API token (username:token format)
def JENKINS_USER = 'admin'
def JENKINS_API_TOKEN = '3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c'

// Alternative tokens
def JENKINS_TOKENS = [
    user1: '7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f',
    user2: '1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e',
    service: '5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c'
]

// Triggering a build via API
def triggerBuild() {
    def jenkins = Jenkins.getInstance()
    def authString = "${JENKINS_USER}:${JENKINS_API_TOKEN}".bytes.encodeBase64().toString()

    // Jenkins crumb for CSRF protection
    def crumb = '9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f'

    return [auth: authString, crumb: crumb]
}

// Legacy API token format
def LEGACY_TOKEN = '11234567890abcdef1234567890abcdef'
