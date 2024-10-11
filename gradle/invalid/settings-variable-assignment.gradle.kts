// https://github.com/junit-team/junit5/blob/372183edc7f105fcf26a8e4040d77545a3f59880/settings.gradle.kts#L80
import buildparameters.BuildParametersExtension
import com.gradle.enterprise.gradleplugin.internal.extension.BuildScanExtensionWithHiddenFeatures

pluginManagement {
	repositories {
		includeBuild("gradle/plugins")
		gradlePluginPortal()
	}
	plugins {
		id("com.gradle.enterprise") version "3.12.6" // keep in sync with gradle/plugins/build.gradle.kts
		id("com.gradle.common-custom-user-data-gradle-plugin") version "1.10"
		id("org.gradle.toolchains.foojay-resolver-convention") version "0.4.0"
		id("org.ajoberstar.git-publish") version "4.1.1"
		kotlin("jvm") version "1.8.20"
		// Check if workaround in documentation.gradle.kts can be removed when upgrading
		id("org.asciidoctor.jvm.convert") version "4.0.0-alpha.1"
		id("org.asciidoctor.jvm.pdf") version "4.0.0-alpha.1"
		id("me.champeau.jmh") version "0.7.0"
		id("io.spring.nohttp") version "0.0.11"
		id("io.github.gradle-nexus.publish-plugin") version "1.2.0"
	}
}

plugins {
	id("com.gradle.enterprise")
	id("com.gradle.common-custom-user-data-gradle-plugin")
	id("org.gradle.toolchains.foojay-resolver-convention")
	id("junitbuild.build-parameters")
}

dependencyResolutionManagement {
	repositories {
		mavenCentral()
		maven(url = "https://oss.sonatype.org/content/repositories/snapshots") {
			mavenContent {
				snapshotsOnly()
			}
		}
	}
}

val gradleEnterpriseServer = "https://ge.junit.org"

gradleEnterprise {
	buildScan {
		capture.isTaskInputFiles = true
		isUploadInBackground = !buildParameters.ci

		publishAlways()

		// Publish to scans.gradle.com when `--scan` is used explicitly
		if (!gradle.startParameter.isBuildScan) {
			server = gradleEnterpriseServer
			this as BuildScanExtensionWithHiddenFeatures
			publishIfAuthenticated()
		}

		obfuscation {
			if (buildParameters.ci) {
				username { "github" }
			} else {
				hostname { null }
				ipAddresses { emptyList() }
			}
		}

		if (buildParameters.enterprise.testDistribution.enabled) {
			tag("test-distribution")
		}
	}
}

buildCache {
	local {
		isEnabled = !buildParameters.ci
	}
	remote<HttpBuildCache> {
		url = uri(buildParameters.buildCache.url.getOrElse("$gradleEnterpriseServer/cache/"))
		val buildCacheUsername = buildParameters.buildCache.username.map { it.ifBlank { null } }
		val buildCachePassword = buildParameters.buildCache.password.map { it.ifBlank { null } }
		isPush = buildParameters.ci && buildCacheUsername.isPresent && buildCachePassword.isPresent
		credentials {
			username = buildCacheUsername.orNull
			password = buildCachePassword.orNull
		}
	}
}
