import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from simulation.experiment import Simulation


def run_production_batches():
    # Define batches
    suite = [{"name": f"Batch_{i}"} for i in range(1, 11)]

    events_per_batch = 100000 # 100k particles per batch

    print(f"[*] Starting Validation Suite: {len(suite)} batches.")
    
    for config_override in suite:
        batch_name = config_override["name"]
        print(f"\n{'='*20} RUNNING: {batch_name} {'='*20}")
        
        sim = Simulation()
        # Load baseline
        sim.load_config()
        
        # Explicitly enforce 26 GeV and Iridium target
        sim.beam.energy_mean = "26 GeV"
        sim.environment.target_material = "G4_Ir"
        
        # Apply batch particle count
        sim.beam.count = events_per_batch
        
        # Ensure a unique name to prevent overwriting
        original_id_func = sim.get_run_identifier
        sim.get_run_identifier = lambda orig=original_id_func, name=batch_name: f"{name}_{orig()}"
        
        # Execute
        sim.run(interactive=False)
        
        print(f"{'='*20} {batch_name} COMPLETE {'='*20}")
        time.sleep(2)


if __name__ == "__main__":
    run_production_batches()
