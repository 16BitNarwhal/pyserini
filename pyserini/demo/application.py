import subprocess
import sys

def export_nextjs():
    # Export the Next.js app
    frontend_path = "frontend/"
    subprocess.call("npm run build && npm run export", shell=True, cwd=frontend_path)

def start_fastapi():
    # Start the FastAPI app
    subprocess.Popen("uvicorn main:app --reload", shell=True)

if __name__ == "__main__":
    # get args
    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] == "build":
            export_nextjs()
    start_fastapi()