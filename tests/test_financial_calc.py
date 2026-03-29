import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from finsaarthi.tools.financial_calc import calculate_sip_for_goal, compare_tax_regimes

def test_sip_calculation():
    # Goal: 1Cr, 20 years, 12% returns
    sip = calculate_sip_for_goal(10000000, 20, 0.12)
    print(f"Monthly SIP for 1Cr in 20yrs at 12%: {sip}")
    assert sip > 0

def test_tax_comparison():
    # Salary 15L (FY 2025-26)
    # New Regime: Taxable = 15L - 75k = 14.25L
    # Tax = 20k (4-8) + 40k (8-12) + 33.75k (12-14.25) = 93.75k
    # Total with 4% Cess = 97.5k
    result = compare_tax_regimes(1500000, 150000, 50000, 50000, 25000)
    print(f"Tax Comparison (FY 2025-26): {result}")
    assert 'old' in result
    assert result['new'] == 97500.0

if __name__ == "__main__":
    test_sip_calculation()
    test_tax_comparison()
    print("All tests passed!")
