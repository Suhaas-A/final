import subprocess


def main():
    # Run Streamlit app
    process = subprocess.Popen(['streamlit', 'run', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for Streamlit app to start
    process.stdout.readline()

    # Wait for the Streamlit app to finish
    process.wait()


if __name__ == "__main__":
    main()
