import subprocess

subprocess.run(["del", "README.html"], shell=True)
subprocess.run(["git", "add", "."], shell=True)

print("Commit message:")
cm = input();

subprocess.run(["git", "commit", "-m", cm], shell=True)
subprocess.run(["git", "push"], shell=True)
subprocess.run(["fernprlz"], shell=True)
subprocess.run(["Vw.67544"], shell=True)