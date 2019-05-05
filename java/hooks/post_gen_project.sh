#!/bin/sh

ORIG="`cat src/main/java/App.java`"

echo | gradle init --project-name . --type java-application --dsl kotlin --test-framework junit

# sed -i -e 's/rootProject.*//' settings.gradle.kts
sed -i -e '/rootProject/d' settings.gradle.kts

echo "$ORIG" > src/main/java/App.java
sed -i -e '/    /d' src/test/java/AppTest.java
