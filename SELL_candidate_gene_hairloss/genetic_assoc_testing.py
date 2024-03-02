#!usr/bin/env python

#Author = Chiranan Khantham

import subprocess

def assoc(input_file, pheno_file, pheno_name=None):
    """ A standard case/control association analysis
    --assoc writes the results of a 1df chi-square allelic test
    """
    
    full_command = ["./plink", "--allow-no-sex", 
                    "--file", input_file, 
                    "--pheno", pheno_file, 
                    "--pheno-name", pheno_name, 
                    "--ci", "0.95",
                    "--assoc", 
                    "--out", f'{pheno_name}Control_ASSSOC'
                   ]
    try:
        subprocess.run(full_command, check=True, capture_output=True)
        print("PLINK command for chi-square allelic test has been executed successfully.")
        return True
    
    except subprocess.CalledProcessError as e:
        print("Error executing PLINK command:", e)
        return False

def model(input_file, pheno_file, pheno_name=None):
    """a standard case/control association analysis using Fisher's exact test
    --model performs four other tests as well 
    (1df dominant gene action, 1df recessive gene action, 2df genotypic, and Cochran-Armitage trend)
    """
    full_command = ["./plink", "--allow-no-sex", 
                    "--file", input_file, 
                    "--pheno", pheno_file, 
                    "--pheno-name", pheno_name, 
                    "--model",
                    "--fisher", 
                    "--out", f'{pheno_name}Control_MODEL'
                   ]
    try:
        subprocess.run(full_command, check=True, capture_output=True)
        print("PLINK command for association analysis using Fisher's exact test has been executed successfully.")
        return True
    
    except subprocess.CalledProcessError as e:
        print("Error executing PLINK command:", e)
        return False


def additive_logistic(input_file, pheno_file, covar_file, pheno_name=None):
    """Allelic model: D versus d (D is the minor allele and d is the major allele)"""
    
    full_command = ["./plink", "--allow-no-sex", 
                    "--file", input_file, 
                    "--pheno", pheno_file, 
                    "--pheno-name", pheno_name, 
                    "--logistic", 
                    "--covar", covar_file,
                    "--hide-covar",
                    "--ci", "0.95",
                    "--adjust", 
                    "--out", f'{pheno_name}Control_AGE_ADDITIVE'
                   ]
    try:
        subprocess.run(full_command, check=True, capture_output=True)
        print("PLINK command for logistic regression, assuming additive model, has been executed successfully.")
        return True
    
    except subprocess.CalledProcessError as e:
        print("Error executing PLINK command:", e)
        return False

def dominant_logistic(input_file, pheno_file, covar_file, pheno_name=None):
    """Dominant: (DD, Dd) versus dd"""
    
    full_command = ["./plink", "--allow-no-sex", 
                    "--file", input_file, 
                    "--pheno", pheno_file, 
                    "--pheno-name", pheno_name, 
                    "--logistic", 
                    "--covar", covar_file,
                    "--hide-covar",
                    "--ci", "0.95",
                    "--dominant",
                    "--adjust", 
                    "--out", f'{pheno_name}Control_AGE_DOMINANT'
                   ]
    try:
        subprocess.run(full_command, check=True, capture_output=True)
        print("PLINK command for logistic regression, assuming dominant model, has been executed successfully.")
        return True
    
    except subprocess.CalledProcessError as e:
        print("Error executing PLINK command:", e)
        return False


def recessive_logistic(input_file, pheno_file, covar_file, pheno_name=None):
    """Recessive model: DD versus (Dd, dd)"""
    
    full_command = ["./plink", "--allow-no-sex", 
                    "--file", input_file, 
                    "--pheno", pheno_file, 
                    "--pheno-name", pheno_name, 
                    "--logistic", 
                    "--covar", covar_file,
                    "--hide-covar",
                    "--ci", "0.95",
                    "--recessive",
                    "--adjust", 
                    "--out", f'{pheno_name}control_AGE_RECESSIVE'
                   ]
    try:
        subprocess.run(full_command, check=True, capture_output=True)
        print("PLINK command for logistic regression, assuming recessive model, has been executed successfully.")
        return True
    
    except subprocess.CalledProcessError as e:
        print("Error executing PLINK command:", e)
        return False

def genotypic_logistic(input_file, pheno_file, covar_file, pheno_name=None):
    """The genotypic test provides a general test of association in the 2-by-3 table of disease-by-genotype.
    Genotypic model:DD versus Dd versus dd"""
    
    full_command = ["./plink", "--allow-no-sex", 
                    "--file", input_file, 
                    "--pheno", pheno_file, 
                    "--pheno-name", pheno_name, 
                    "--logistic", 
                    "--covar", covar_file,
                    "--hide-covar",
                    "--genotypic",
                    "--adjust", 
                    "--out", f'{pheno_name}control_AGE_GENOTYPIC'
                   ]
    try:
        subprocess.run(full_command, check=True, capture_output=True)
        print("PLINK command for logistic regression, assuming genotypic model, has been executed successfully.")
        return True
    
    except subprocess.CalledProcessError as e:
        print("Error executing PLINK command:", e)
        return False

def main(input_file, pheno_file, covar_file, pheno_name=None):
    assoc(input_file, pheno_file, pheno_name)
    model(input_file, pheno_file, pheno_name)
    additive_logistic(input_file, pheno_file, covar_file, pheno_name)
    dominant_logistic(input_file, pheno_file, covar_file, pheno_name)
    recessive_logistic(input_file, pheno_file, covar_file, pheno_name)
    genotypic_logistic(input_file, pheno_file, covar_file, pheno_name)