import sublime
import sublime_plugin
import subprocess
import json
import re
import urllib.parse
import urllib.request

class SemgrepCheckerListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        file_path = view.file_name()
        if file_path and "/test/" in file_path:
            self.run_semgrep(view)


    def run_semgrep(self, view):
        file_path = view.file_name()
        command = ['semgrep', '--json', '-f', '/home/l0xm1/Documents/BCA/major_project/SemSub/semgrep_rules.yml', file_path]
        try:
            output = subprocess.check_output(command)
            findings = json.loads(output.decode('utf-8'))
            self.display_findings(view, findings)
        except subprocess.CalledProcessError as e:
            print(f"Error running Semgrep: {e.output}")

    def display_findings(self, view, findings):
        vulnerabilities_found = False
        for finding in findings.get("results", []):
            severity = finding.get("extra", {}).get("severity", "Unknown")
            if severity == 'WARNING':
                vulnerabilities_found = True
                message = finding.get("extra", {}).get("message", "Unknown message")
                vuln_function = finding.get("extra", {}).get("metadata", {}).get("vulnerable_function")
                safe_function = finding.get("extra", {}).get("metadata", {}).get("safe_function")
                if vuln_function and safe_function:
                    self.replace_function(view, vuln_function, safe_function)
                    sublime.message_dialog(f"Vulnerability found and replaced: {message}")
                else:
                    sublime.message_dialog(f"Vulnerability found: {message}")
                self.report_vulnerability(view.file_name(), finding)

    def replace_function(self, view, vuln_function, safe_function):
        file_region = sublime.Region(0, view.size())
        file_contents = view.substr(file_region)
        updated_contents = re.sub(r'\b{}\b'.format(re.escape(vuln_function)), safe_function, file_contents)
        if updated_contents != file_contents:
            view.run_command("replace_vulnerable_function", {"updated_contents": updated_contents})
            sublime.message_dialog(f"Vulnerable function '{vuln_function}' replaced with safe function '{safe_function}'.")

    def report_vulnerability(self, file_path, finding):
        data = {
            "file_path": file_path,
            "message": finding.get("extra", {}).get("message", "Unknown message"),
            "line": finding.get("start", {}).get("line", "Unknown line"),
            "severity": finding.get("extra", {}).get("metadata", {}).get("severity"),
            "references": finding.get("extra", {}).get("metadata", {}).get("references")


        }
        try:
            url = 'http://127.0.0.1:5000/report'
            data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req) as response:
                pass
        except Exception as e:
            print(f"Failed to report vulnerability: {e}")

class ReplaceVulnerableFunctionCommand(sublime_plugin.TextCommand):
    def run(self, edit, updated_contents):
        file_region = sublime.Region(0, self.view.size())
        self.view.replace(edit, file_region, updated_contents)
        self.view.run_command('save')
