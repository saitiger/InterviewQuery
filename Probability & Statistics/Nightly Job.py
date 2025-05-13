import numpy as np
import matplotlib.pyplot as plt

def simulate_job_overlaps_seconds(days=365, trials=1000000):
    """
    Simulate the random job scheduling scenario using seconds for a given number of days.
    
    Parameters:
    - days: Number of days to simulate
    - trials: Number of simulation trials to run for better estimate
    
    Returns:
    - Average annual cost across all trials
    """
    # 5 hours = 5 * 60 * 60 = 18000 seconds
    time_window = 5 * 60 * 60
    # Each job lasts 1 hour = 3600 seconds
    job_duration = 60 * 60
    
    # Generate random start times for both jobs (in seconds)
    job1_start = np.random.randint(0, time_window, size=trials)
    job2_start = np.random.randint(0, time_window, size=trials)
    
    # Check for overlap: Jobs overlap if their start times are within 1 hour of each other
    overlap = np.abs(job1_start - job2_start) < job_duration
    
    # Calculate overlap probability
    overlap_probability = np.mean(overlap)
    
    # Calculate annual cost
    annual_cost = overlap_probability * days * 1000
    
    return {
        "overlap_probability": overlap_probability,
        "annual_cost": annual_cost,
        "sample_data": (job1_start[:1000], job2_start[:1000], overlap[:1000])  # For visualization
    }

# Run the simulation
results = simulate_job_overlaps_seconds(trials=10000000)

print(f"Overlap probability: {results['overlap_probability']:.6f}")
print(f"Annual cost: ${results['annual_cost']:.2f}")

# Theoretical calculation
def theoretical_calculation():
    """
    Calculate the expected overlap probability for continuous time.
    
    For a 5-hour window with 1-hour jobs, the theoretical probability is:
    P(overlap) = 1 - P(no overlap) = 1 - (4/5)*(4/5) = 1 - 16/25 = 9/25 = 0.36
    
    Alternative calculation:
    The probability density for |t₁-t₂| < 1 in a 5-hour window is 9/25.
    """
    probability = 9/25  # = 0.36
    annual_cost = probability * 365 * 1000
    
    return {
        "probability": probability,
        "annual_cost": annual_cost
    }

theory = theoretical_calculation()
print(f"\nTheoretical probability: {theory['probability']:.6f}")
print(f"Theoretical annual cost: ${theory['annual_cost']:.2f}")

# Create a visualization to help understand the overlap
def create_visualization(job1_starts, job2_starts, overlaps):
    plt.figure(figsize=(10, 6))
    
    # Convert seconds to hours for better readability
    job1_hours = job1_starts / 3600
    job2_hours = job2_starts / 3600
    
    # Plot all points
    plt.scatter(job1_hours, job2_hours, alpha=0.1, color='blue', label='No overlap')
    
    # Highlight overlap points
    overlap_j1 = job1_hours[overlaps]
    overlap_j2 = job2_hours[overlaps]
    plt.scatter(overlap_j1, overlap_j2, alpha=0.3, color='red', label='Overlap')
    
    # Add diagonal line for reference
    plt.plot([0, 5], [0, 5], 'g--', alpha=0.5)
    
    # Add lines showing the overlap region (|t₁-t₂| < 1)
    plt.plot([0, 4], [1, 5], 'k-', alpha=0.5)
    plt.plot([1, 5], [0, 4], 'k-', alpha=0.5)
    
    # Fill the overlap region
    x = np.array([0, 4, 5, 5, 1, 0])
    y = np.array([1, 5, 5, 4, 0, 0])
    plt.fill(x, y, alpha=0.1, color='red')
    
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    plt.xlabel('Job 1 Start Time (hours after 7 PM)')
    plt.ylabel('Job 2 Start Time (hours after 7 PM)')
    plt.title('Job Overlap Visualization')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Calculate and show the area ratio
    overlap_area = 9  # square hours
    total_area = 25  # square hours
    plt.text(3.5, 0.5, f'Overlap area: {overlap_area}/{total_area} = {overlap_area/total_area:.2f}', 
             bbox=dict(facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

# Uncomment the following line to generate the visualization
# job1_sample, job2_sample, overlap_sample = results['sample_data']
# create_visualization(job1_sample, job2_sample, overlap_sample)
