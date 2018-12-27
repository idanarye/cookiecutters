#!/bin/sh

gradle init --type kotlin-application --dsl kotlin < /dev/null
rm src/test/kotlin/AppTest.kt
cat > src/main/kotlin/App.kt <<-EOF
fun main(args: Array<String>) {
}
EOF
