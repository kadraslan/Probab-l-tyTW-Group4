IE 221 – Probability | Team Work 4
SLLN & CLT Simulations and Monte Carlo π Estimation

This project contains simulations of the Strong Law of Large Numbers (SLLN) and the Central Limit Theorem (CLT). Additionally, a statistical estimation of π is performed using the Monte Carlo method.

Project Structure:
Probab-I-lyTW-Group4/
src/ (Source code)
slln_simulation.py
clt_simulation.py
monte_carlo_pi.py
results/figures/ (Generated plots)
slln_convergence.png
clt_histograms.png
pi_estimation.png
reports/ (Technical report in PDF)
TeamWork4_Report.pdf
README.md (This file)
(other project files)

Installation:
Requirements: Python 3.8+ and pip (Python package manager).
Steps:

Clone the repository: git clone https://github.com/Probab-I-lyTW-Group4/IE221_TeamWork4.git

Navigate to the project folder: cd IE221_TeamWork4

(Optional) Create a virtual environment: python -m venv venv, then activate it with: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)

Install required libraries: pip install -r requirements.txt
Note: If there is no requirements.txt file, you can install the necessary packages manually: pip install numpy matplotlib scipy

Usage:
To run the simulations, execute each script in the src/ folder:

For SLLN simulation: python src/slln_simulation.py

For CLT simulation: python src/clt_simulation.py

For Monte Carlo π estimation: python src/monte_carlo_pi.py

Sample Outputs:
When you run the simulations, the following plots will be generated in the results/figures/ folder:

slln_convergence.png: Shows the convergence of the sample mean to the theoretical mean.

clt_histograms.png: Histograms of standardized sample means for different sample sizes.

pi_estimation.png: Shows the Monte Carlo estimation of π and the error convergence.

Code Documentation:
All functions are documented with docstrings. Please refer to the source code for detailed documentation.

Technical Report:
A detailed technical report is available in the reports/ folder as TeamWork4_Report.pdf. It includes theoretical background, methodology, results, and discussion.

Team Members:

Kadir Aslancı (2111021075)

Yiğithan Aldemir (2311021061)

Zehra Sena Gündoğdu (2211021009)

License:
This project is for academic purposes only.

Contact:
For questions, please contact the team members via their university email addresses.

Note: Make sure to have the required Python packages installed before running the code.
