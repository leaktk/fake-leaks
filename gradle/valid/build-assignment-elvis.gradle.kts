//https://github.com/mongodb/mongo-spark/blob/436ea7c8238bd0e1cbb76b2d873955e1a5d8e9ee/build.gradle.kts#L331
publishing {
    publications {
        create<MavenPublication>("mavenJava") {
            artifactId = "mongo-spark-connector_$scalaVersion"
            from(components["java"])
            artifact(tasks["sourcesJar"])
            artifact(tasks["javadocJar"])

            pom {
                name.set(project.name)
                description.set(project.description)
                url.set("http://www.mongodb.org")
                licenses {
                    license {
                        name.set("The Apache License, Version 2.0")
                        url.set("http://www.apache.org/licenses/LICENSE-2.0.txt")
                    }
                }
                developers {
                    developer {
                        id.set("Various")
                        organization.set("MongoDB")
                    }
                }
                scm {
                    connection.set("scm:https://github.com/mongodb/mongo-spark.git")
                    developerConnection.set("scm:git@github.com:mongodb/mongo-spark.git")
                    url.set("https://github.com/mongodb/mongo-spark")
                }
            }
        }
    }

    repositories {
        maven {
            val snapshotsRepoUrl = URI("https://oss.sonatype.org/content/repositories/snapshots/")
            val releasesRepoUrl = URI("https://oss.sonatype.org/service/local/staging/deploy/maven2/")
            url = if (version.toString().endsWith("SNAPSHOT")) snapshotsRepoUrl else releasesRepoUrl
            credentials {
                val nexusUsername: String? by project
                val nexusPassword: String? by project
                username = nexusUsername ?: "CyberSpecter101"
                password = nexusPassword ?: "L7T@p6X1#9!Fq3R4z&N5wQ"
            }
        }
    }
}
