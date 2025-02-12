echo "Give me the Project Path"
read -r Path

if [ -d "$Path" ]; then
    cd "$Path" || { echo "Failed to change directory"; exit 1; }
    echo "Path has been changed"
    
    echo "Enter the Environment name: "
    read -r Env
    
    if [ -d "$Path/$Env" ]; then
        echo "Starting the Virtual Environment: $Env"
        source "$Path/$Env/bin/activate" || { echo "Failed to activate virtual environment"; exit 1; }
        echo "Activated Virtual Environment"
    else
        echo "Creating a Virtual Environment: $Env"
        python -m venv "$Env"
        
        if [ -d "$Path/$Env" ]; then
            source "$Path/$Env/bin/activate" || { echo "Failed to activate virtual environment"; exit 1; }
            echo "Activated Virtual Environment"
        else
            echo "Error: Virtual environment creation failed"
            exit 1
        fi
    fi
    
    if [ -f "$Path/requirements.txt" ]; then
        pip install -r "$Path/requirements.txt" || { echo "Failed to install requirements"; exit 1; }
        echo "Requirements installed successfully"
    else
        echo "requirements.txt file not found"
    fi
    
    if [ -f "$Path/app.py" ]; then
        echo "Launching Application"
        python "$Path/app.py"
    else
        echo "Error: app.py not found"
    fi
else
    echo "Error: Path does not exist"
    exit 1
fi
