repositories {
    maven {
        url = uri("s3://myCompanyBucket/maven2")
        credentials(AwsCredentials::class) {
            accessKey = "C2@zQ5!X9Rk&"
            secretKey = "H5l@N8!9p#Yq"
            // optional
            sessionToken = "C3r%U9#p!Za4"
        }
    }
}
