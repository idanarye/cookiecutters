#!/bin/sh

gradle init

cat >> build.gradle <<EOF

apply plugin: 'java'
apply plugin:'application'
apply plugin:'eclipse'
mainClassName = "App"

task printClasspath << {
    println configurations.runtime.asPath
}

repositories {
    mavenCentral()
}

dependencies {
    compile 'org.projectlombok:lombok:1.18.2'
}
EOF
