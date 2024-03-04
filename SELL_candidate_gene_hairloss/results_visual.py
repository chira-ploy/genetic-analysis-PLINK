#!usr/bin/env python

#Author = Chiranan Khantham

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def merge_result(model):

    # Get list of all files in the directory
    files = os.listdir('./')

    left_df = pd.DataFrame()
    right_df = pd.DataFrame()

    # Iterate over the files and read them into DataFrames
    for file in files:
        if file.startswith('MALES_2') and f'{model}.assoc' in file:
            df = pd.read_csv(file, delimiter='\s+')
            if file.endswith('.assoc.logistic'):
                left_df = pd.concat([left_df, df], ignore_index=True)
            elif file.endswith('.assoc.logistic.adjusted'):
                right_df = pd.concat([right_df, df], ignore_index=True)

            
    # Merge DataFrames based on specified columns
    merge_df = pd.merge(left_df, right_df, left_on=['CHR', 'SNP', 'P'], right_on=['CHR', 'SNP', 'UNADJ'], how='left')
    return merge_df

def plot_result(merge_df, model):
    plt.figure(figsize=(8,3))
    merge_df['SNP_info'] = merge_df['SNP'].astype(str) + ' ' + merge_df['A1'].astype(str)
    sns.pointplot(data=merge_df, x='OR', y='SNP_info', join=False, color='black')
    plt.errorbar(x=merge_df['OR'], y=merge_df['SNP'].index, xerr=(merge_df['OR'] - merge_df['L95'], 
                                                                  merge_df['U95'] - merge_df['OR']), fmt='o', color='black')
    plt.axvline(x=1, linestyle='dashed', color='gray')
    plt.ylabel(None)
    plt.xlim(right=10)
    plt.xlabel('Odds Ratio')
    
    plt.title(f'{model} MODEL', pad=20)

    # Add p-value labels (adjust y position and ha for alignment)
    for i, row in merge_df.iterrows():
        plt.text(row['OR'], i - 0.1, f"p_adj={row['FDR_BH']:.2f}", ha='center', fontsize=8)
        
    # Adjust layout to prevent overlapping elements
    plt.tight_layout()
        
    # Remove frame (axes)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    plt.gca().set_aspect("auto")
    plt.xlim(left=-2, right=10)
    
    plt.show()
    
def main(model):
    allResult_df = merge_result(model)
    allResult_plot= plot_result(allResult_df, model)
    return allResult_df, allResult_plot