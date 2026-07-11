from pathlib import Path

try:
    from data.convert import (
        convert_latest_run,
        convert_run,
        convert_simulation,
        convert_validation,
        describe_branch,
        get_latest_run,
        load_npz,
        root_to_numpy,
        save_run_arrays,
    )
except ImportError:
    from convert import (
        convert_latest_run,
        convert_run,
        convert_simulation,
        convert_validation,
        describe_branch,
        get_latest_run,
        load_npz,
        root_to_numpy,
        save_run_arrays,
    )


def load_validation(filepath=None):
    """Load validation.root branches as numpy arrays."""
    if filepath is None:
        filepath = get_latest_run() / "validation.root"
    return convert_validation(filepath)


def load_simulation(filepath=None):
    """Load simulation.root branches as numpy arrays."""
    if filepath is None:
        filepath = get_latest_run() / "simulation.root"
    return convert_simulation(filepath)


def load_latest():
    """Load validation and simulation arrays from the latest run folder."""
    run_dir = get_latest_run()
    validation = load_validation(run_dir / "validation.root")
    simulation = load_simulation(run_dir / "simulation.root")
    return run_dir, validation, simulation


if __name__ == "__main__":
    run_dir, validation, simulation = load_latest()

    print(f"Latest run: {run_dir}")
    print("\nvalidation.root")
    for key, value in validation.items():
        print(f"  {describe_branch(key, value)}")

    print("\nsimulation.root")
    for key, value in simulation.items():
        print(f"  {describe_branch(key, value)}")
