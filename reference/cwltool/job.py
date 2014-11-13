import subprocess
import os
import tempfile

class Job(object):
    def remap_files():
        pass

    def run(self):
        outdir = tempfile.mkdtemp()

        runtime = []

        if self.container and self.container.get("type") == "docker":
            runtime = ["docker", "run", "-i"]
            for d in self.pathmapper.dirs:
                runtime.append("--volume=%s:%s:ro" % (d, self.pathmapper.dirs[d]))
            runtime.append("--volume=%s:%s:ro" % (outdir, "/tmp/job_output"))
            runtime.append("--workdir=%s" % ("/tmp/job_output"))
            runtime.append("--user=%s" % (os.geteuid()))
            runtime.append(self.container["imageId"])
        else:
            os.chdir(outdir)

        stdin = None
        stdout = None

        if self.stdin:
            stdin = open(self.stdin, "rb")

        if self.stdout:
            stdout = open(os.path.join(outdir, self.stdout), "wb")

        print runtime + self.command_line

        sp = subprocess.Popen(runtime + self.command_line, shell=False, stdin=stdin, stdout=stdout)
        sp.wait()

        if stdin:
            stdin.close()

        if stdout:
            stdout.close()

        print "Output directory is %s" % outdir
