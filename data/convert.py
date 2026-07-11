from pathlib import Path

import numpy as np
import uproot

DATA_DIR = Path(__file__).resolve().parent
RUNS_DIR = DATA_DIR / "runs"


def _branch_to_numpy(branch):
    arr = branch.array(library="ak")
    if "var *" in str(arr.type):
        return [np.asarray(value) for value in arr]
    return np.asarray(arr)


def root_to_numpy(filepath, tree_name):
    """Convert all branches in a ROOT tree to numpy arrays."""
    data = {}
    with uproot.open(filepath) as file:
        if tree_name not in file:
            raise KeyError(f"'{tree_name}' tree not found in {filepath}")

        tree = file[tree_name]
        for key in tree.keys():
            data[key] = _branch_to_numpy(tree[key])

    return data


def convert_validation(filepath):
    """Convert validation.root (Validation tree) to numpy arrays."""
    return root_to_numpy(filepath, "Validation")


def convert_simulation(filepath):
    """Convert simulation.root (Seeds tree) to numpy arrays."""
    return root_to_numpy(filepath, "Seeds")


def convert_run(run_dir):
    """Convert both ROOT files in a run folder to numpy arrays."""
    run_dir = Path(run_dir)
    return {
        "validation": convert_validation(run_dir / "validation.root"),
        "simulation": convert_simulation(run_dir / "simulation.root"),
    }


def _to_npz_value(value):
    if isinstance(value, list):
        return np.array(value, dtype=object)
    return value


def save_npz(data, output_path):
    """Save a branch dictionary to a compressed .npz file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(output_path, **{key: _to_npz_value(value) for key, value in data.items()})


def load_npz(filepath):
    """Load numpy arrays saved by save_npz."""
    with np.load(filepath, allow_pickle=True) as archive:
        return {key: archive[key] for key in archive.files}


def save_run_arrays(run_dir, output_dir=None):
    """Convert a run's ROOT files and save them as .npz arrays."""
    run_dir = Path(run_dir)
    arrays = convert_run(run_dir)
    output_dir = Path(output_dir) if output_dir else run_dir

    validation_path = output_dir / "validation.npz"
    simulation_path = output_dir / "simulation.npz"

    save_npz(arrays["validation"], validation_path)
    save_npz(arrays["simulation"], simulation_path)

    return {
        "validation": validation_path,
        "simulation": simulation_path,
    }


def get_latest_run():
    """Return the most recently modified run folder in data/runs/."""
    if not RUNS_DIR.exists():
        raise FileNotFoundError(f"Runs directory not found: {RUNS_DIR}")

    runs = [path for path in RUNS_DIR.iterdir() if path.is_dir() and path.name.startswith("run_")]
    if not runs:
        raise FileNotFoundError(f"No run folders found in {RUNS_DIR}")

    return max(runs, key=lambda path: path.stat().st_mtime)


def convert_latest_run(save=False):
    """Convert the latest run's ROOT files to numpy arrays."""
    run_dir = get_latest_run()
    arrays = convert_run(run_dir)

    if save:
        paths = save_run_arrays(run_dir)
        return run_dir, arrays, paths

    return run_dir, arrays


def describe_branch(name, value):
    if isinstance(value, list):
        lengths = [len(item) for item in value[:5]]
        return f"{name}: jagged list ({len(value)} events, sample lengths {lengths})"
    return f"{name}: array shape {value.shape}, dtype {value.dtype}"


if __name__ == "__main__":
    run_dir, arrays, paths = convert_latest_run(save=True)

    print(f"Converted run: {run_dir}")
    print(f"Saved validation arrays to: {paths['validation']}")
    print(f"Saved simulation arrays to: {paths['simulation']}")

    print("\nvalidation.root")
    for key, value in arrays["validation"].items():
        print(f"  {describe_branch(key, value)}")

    print("\nsimulation.root")
    for key, value in arrays["simulation"].items():
        print(f"  {describe_branch(key, value)}")
