import subprocess
import sys

def install_requirements():
    print("Installing required packages from requirements.txt...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print("❌ Error installing packages.")
        print(str(e))

if __name__ == "__main__":
    install_requirements()
