from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while f.readline() != '':
            all_data.append(f.readline())


filenames = [f'./file {num}.txt' for num in range(1, 5)]


# start_time = datetime.now()
# if __name__ == '__main__':
#     for filename in filenames:
#         read_info(filename)
#
# end_time = datetime.now()
# print(f'Time: {end_time - start_time} (линейный)'


if __name__ == '__main__':
    start_time = datetime.now()
    for filename in filenames:
        process = multiprocessing.Process(target=read_info, args=(filename,))
        process.start()
        print(f'{filename} {process.pid} {process.is_alive()}')
    end_time = datetime.now()
    print(f'Time: {end_time - start_time} (многопроцессный)')
