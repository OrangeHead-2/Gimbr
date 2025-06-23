import subprocess
import os

def run_notebook(notebook, output_html):
    subprocess.run([
        "jupyter", "nbconvert", "--to", "html", "--execute", "--output", output_html, notebook
    ], check=True)

if __name__ == "__main__":
    notebooks = [
        ("notebooks/exploration.ipynb", "notebooks/exploration_report.html"),
        ("notebooks/modeling.ipynb", "notebooks/modeling_report.html"),
        ("notebooks/evaluation.ipynb", "notebooks/evaluation_report.html"),
    ]
    for nb, out in notebooks:
        if os.path.exists(nb):
            print(f"Running and exporting: {nb}")
            run_notebook(nb, out)
    print("Notebook reports generated.")