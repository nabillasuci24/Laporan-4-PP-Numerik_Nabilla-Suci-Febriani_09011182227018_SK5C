import time
import multiprocessing

def gaussian_elimination_partial(A, start_row, end_row, process_id):
    start_time = time.time()
    for i in range(start_row, end_row):
        diag = A[i][i]
        for j in range(kolom):
            A[i][j] /= diag
        for k in range(i + 1, kolom):
            if k != baris:
                diag1 = A[k][i]
                for j in range(kolom):
                    A[k][j] = A[k][j] - diag1 * A[i][j]
    end_time = time.time()
    print(f"Process {process_id} execution time: {end_time - start_time} seconds")

if __name__ == '__main__':
    ordo = int(input("Masukkan ordo matrix : "))
    baris = ordo
    kolom = ordo + 1

    A = []
    for i in range(baris):
        matrix = []
        for j in range(kolom):
            matrix.append(0)
        A.append(matrix)

    for i in range(baris):
        print("Masukkan persamaan ke-%d" % (i + 1))
        for j in range(0, kolom):
            A[i][j] = int(input(f"Masukkan angka baris-{i + 1} kolom-{j + 1}: "))

    start_time = time.time()
    
    processes = []
    num_processes = 4
    rows_per_process = baris // num_processes

    for i in range(num_processes):
        start_row = i * rows_per_process
        end_row = (i + 1) * rows_per_process if i < num_processes - 1 else baris
        process = multiprocessing.Process(target=gaussian_elimination_partial, args=(A, start_row, end_row, i))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    for i in range(0, baris):
        for j in range(0, kolom):
            print("%4.2f" % (A[i][j]), end=" ")
        print("\n")

    x3 = A[2][3]
    x2 = A[1][3] - A[1][2] * x3
    x1 = A[0][3] - A[0][2] * x3 - A[0][1] * x2
    print("x1= %4.2f \nx2= %4.2f \nx3= %4.2f" % (x1, x2, x3))

    elapsed_time = end_time - start_time
    print("Total execution time for all processes: %f seconds"%elapsed_time)