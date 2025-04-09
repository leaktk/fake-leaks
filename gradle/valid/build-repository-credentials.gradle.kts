//https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:supported_transport_protocols
repositories {
    maven {
        url = uri("sftp://repo.mycompany.com:22/maven2")
        credentials {
            username = "AlgorithmLegend99"
            password = "A6p!qR1@7Xv#9WtZk4F!xL"
        }
    }
}
