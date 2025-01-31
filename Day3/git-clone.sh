#!/bin/bash
# Author: Prashanth
# Purpose: Clone a Git repository, build using Maven, and deploy the WAR file to Tomcat
# Usage: ./git-clone.sh

# Define repository and target directories
REPO_LINK="git@github.com:vilasvarghese/docker-k8s.git"  # Replace with the actual Git repository link
TARGET_DIR="C:/Users/Administrator/ShellScripting/Day3/Repository1"  # Replace with the desired directory
TOMCAT_HOME="C:\apache-tomcat-10.1.34"  # Set path to your Tomcat installation
JAVA_HOME="C:\Program Files\Java\jdk-11.0.15.1"
CATALINA_BAT="C:\apache-tomcat-10.1.34\bin"

# Check if JAVA_HOME is set
if [ -z "$JAVA_HOME" ]; then
  echo "ERROR: JAVA_HOME is not set. Please configure Java before running this script."
  exit 1
fi

# Check if Maven is installed
if ! command -v mvn &> /dev/null; then
  echo "ERROR: Maven is not installed or not in PATH. Please install Maven."
  exit 1
fi

# Check if Tomcat is installed
if [ ! -d "$TOMCAT_HOME" ]; then
  echo "ERROR: Tomcat directory not found at $TOMCAT_HOME. Exiting..."
  exit 1
fi

# Clone or pull the latest changes from the repository
echo "Checking for existing repository..."
if [ -d "$TARGET_DIR/.git" ]; then
  echo "Repository exists. Pulling latest changes..."
  cd "$TARGET_DIR" || { echo "ERROR: Failed to enter $TARGET_DIR"; exit 1; }
  git pull origin main
else
  echo "Cloning repository..."
  git clone "$REPO_LINK" "$TARGET_DIR"
  cd "$TARGET_DIR" || { echo "ERROR: Failed to enter $TARGET_DIR"; exit 1; }
fi

# Ensure the project has a pom.xml file
if [ ! -f "pom.xml" ]; then
  echo "ERROR: No pom.xml found in $TARGET_DIR. Ensure you have cloned a valid Maven project."
  exit 1
fi

# Build the project using Maven
echo "Running Maven clean package..."
mvn clean package -DskipTests

# Check if the WAR file was created
WAR_FILE=$(find target -name "*.war" | head -n 1)
if [ -z "$WAR_FILE" ]; then
  echo "ERROR: No WAR file found in target directory. Build failed."
  exit 1
fi

# Wait for Tomcat to stop completely
sleep 5

# Copy the WAR file to the Tomcat webapps directory
echo "Deploying WAR file to Tomcat..."
cp "$WAR_FILE" "$TOMCAT_HOME/webapps/"

# Start the Tomcat server
# echo "Starting Tomcat server..."
# "$CATALINA_BAT\catalina.bat start"

cd "$CATALINA_BAT"
./catalina.bat start

# Notify the user
echo "Deployment completed successfully. Application is now running on Tomcat."
