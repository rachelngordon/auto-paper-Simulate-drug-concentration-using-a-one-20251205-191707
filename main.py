# ==== main.py ====
import numpy as np
import matplotlib.pyplot as plt

def concentration(t, dose, Vd, kel):
    '''One-compartment IV bolus concentration.'''
    return (dose / Vd) * np.exp(-kel * t)

def run_exp1():
    dose = 100.0  # mg
    Vd = 10.0     # L
    kel = 0.15    # h^-1
    t = np.linspace(0, 24, 241)  # every 0.1 h
    C = concentration(t, dose, Vd, kel)
    plt.figure()
    plt.plot(t, C, label=f'kel={kel:.2f} h$^{{-1}}$')
    plt.xlabel('Time (h)')
    plt.ylabel('Concentration (mg/L)')
    plt.title('IV Bolus Concentration-Time Profile')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('iv_bolus_conc_vs_time.png')
    plt.close()

def run_exp2():
    dose = 100.0
    Vd = 10.0
    kels = [0.05, 0.15, 0.30]
    t = np.linspace(0, 24, 241)
    plt.figure()
    for kel in kels:
        C = concentration(t, dose, Vd, kel)
        plt.plot(t, C, label=f'kel={kel:.2f}')
    plt.xlabel('Time (h)')
    plt.ylabel('Concentration (mg/L)')
    plt.title('Effect of Elimination Rate Constant')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('kel_sweep_conc_vs_time.png')
    plt.close()

def main():
    run_exp1()
    run_exp2()
    # Primary numeric answer: initial concentration after bolus (C0)
    dose = 100.0
    Vd = 10.0
    C0 = dose / Vd
    print('Answer:', C0)

if __name__ == '__main__':
    main()

