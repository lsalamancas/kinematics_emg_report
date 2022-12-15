selected_run = '03'
runs = ['03', '04', '05']

runs = [run for run in runs if run != selected_run]
print(runs)