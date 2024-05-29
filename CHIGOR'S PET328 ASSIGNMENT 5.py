def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def classify_gridblocks(layers, rows, columns, cut_off):
    active_count = 0
    inactive_count = 0
    total_gridblocks = layers * rows * columns

    for layer in range(layers):
        active_count_layer = 0
        for row in range(rows):
            for column in range(columns):
                permeability = get_float_input(f"Enter the permeability for gridblock ({layer}, {row}, {column}): ")
                if permeability >= cut_off:
                    active_count += 1
                    active_count_layer += 1
                else:
                    inactive_count += 1
        
        print(f"Layer {layer}: {active_count_layer} active gridblocks")

    percentage_active = (active_count / total_gridblocks) * 100
    print(f"Total active gridblocks: {active_count}")
    print(f"Total inactive gridblocks: {inactive_count}")
    print(f"Percentage of active gridblocks in the entire reservoir: {percentage_active:.2f}%")

if __name__ == "__main__":
    layers = get_int_input("Enter the number of layers in the reservoir: ")
    rows = get_int_input("Enter the number of rows in each layer: ")
    columns = get_int_input("Enter the number of columns in each row: ")
    cut_off = get_float_input("Enter the permeability cut-off value: ")

    classify_gridblocks(layers, rows, columns, cut_off)
