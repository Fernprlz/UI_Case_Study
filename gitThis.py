import subprocess

subprocess.run(["del", "prepros-6.config"], shell=True)
subprocess.run(["del", "README.html"], shell=True)
subprocess.run(["git", "add", "."], shell=True)

print("Commit message:")
cm = input();

subprocess.run(["git", "commit", "-m", cm], shell=True)
subprocess.run(["git", "push"], shell=True)
