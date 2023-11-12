import multiprocessing
import time

def f1(x):
    return x ** 2 - 20

def det_f1(x):
    return 2 * x

def newton_raphson(func, d_func, x, tolerence, max_iterations, real_root=None, process_id=0):
    if d_func(x) == 0:
        print("Newton-Raphson gagal dijalankan pada proses {0}.".format(process_id))
        return None
    else:
        iterations = 1
        start_time = time.time()
        while abs(func(x) / d_func(x)) >= tolerence and iterations <= max_iterations:
            current_iteration_print = "Proses {0}, Iterasi : {1}".format(process_id, iterations)
            if func(x) == 0:
                print(current_iteration_print + ", Solusi ditemukan : {0}".format(x))
                return x
            
            x = x - func(x) / d_func(x)
            if d_func(x) == 0:
                print("Newton-Raphson gagal dijalankan pada proses {0}.".format(process_id))
                return None
            current_iteration_print += ", {0}".format(x)
            iterations += 1
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            current_iteration_print += ", Waktu per Iterasi: {0} detik".format(elapsed_time)
            
            print(current_iteration_print)
        
        print("\nProses {0}, Jumlah iterasi : ".format(process_id), iterations)
        print("Proses {0}, Hasil akhir : ".format(process_id), x)

if __name__ == '__main__':
    processes = []
    inputs = [(f1, det_f1, 1.5, 0.00001, 30, 1, i) for i in range(4)]  # 4 proses

    for input_data in inputs:
        p = multiprocessing.Process(target=newton_raphson, args=input_data)
        processes.append(p)
        p.start()

    for process in processes:
      process.join()