import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _ensure_venv():
    venv_dir = PROJECT_ROOT / ".venv"
    venv_python = venv_dir / "bin" / "python"
    in_project_venv = Path(sys.prefix).resolve() == venv_dir.resolve()
    if venv_python.exists() and not in_project_venv:
        import subprocess
        raise SystemExit(subprocess.call([str(venv_python), *sys.argv]))


_ensure_venv()

from simulation.experiment import Simulation


def main():
    sim = Simulation()
    is_interactive = sim.load_config()
    sim.run(interactive=is_interactive)


if __name__ == "__main__":
    main()
