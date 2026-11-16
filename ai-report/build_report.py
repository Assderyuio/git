# Runner: executes p1..p6 in one shared namespace (p1 creates the canvas).
ns = {"__name__": "__main__"}
for part in ["build_report_p1.py", "build_report_p2.py", "build_report_p3.py", "build_report_p4.py", "build_report_p5.py", "build_report_p6.py"]:
    src = open("/home/user/git/ai-report/" + part, encoding="utf-8").read()
    code = compile(src, part, "exec")
    exec(code, ns)
