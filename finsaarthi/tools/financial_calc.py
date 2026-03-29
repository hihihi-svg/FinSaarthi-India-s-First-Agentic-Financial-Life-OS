import numpy_financial as npf
import numpy as np
from datetime import datetime

def calculate_xirr(cashflows: list, dates: list) -> float:
    """Calculate Extended IRR for irregular SIP cashflows"""
    # Placeholder: In a real implementation, you'd use scipy.optimize.newton
    # for root-finding. For now, we'll return a placeholder value.
    # TODO: Implement actual Newton-Raphson for XIRR
    return 0.15 # 15% placeholder

def calculate_sip_for_goal(goal_amount, years, rate, current_savings=0):
    """Monthly SIP needed to reach goal at given return rate"""
    months = years * 12
    monthly_rate = rate / 12
    if monthly_rate == 0:
        return round((goal_amount - current_savings) / months, 2)
    
    future_current = current_savings * (1 + monthly_rate)**months
    remaining = goal_amount - future_current
    sip = npf.pmt(monthly_rate, months, 0, -remaining)
    return round(sip, 2)

def calculate_old_regime(gross_salary, deductions_80c, hra, nps, medical):
    """Simplified 2024-25 Old Tax Regime calculation"""
    taxable = gross_salary - deductions_80c - hra - nps - medical - 50000 # Standard Deduction
    if taxable <= 0: return 0
    # Simplified slabs
    tax = 0
    if taxable > 1500000: tax += (taxable - 1500000) * 0.3 + 275000
    elif taxable > 1200000: tax += (taxable - 1200000) * 0.2 + 115000
    elif taxable > 1000000: tax += (taxable - 1000000) * 0.2 + 75000
    elif taxable > 500000: tax += (taxable - 500000) * 0.2 + 12500
    elif taxable > 250000: tax += (taxable - 250000) * 0.05
    return tax * 1.04 # Health & Education Cess

def calculate_new_regime(gross_salary):
    """2025-26 New Tax Regime (Budget 2025) calculation"""
    standard_deduction = 75000
    taxable = gross_salary - standard_deduction
    
    if taxable <= 1200000: return 0 # Rebate u/s 87A up to 12L
    
    tax = 0
    # Slabs for FY 2025-26
    if taxable > 2400000:
        tax += (taxable - 2400000) * 0.3 + 300000 # (4*0.05 + 4*0.1 + 4*0.15 + 4*0.2 + 4*0.25)
    elif taxable > 2000000:
        tax += (taxable - 2000000) * 0.25 + 200000
    elif taxable > 1600000:
        tax += (taxable - 1600000) * 0.2 + 120000
    elif taxable > 1200000:
        tax += (taxable - 1200000) * 0.15 + 60000
    elif taxable > 800000:
        tax += (taxable - 800000) * 0.1 + 20000
    elif taxable > 400000:
        tax += (taxable - 400000) * 0.05
        
    return tax * 1.04 # 4% Cess

def compare_tax_regimes(gross_salary, deductions_80c, hra, nps, medical):
    """Compare old vs new tax regime and return savings"""
    old_tax = calculate_old_regime(gross_salary, deductions_80c, hra, nps, medical)
    new_tax = calculate_new_regime(gross_salary)
    return {'old': old_tax, 'new': new_tax, 'savings': abs(old_tax - new_tax)}
