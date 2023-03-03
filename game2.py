"Игра угадай число. V2 компьютер сам загадывает и сам разгадывает"

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадывает число

    Args:
        number (int, optional): _description_. Defaults to 1.Загаданное число

    Returns:
        int: _description_ Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) 
        if number == predict_number:
            break
    return(count)

    
print(f'Количество попыток: {random_predict(10)}')
   